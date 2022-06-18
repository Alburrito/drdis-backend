"""Api exceptions list"""

class ApiException(Exception):
    """Base class for Api exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
