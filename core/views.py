from django.shortcuts import render,redirect
from .models import Item,Category
from . import models

def main(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'main.html',context)
   

def items(request,id=None):
    item=models.Item.objects.get(id=id)
    print(item)
    context={
        'item':item,
        'id':id
    }
    return render(request,'computer_forensic.html',context)


def index2(request):
    return render(request, 'index2.html')

def analytics(request):
    return render(request,'analytics.html')

def cloud_forensic(request):
    return render(request,'cloud_forensic.html') 

def computer_forensic(request):
    item = Item.objects.all()
    category=Category.objects.all()
    context = {
        'item': item,
        'category': category
          
         }
    return render(request,'computer_forensic.html',context)
    
def db_forensic(request):
    return render(request,'db_forensic.html')

def index(request):
    return render(request,'index.html')

def iot_forensic(request):
    return render(request,'iot_forensic.html')

def map(request):
    return render(request,'map.html')

def mobil_forensic(request):
    return render(request,'mobil_forensic.html')

def network_forensic(request):
    return render(request,'network_forensic.html')

def page_404_error(request):
    return render(request,'page_404_error.html')

def page_coming_soon(request):
    return render(request,'page_coming_soon.html')

def page_login(request):
    return render(request,'page_login.html')

def page_register(request):
    return render(request,'page_register.html')

def pos_customer_order(request):
    return render(request,'pos_customer_order.html')

def pos_menu_stock(request):
    return render(request,'pos_menu_stock.html')

def settings(request):
    return render(request,'settings.html')

def ui_icons(request):
    return render(request,'ui_icons.html')


 