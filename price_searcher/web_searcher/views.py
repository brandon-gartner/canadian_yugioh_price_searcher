from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MainApp import MainCardSearcher
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'card_listings': {
            "listing": {
                "name": "Blue-Eyes White Dragon - LOB-EN001 - 1st Edition",
                "vendor": "Cardbrawlers",
                "price": "$100.00",
                "shipping_cost": "$1.50",
            }
        }
    }
    return HttpResponse(template.render(context, request))

def result(request):
    template = loader.get_template('results.html')
    searcher = MainCardSearcher()
    cardList = searcher.getCardPricesList()
    context = {
        'card_listings': {
            cardList,
        }
    }
    return HttpResponse(template.render(context, request))