from .WebstoreInterface import WebstoreInterface
from bs4 import BeautifulSoup
from .ListedItem import ListedItem
import requests

shippingCost = 1.5

#module for facetoface games
class Four01ModuleClass(WebstoreInterface):
    
    #generates the appropriate URL for the program to read them from
     def GenerateUrl(self, cardname):
        "generate the url to find the card"
        url_name_section = GenerateUrlString(cardname)
        url = "https://store.401games.ca/pages/search-results?q=" + url_name_section + "&narrow=%5B%5B%22Type%22%2C%22Yugioh%22%5D%5D&disable_semantics=1&page_num=3"
        return url
        
    #searches the search at the URL, and returns a list of all found cards
     def SearchForCard(self, cardname):
         url = self.GenerateUrl(cardname)
         webpage_as_text = requests.get(url)
         soup = BeautifulSoup(webpage_as_text.text, "html.parser")
         cardDisplay = soup.find(id="isp_search_results_container")
         print(type(cardDisplay))
         cards = cardDisplay.find_all('li', class_='isp_grid_product')
         cardList = FormatCardList(cards)
         return cardList

#formats the search into the appropriate way for the website
def GenerateUrlString(cardname):
        return cardname
    
#formats their listings into individual listing objects, which we return
def FormatCardList(productList):
    cardList = []
    for listing in productList:
        print(type(listing))
        print(listing)
        titleContainer = listing.find('div', class_='isp_product_title')
        print(titleContainer.strip())
        priceContainer = listing.find('div', class_='isp_product_price_money')
        print(type(priceContainer))
        price = priceContainer['data-currency-cad'][1:-4]
        print(price)
        cardListing = listing.find('li', class_='caraaaad')
        print(type(cardListing))
        name = cardListing['data-name']
        try:
           price = float(cardListing['data-product-price'])
        except ValueError:
            print("Contact Valcon, 401 Games site has been modified.")
        
        card = ListedItem(name, price, '401 Games', shippingCost)
        cardList.append(card)
    
    return cardList