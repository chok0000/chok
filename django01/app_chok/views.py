from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "สมชาย"
    age = "30"
    return render(request,"index.html",{"name":name,"age":age})
def about(request):
    return render(request,"about.html")

def gallery(request):
    return render(request,"gallery.html")
def blog(request):
    return render(request,"blog.html")