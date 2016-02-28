from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def start_page(request):
    now = datetime.datetime.now()
#    logo = 'logo2.png'
    return render_to_response('index.html', {'current_datetime': now})
#                                                'logo':logo})

#def image_exam(request):
