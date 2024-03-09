from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories
# Create your views here.
def index(request) -> HttpResponse:
     categories =Categories.objects.all()
     context={
    'title':'Home',
    'content':'Main Stranica-Home',
    'categories':categories,
    }
     return render(request,'main/index.html',context)


def about(request) -> HttpResponse:
     context={
    'title':'Home-О нас',
    'content':'о нас',
    'text_on_page':"lorem5"
    }
     return render(request,'main/about.html',context)
