from django.shortcuts import render

# Create your views here.

def brain(request):
    return render(request,'brain.html')

def heart(request):
    return render(request,'heart.html')
