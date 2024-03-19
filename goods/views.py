from django.shortcuts import render
import goods
from goods.models import Products
# Create your views here.
goods=Products.objects.all()
def catalog(request):
    context={
        

        'title':'catalog',
        "goods" : goods,
    }
    return render(request,'goods/catalog.html',context)

def product(request):
    return render(request,'goods/product.html')