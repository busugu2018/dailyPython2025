# Quick OOP:

class travelTicket:
    def __init__(self, source, destination, date, price):
        self._source = source
        self._date = date
        self._price = price
        self._destination = destination

    def get_source(self):
        return self._source
    
    def set_source(self, source):
        self._source = source

    def get_destination(self):
        return self._destination
    
    def set_destination(self, destination):
        self._destination = destination

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price

# Creting an object
ticket1 = travelTicket("NY", "Saigon", "2024-05-15", 1100)

# Access the current values
print("Origin: ", ticket1.get_source())
print("Destination: ", ticket1.get_destination())
print("Date: ", ticket1.get_date())
print("Price: ", ticket1.get_price())

#Edit our encapsulated attributes using out setter methods
ticket1.set_price(800)
ticket1.set_destintion("Hong Kong")

# Access updated values
print("Modified destinatiom: ", ticket1.get_destintion())
print("Modified price: ", ticket1.get_price())

