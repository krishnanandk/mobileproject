from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm
from mobile.models import Brands


def get_brandindex(request):
   return render(request,"index.html")

def create_brands(request):
    if request.method=="GET":
       form=BrandCreateForm()
       context={}
       context["form"]=form
       return render(request,"createbrand.html",context)

    elif request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            brandname=form.cleaned_data.get("brand_name")

            brand = Brands(brand_name=brandname)
            brand.save()
            return render(request,"index.html")


def list_all_brands(request):
    brand=Brands.objects.all()
    context={}
    context["brands"]=brand
    return render(request,"listallbrands.html",context)


def delete_brands(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("list")

def update_brands(request,id):
    brand=Brands.objects.get(id=id)
    dict={
        "brand_name":brand.brand_name

     }
    form=BrandCreateForm(initial=dict)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            brandname=form.cleaned_data.get("brand_name")

            brand.brand_name=brandname

            brand.save()
            return redirect("list")
    return render(request,"update.html",context)