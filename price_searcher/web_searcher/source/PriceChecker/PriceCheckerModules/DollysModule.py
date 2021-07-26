from .WebstoreInterface import WebstoreInterface
from bs4 import BeautifulSoup
from .ListedItem import ListedItem
import requests

shippingCost = 1.5

#module for facetoface games
class DollysModuleClass(WebstoreInterface):
    
    #generates the appropriate URL for the program to read them from
     def GenerateUrl(self, cardname):
        "generate the url to find the card"
        url_name_section = GenerateUrlString(cardname)
        url = "https://www.dollys.ca/products/search?q=" + url_name_section + "&c=1"
        return url
        
    #searches the search at the URL, and returns a list of all found cards
     def SearchForCard(self, cardname):
         url = self.GenerateUrl(cardname)
         webpage_as_text = requests.get(url)
         soup = BeautifulSoup(webpage_as_text.text, "html.parser")
         cardDisplay = soup.find(class_="products")
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
        cardListing = listing.find('div', class_='meta')
       # print(listing)
        try:
             name = cardListing.find(class_='name')['title']
             priceContainer = cardListing.find('div', class_="variant-row")
             inStock = priceContainer.find('span', {"class" : "variant-qty"}).text
             if inStock == "Out of stock.":
                 continue
             
             #remove the first 5 characters to remove CAD $
             try:
                 price = float(cardListing.find('span', {"class" : "regular price"}).text[5:])
             except ValueError:
                 print("Please let Valcon know there is an issue with the Dolly's website.")
             
        except AttributeError:
            continue
        
        card = ListedItem(name, price, 'Dolly\'s Toys and Games', shippingCost)
        cardList.append(card)
    
    return cardList