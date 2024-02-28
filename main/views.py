from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request) -> HttpResponse:
     context={
    'title':'Home',
    'content':'Main Stranica-Home',
    'dict':{'asd':1},
    'Bool':True
    }
     return render(request,'main/index.html',context)

def about(request) -> HttpResponse:
    return HttpResponse('About Page')