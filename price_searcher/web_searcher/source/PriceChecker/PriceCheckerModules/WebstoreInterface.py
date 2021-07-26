from abc import ABC, abstractmethod

#webstore interface
class WebstoreInterface(ABC):
    
    #generate the url it will check
    @abstractmethod
    def GenerateUrl(self, cardname):
        "generate the url to find the card"
        pass
    
    #searches the site for the card and returns the resulting list
    @abstractmethod
    def SearchForCard(self, cardname):
        "search for the card, for now simply return a listeditem of each"
        pass