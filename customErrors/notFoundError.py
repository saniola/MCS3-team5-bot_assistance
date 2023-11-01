class NotFoundError(Exception):
    def __init__(self, search_param):
        self.message = f"There are no {search_param} matching the search criteria"
        super().__init__(self)
