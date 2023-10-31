from models.field import Field
from utils.is_valid_email import is_valid_email

class Email(Field):
    def __init__(self, email):
        if not is_valid_email(email):
            raise TypeError
        super().__init__(email)
