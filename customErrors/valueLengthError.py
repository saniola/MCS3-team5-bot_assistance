class ValueLengthError(Exception):
    message = "The search string must have at least 2 characters"
    def __init__(self):
        super().__init__(self)
