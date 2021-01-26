from django.shortcuts import render, HttpResponse
from .models import Materials

# Create your views here.
def index(request):
    return render(request, 'index.html')

def shop(request):
    mat1 = Materials()
    mat1.name = 'black kid wear'
    mat1.img = 'kid1.jpg'
    mat1.price = 499

    mat2 = Materials()
    mat2.name = 'black kid wear'
    mat2.img = 'kid1.jpg'
    mat2.price = 499

    mat3 = Materials()
    mat3.name = 'black kid wear'
    mat3.img = 'kid1.jpg'
    mat3.price = 499

    mat4 = Materials()
    mat4.name = 'black kid wear'
    mat4.img = 'kid1.jpg'
    mat4.price = 499
  
    mats=[mat1,mat2,mat3,mat4]

    return render(request, 'shop.html', {'mats':mats})

def cart(request):
    return render(request, 'cart.html')    

def wishlist(request):
    return render(request, 'wishlist.html')      

 