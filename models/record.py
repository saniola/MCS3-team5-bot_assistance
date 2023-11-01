from models.email import Email
from models.birthday import Birthday
from models.name import Name
from models.phone import Phone
from models.address import Address
from utils.is_valid_phone import is_valid_phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"\
            f"{', email: ' + self.email.value if self.email is not None else ''}"\
            f"{', birthday: ' + self.birthday.value if self.birthday is not None else ''}"\
            f"{', ' + str(self.address) if self.address is not None else ''}"
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [item for item in self.phones if item.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if is_valid_phone(new_phone):
            for item in self.phones:
                if item.value == old_phone:
                    item.value = new_phone
                    return
            raise KeyError
        else:
            raise TypeError

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item.value
        raise KeyError

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        if self.birthday:
            return f"Birthday for {self.name.value}: {self.birthday.value}"
        return f"No birthday set for {self.name.value}"
    
    def add_email(self, email):
        self.email = Email(email)    

    def change_email(self, email):
        self.email = Email(email)

    def change_name(self, new_name):
        self.name.value = new_name

    def isPhoneExists(self, phone):
        for item in self.phones:
            if item.value == phone:
                return True
        return False
    def add_address(self, city) -> Address:
        self.address = Address(city)
        return self.address
    
    def del_address(self):
        self.address = None
        
