class NotFoundError(Exception):
    def __init__(self):
        self.message = "There are no records matching the search criteria"
        super().__init__(self)
