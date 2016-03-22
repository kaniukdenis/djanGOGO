# coding: utf-8
from django.shortcuts import render
from public.models import Public, Comments
from django.shortcuts import render_to_response, Http404, redirect
from django.core.exceptions import ObjectDoesNotExist
from public.forms import CommentForm
from django.core.context_processors import csrf




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
                                                'culture4':culture[3],})
    
def science(request):
    science = Public.objects.filter(theme = "Science").order_by('-date_pub')[:9]
    return render_to_response('science2.html',{'science1':science[0],
                                                'science2':science[1],
                                                'science3':science[2],
                                                'science4':science[3],
                                                'science5':science[4],
                                                'science6':science[5],
                                                'science7':science[6],
                                                'science8':science[7],
                                                'science9':science[8]})
    

def society(request):
    society = Public.objects.filter(theme = "Society").order_by('-date_pub')[:9]
    return render_to_response('society.html',{'society1':society[0],
                                              'society2':society[1],
                                              'society3':society[2],
                                              'society4':society[3],
                                              'society5':society[4],
                                              'society6':society[5],
                                              'society7':society[6],
                                              'society8':society[7],
                                              'society9':society[8]})

def policy(request):
    policy = Public.objects.filter(theme = "Policy").order_by('-date_pub')[:9]
    return render_to_response('policy.html',{'policy1':policy[0],
                                             'policy2':policy[1],
                                             'policy3':policy[2],
                                             'policy4':policy[3],
                                             'policy5':policy[4],
                                             'policy6':policy[5],
                                             'policy7':policy[6],
                                             'policy8':policy[7],
                                             'policy9':policy[8],})

def bussiness(request):
    bussiness = Public.objects.filter(theme = "Bussiness").order_by('-date_pub')[:9]
    return render_to_response('bussiness.html',{'bussiness1':bussiness[0],
                                               'bussiness2':bussiness[1],
                                               'bussiness3':bussiness[2],
                                               'bussiness4':bussiness[3],
                                               'bussiness5':bussiness[4],
                                               'bussiness6':bussiness[5],
                                               'bussiness7':bussiness[6],
                                               'bussiness8':bussiness[7],
                                               'bussiness9':bussiness[8]})

def culture(request):
    culture = Public.objects.filter(theme = "Culture").order_by('-date_pub')[:9]
    return render_to_response('culture.html',{'culture1':culture[0],
                                              'culture2':culture[1],
                                              'culture3':culture[2],
                                              'culture4':culture[3],
                                              'culture5':culture[4],
                                              'culture6':culture[5],
                                              'culture7':culture[6],
                                              'culture8':culture[7],
                                              'culture9':culture[8]})

def detail(request, public_id):
    return render_to_response('article.html', {'public':Public.objects.get(id = public_id)})

def addlikes(request, public_id):
    try:
        public = Public.objects.get(id = public_id)
        public.likes += 1
        public.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/{{science}}/%s' % public_id)


def adddislikes(request, public_id):
    try:
        public = Public.objects.get(id = public_id)
        public.dislikes += 1
        public.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/science/%s/' % public_id)

def detail(request, public_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['public'] = Public.objects.get(id = public_id)
    args['comments'] = Comments.objects.filter(comments_public_id = public_id)
    args['form'] = comment_form
    return render_to_response('article.html', args)

def addcomment(request , public_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comments_public = Public.objects.get(id = public_id)
            form.save()
    return redirect('science/%s' % public_id)
    
    
