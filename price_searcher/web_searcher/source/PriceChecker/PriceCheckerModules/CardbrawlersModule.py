from .WebstoreInterface import WebstoreInterface
from bs4 import BeautifulSoup
from .ListedItem import ListedItem
import requests

shippingCost = 1.5

#module for facetoface games
class CBModuleClass(WebstoreInterface):
    
    #generates the appropriate URL for the program to read them from
     def GenerateUrl(self, cardname):
        "generate the url to find the card"
        url_name_section = GenerateUrlString(cardname)
        url = "https://cardbrawlers.com/search?q=" + url_name_section + "*+product_type%3A%22yugioh%22"
        return url
        
     def SearchForCard(self, cardname):
         url = self.GenerateUrl(cardname)
         webpage_as_text = requests.get(url)
         cardDisplay = BeautifulSoup(webpage_as_text.text, "html.parser")
         cards = cardDisplay.find_all('div', class_='col-lg-9')[0].find_all('div', class_='row')[0].find_all('div', class_='product Norm')
         cardList = FormatCardList(cards)
         return cardList

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
        name = listing.find('p', class_='productTitle').text.strip()
        price = listing.find('p', class_='productPrice').text.strip()
        if price == "Varies":
            conditions = listing.find_all('div', class_='addNow')
            for condition in conditions:
                enteredString = condition.text.strip()
                listReturned = separateData(enteredString)
                card = ListedItem(name + " - " + listReturned[0], listReturned[1], "CardBrawlers", shippingCost)
                cardList.append(card)
            continue
        elif price == "Sold Out":
            continue
        price = price[1:]
        card = ListedItem(name, price, "CardBrawlers", shippingCost)
        cardList.append(card)
    
    return cardList

def separateData(enteredString):
    num = 0
    for char in enteredString:
        if char == '$':
            break
        else:
            num += 1
    condition = enteredString[:num-3]
    price = enteredString[num+1:]
    listReturned = [condition, price]
    
    return listReturned