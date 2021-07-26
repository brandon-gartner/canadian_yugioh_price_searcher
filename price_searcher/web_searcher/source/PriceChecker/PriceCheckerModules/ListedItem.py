#a container to create a basic listing, which we can search through, etc.
class ListedItem:
    
    #a basic constructor
    def __init__(self, name, cost, webstore_name, webstore_ship_cost):
        self.name = name
        self.cost = float(cost)
        self.webstore_ship_cost = webstore_ship_cost
        self.webstore_name = webstore_name
        self.individualcost = round((self.cost + self.webstore_ship_cost) * 1.15, 2)
        
    #gives a basic string representation of the card
    def __str__(self):
        stringversion = (self.name + "\n$" + str(self.cost) + "\n" + self.webstore_name + "\n" + "(Total cost if bought individually: $" + str(self.individualcost) + ")\n")
        return stringversion
    
    