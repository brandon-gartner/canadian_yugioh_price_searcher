from .WebstoreInterface import WebstoreInterface
from bs4 import BeautifulSoup
from .ListedItem import ListedItem
import requests

shippingCost = 1.5

#module for facetoface games
class F2FModuleClass(WebstoreInterface):
    
    #generates the appropriate URL for the program to read them from
     def GenerateUrl(self, cardname):
        "generate the url to find the card"
        url_name_section = GenerateUrlString(cardname)
        url = "https://www.facetofacegames.com/search.php?search_query=" + url_name_section + "&section=product&_bc_fsnf=1&in_stock=1&category=4878"
        return url
        
    #searches the search at the URL, and returns a list of all found cards
     def SearchForCard(self, cardname):
         url = self.GenerateUrl(cardname)
         webpage_as_text = requests.get(url)
         soup = BeautifulSoup(webpage_as_text.text, "html.parser")
         cardDisplay = soup.find(class_="productGrid")
         cards = cardDisplay.find_all('li', class_='product')
         cardList = FormatCardList(cards)
         return cardList

#formats the search into the appropriate way for the website
def GenerateUrlString(cardname):
        words = cardname.split()
        urlstring = ""
        for word in words:
            urlstring += word
            urlstring += "_"
        endurlstring = urlstring[:-1]
        return endurlstring
    
#formats their listings into individual listing objects, which we return
def FormatCardList(productList):
    cardList = []
    for listing in productList:
        cardListing = listing.find('article', class_='card')
        name = cardListing['data-name']
        try:
           price = float(cardListing['data-product-price'])
        except ValueError:
            print("Contact Valcon, FaceToFace site has been modified.")
        
        card = ListedItem(name, price, 'FaceToFace', shippingCost)
        cardList.append(card)
    
    return cardList