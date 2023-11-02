class Address():
    def __init__(self, city):
        if len(city) <= 1:
            raise TypeError("city should have more than one letter")
        self.city = city
        self.street = None
        self.house = None
        self.apartment = None

    def set_street(self, street):
        if len(street) <= 1:
            raise TypeError("street should have more than one letter")
        self.street = street
        
    def set_house(self, house: str):
        if self.street is None:
            raise TypeError("street have to be not empty")
        if len(house) < 1:
            raise TypeError("house number can't be empty")
        self.house =  house
    
    def set_apartment(self, apartment: str):
        if self.street is None:
            raise TypeError("street have to be not empty")
        if self.house is None:
            raise TypeError("house number have to be not empty")
        if len(apartment) < 1:
            raise TypeError("apartment number can't be empty")
        self.apartment = apartment
    
    def __str__(self):
        return f"city: {self.city}"\
         f"{', street: '+self.street if self.street is not None else ''}"\
         f"{', house: '+self.house if self.house is not None else ''}"\
         f"{', apartment: '+self.apartment if self.apartment is not None else ''}\n"
        