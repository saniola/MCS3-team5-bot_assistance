import pickle
from collections import UserDict, defaultdict
from utils.get_next_week_birthdays import get_next_birthdays
from utils.print_results import print_results

class AddressBook(UserDict):
    data_file_name = './data/addres_book.bin'

    def __init__(self):
        try:
            with open(AddressBook.data_file_name, 'rb') as fn:
                self.data = pickle.load(fn)
        except FileNotFoundError:
            super().__init__(self)

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self, days):
        return get_next_birthdays(self.data, days)

    def save(self):
        with open(AddressBook.data_file_name, 'wb') as fn:
            pickle.dump(self, fn)
