from field import Field
from utils.is_valid_phone import is_valid_phone

class Phone(Field):
    def __init__(self, phone):
        if not is_valid_phone(phone):
            raise TypeError
        super().__init__(phone)
