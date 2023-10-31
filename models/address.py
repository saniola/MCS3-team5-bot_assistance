from models.field import Field


class Address(Field):
    def __init__(self):
        super().__init__(None)

    @property
    def address(self):
        print(type(self.value))
        return self.value

    @address.setter
    def address(self, new_value):
        if len(new_value) <= 1:
            raise ValueError
        self.value =  new_value
