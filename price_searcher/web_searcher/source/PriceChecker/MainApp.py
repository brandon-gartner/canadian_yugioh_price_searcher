from bs4 import BeautifulSoup
import PriceCheckerModules.ListedItem
from PriceCheckerModules.F2FModule import F2FModuleClass
from PriceCheckerModules.CardbrawlersModule import CBModuleClass
from PriceCheckerModules.FourZeroOneModule import Four01ModuleClass
from PriceCheckerModules.DollysModule import DollysModuleClass
from PriceCheckerModules.GKVerdunModule import GKVerdunModuleClass
from PriceCheckerModules.GKOnlineModule import GKOnlineModuleClass

def checkPrice(card):
    return card.cost

class MainCardSearcher:
    
    def __init__(self):
        self.faceSearcher = F2FModuleClass()
        self.cardbrawlersSearcher = CBModuleClass()
        self.gkVerdunSearcher = GKVerdunModuleClass()
        self.gkOnlineSearcher = GKVerdunModuleClass()
        self.dollySearcher = DollysModuleClass()
        #instantiate one of each searcher


        #broken, seemingly require selenium
        #four01Searcher = Four01ModuleClass()


    
    def getCardPricesList(self):
        #get input from user
        userInput = str(input())
        
        #add found cards to each
        cardList = []
        cardList.extend(self.faceSearcher.SearchForCard(userInput))
        cardList.extend(self.cardbrawlersSearcher.SearchForCard(userInput))
        cardList.extend(self.gkVerdunSearcher.SearchForCard(userInput))
        cardList.extend(self.gkOnlineSearcher.SearchForCard(userInput))
        cardList.extend(self.dollySearcher.SearchForCard(userInput))
        
        #broken, seemingly need selenium
        #cardList.extend(four01Searcher.SearchForCard(userInput))
        
        #sort by price descending
        cardList.sort(key=checkPrice)
        
        return cardList

