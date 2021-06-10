from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse('Homepage - Welcome')
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('About - Welcome This is a django tutorial introduction')
    return render(request, 'about.html')
