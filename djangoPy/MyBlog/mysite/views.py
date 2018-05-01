from django.shortcuts import render
# from django.http import HttpResponse
from .models import Article
import datetime

def index(request):
    blogAllList = Article.objects.all()
    context = {}
    # now = datetime.datetime.now()
    # context['hello'] = "Hello World "
    context['blogAllList'] = blogAllList
    # context['username']    = request.user.username

    # context['date']  = 'date is %s' % now
    
    return render(request, 'home.html', context)