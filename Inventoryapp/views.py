from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from datetime import datetime as dt


from Inventoryapp.models import InventoryappOrdertbl, InventoryappProduct

# Create your views here.

class ProductPage(View):
    def get(self,request):
        return render(request,'productupload.html')

class ProductEntry(View):
    def post(self,request):
        Name = request.POST['Name']
        Category = request.POST['Category']
        Quantity =request.POST['Quantity']
        Price = request.POST['Price']
        result = InventoryappProduct(Name=Name,Category=Category,Quantity=Quantity,Price=Price)
        result.save()
        return JsonResponse({"status":"success"})
    
    
       
    
class ProductDisplay(View):
    def get(self,request):
        data = InventoryappProduct.objects.all()
        return render(request,'productview.html',{'data':data})
    
class Ordercreation(View):
    def get(self,request):
        data = InventoryappProduct.objects.all()
        return render(request,'OrderCreation.html',{'data':data})
    


class OrderCreation(View):
    def post(self,request):
        proudctid = request.POST['productid']
        Quantity = request.POST['Quantity']
        TotalPrice = request.POST['TotalPrice']
        date =dt.now()
        result = InventoryappOrdertbl(quantity=Quantity,totalprice=TotalPrice,date=date,productid=proudctid)
        result.save()
        data = InventoryappProduct.objects.get(id= proudctid)
        stock_decraese =  data.Quantity - 1
        data.Quantity = stock_decraese
        data.save()
        return JsonResponse({"status":"success"})