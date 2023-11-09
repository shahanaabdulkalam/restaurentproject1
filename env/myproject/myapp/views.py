from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def menupage(request):
    return render(request,'menupage.html')
def aboutpage(request):
    return render(request,'aboutpage.html')