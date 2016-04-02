# coding: utf-8

from django.shortcuts import render
from public.models import Public, Comments
from django.shortcuts import render_to_response, Http404, redirect
from django.core.exceptions import ObjectDoesNotExist
from public.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth 


def spisok(request):
    news = Public.objects.all().order_by('-date_pub')
    return render_to_response('allnews.html', {'news':news})

def mainnews(request):
    mainnews = Public.objects.all().order_by('-date_pub')[:6]
    science = Public.objects.filter(theme = "Science").order_by('-date_pub')[:4]
    society = Public.objects.filter(theme = "Society").order_by('-date_pub')[:4]
    policy = Public.objects.filter(theme = "Policy").order_by('-date_pub')[:4]
    bussiness = Public.objects.filter(theme = "Bussiness").order_by('-date_pub')[:4]
    culture = Public.objects.filter(theme = "Culture").order_by('-date_pub')[:4]
    return render_to_response('mainnews.html',{'mainnews1':mainnews[0],
                                                'mainnews2':mainnews[1],
                                                'mainnews3':mainnews[2],
                                                'mainnews4':mainnews[3],
                                                'mainnews5':mainnews[4],
                                                'mainnews6':mainnews[5],
                                               'science1':science[0],
                                                'science2':science[1],
                                                'science3':science[2],
                                                'science4':science[3],
                                               'society1':society[0],
                                                'society2':society[1],
                                                'society3':society[2],
                                                'society4':society[3],
                                               'policy1':policy[0],
                                                'policy2':policy[1],
                                                'policy3':policy[2],
                                                'policy4':policy[3],
                                               'bussiness1':bussiness[0],
                                                'bussiness2':bussiness[1],
                                                'bussiness3':bussiness[2],
                                                'bussiness4':bussiness[3],
                                               'culture1':culture[0],
                                                'culture2':culture[1],
                                                'culture3':culture[2],
                                                'culture4':culture[3],
                                                'user': auth.get_user(request).username})

def theme(request, theme):
    items = Public.objects.filter(theme = theme ).order_by('-date_pub')[:9]
    return render_to_response('kindofnews.html',{'news1':items[0],
                                                'news2':items[1],
                                                'news3':items[2],
                                                'news4':items[3],
                                                'news5':items[4],
                                                'news6':items[5],
                                                'news7':items[6],
                                                'news8':items[7],
                                                'news9':items[8]})
    

def detail(request, public_id):
    user = auth.get_user(request).username
    science = bussiness = society = policy = culture = "pannel"
    public = Public.objects.get(id = public_id)
    if public.theme == "Science":
        science = "active"
    elif public.theme == "Bussiness":
        bussiness = "active"
    elif public.theme == "Society":
        society = "active"
    elif public.theme == "Policy":
        policy = "active"
    elif public.theme == "Culture":
        culture = "active"
    
    return render_to_response('article.html', {'public':Public.objects.get(id = public_id),
                                               'science':science,
                                               'bussiness':bussiness,
                                               'society':society,
                                               'policy':policy,
                                               'culture':culture,
                                               'user': user})
def pannel():
    science = bussiness = society = policy = culture = "pannel"
    public = Public.objects.get(id = public_id)
    if public.theme == "Science":
        science = "active"
    elif public.theme == "Bussiness":
        bussiness = "active"
    elif public.theme == "Society":
        society = "active"
    elif public.theme == "Policy":
        policy = "active"
    elif public.theme == "Culture":
        culture = "active"

def addlikes(request, public_id):
    user = auth.get_user(request)
    public = Public.objects.get(id = public_id)
    publics_with_likes = Public.objects.filter(users_likes = user)
    if public in publics_with_likes:
      public.likes -= 1
      public.users_likes.remove(user)
      public.save()
    else:
      public.likes += 1
      article.users_likes.add(user)
      public.save()
    return redirect('/mainnews/')


def adddislikes(request, public_id):
    user = auth.get_user(request)
    public = Public.objects.get(id = public_id)
    publics_with_dislikes = Public.objects.filter(users_dislikes = user)
    if public in publics_with_dislikes:
      public.dislikes -= 1
      public.users_dislikes.remove(user)
      public.save()
    else:
      public.dislikes += 1
      article.users_dislikes.add(user)
      public.save()
    return redirect('/science/%s/' % public_id)
#def detail(request, public_id):
#    comment_form = CommentForm
#    args = {}
#    args.update(csrf(request))
#    args['public'] = Public.objects.get(id = public_id)
#    args['comments'] = Comments.objects.filter(comments_public_id = public_id)
#    args['form'] = comment_form
#    return render_to_response('article.html', args)

def addcomment(request , public_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comments_public = Public.objects.get(id = public_id)
            form.save()
    return redirect('science/%s' % public_id)