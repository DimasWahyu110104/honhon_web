from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import pesanan

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def ini_model(request):
    data = pesanan.object.all().values()[:5]
    layout = loader.get_template('ini_model.html')
    context = {
        'data': data
    }
    return HttpResponse(layout.render(context))

