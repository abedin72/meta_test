from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"MetaModel/pages/home.html",)
     # return HttpResponse("aa")

def general(request):
    return render(request,"MetaModel/pages/metavers/general.html",)
def metahealth(request):
    return render(request,"MetaModel/pages/metavers/metahealth.html",)
def marketing(request):
    return render(request,"MetaModel/pages/metavers/marketing.html",)

def object(request):
    return render(request,"MetaModel/pages/shop/object.html",)

def nft_a(request):
    return render(request,"MetaModel/pages/nft/nft_a.html",)
def nft_b(request):
    return render(request,"MetaModel/pages/nft/nft_b.html",)
def nft_c(request):
    return render(request,"MetaModel/pages/nft/nft_c.html",)

def map(request):
    return render(request,"MetaModel/pages/land/map.html",)
def three_d(request):
    return render(request,"MetaModel/pages/land/three_d.html",)
def meta(request):
    if request.user.is_authenticated and request.user.is_active:
      return render(request,"MetaModel/pages/land/meta.html",)
    else:
      return render(request,"accounts/login.html",) 
    #   return HttpResponse("please login or signup your account") 
   
def chart_a(request):
    return render(request,"MetaModel/pages/charts/chart_a.html",)
def chart_b(request):
    return render(request,"MetaModel/pages/charts/chart_b.html",)
def chart_c(request):
    return render(request,"MetaModel/pages/charts/chart_c.html",)
    
def white_paper(request):
    return render(request,"MetaModel/pages/white paper/white paper.html",)

