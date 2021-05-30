from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main_page(request):
    template = loader.get_template('main_page.html')
    context = {

    }
    return HttpResponse(template.render(context, request))