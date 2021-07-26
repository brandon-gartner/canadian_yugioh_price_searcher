# -*- coding: utf-8 -*-
from MainApp import MainCardSearcher

searcher = MainCardSearcher()
cardList = searcher.getCardPricesList()
for card in cardList:
    print(card)