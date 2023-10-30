from datetime import datetime
from field import Field

class Birthday(Field):
    def __init__(self, birthday):
        try:
            datetime.strptime(birthday, '%d.%m.%Y')
        except ValueError:
            raise TypeError
        super().__init__(birthday)
