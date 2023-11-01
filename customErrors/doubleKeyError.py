from models.record import Record


class DoubleKeyError(Exception):
    def __init__(self, record: Record, new_name):
        self.message = f"Address book already has record with name {new_name}. \n{str(record)}"
        super().__init__(self)
