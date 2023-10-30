from birthday import Birthday
from name import Name
from phone import Phone
from utils.is_valid_phone import is_valid_phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

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
