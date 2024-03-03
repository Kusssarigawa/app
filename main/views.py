from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request) -> HttpResponse:
     context={
    'title':'Home',
    'content':'Main Stranica-Home',
 
    }
     return render(request,'main/index.html',context)


def about(request) -> HttpResponse:
     context={
    'title':'Home-О нас',
    'content':'о нас',
    'text_on_page':"lorem5"
    }
     return render(request,'main/about.html',context)
