from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Item

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    context={'key':'value', 'name':'Hello Wasit!'}
    return render(request, 'home.html', context)

def item_list(request):
    context = {'items' : Item.objects.all()}
    return render(request, 'item_list.html', context)   

