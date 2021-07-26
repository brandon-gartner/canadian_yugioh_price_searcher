from .WebstoreInterface import WebstoreInterface
from bs4 import BeautifulSoup
from .ListedItem import ListedItem
import requests

shippingCost = 1.5

#module for facetoface games
class GKOnlineModuleClass(WebstoreInterface):
    
    #generates the appropriate URL for the program to read them from
     def GenerateUrl(self, cardname):
        "generate the url to find the card"
        url_name_section = GenerateUrlString(cardname)
        url = "https://www.gamekeeperonline.com/products/search?q=" + url_name_section
        return url
        
    #searches the search at the URL, and returns a list of all found cards
     def SearchForCard(self, cardname):
         url = self.GenerateUrl(cardname)
         webpage_as_text = requests.get(url)
         soup = BeautifulSoup(webpage_as_text.text, "html.parser")
         cardDisplay = soup.find(class_="products-container")
         cards = cardDisplay.find_all('li', class_='product')
         cardList = FormatCardList(cards)
         return cardList

#formats the search into the appropriate way for the website
def GenerateUrlString(cardname):
        words = cardname.split()
        urlstring = ""
        for word in words:
            urlstring += word
            urlstring += "+"
        endurlstring = urlstring[:-1]
        return endurlstring
    
#formats their listings into individual listing objects, which we return
def FormatCardList(productList):
    cardList = []
    for listing in productList:
        checkIfInStock = listing.find("span", {"class" : "variant-short-info"}).text
        if checkIfInStock == 'Hors stock.':
            continue
        
        #the cutting at the end is to remove "CAD $" from each listing
        price = float(listing.find("span", {'class' : "regular price"}).text[5:])
        
        name = listing.find('h4')['title']
        
        card = ListedItem(name, price, 'GameKeeper Online', shippingCost)
        cardList.append(card)
    
    return cardList