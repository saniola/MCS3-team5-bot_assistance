from collections import UserDict, defaultdict
from utils.get_next_week_birthdays import get_next_week_birthdays
from utils.print_results import print_results

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        get_next_week_birthdays(self.data, birthdays_per_week)
        return print_results(birthdays_per_week)
