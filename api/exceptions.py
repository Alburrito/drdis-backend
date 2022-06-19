"""Api exceptions list"""

# General
class ApiException(Exception):
    """Base class for Api exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Database
class CollectionNotFound(ApiException):
    """
    Exception raised when a database collection is not found
    
    Args:
        collection_name: name of the collection
    """
    def __init__(self, collection_name: str):
        super().__init__(f"Collection '{collection_name}' not found")

# Reports
class NoReportsFound(ApiException):
    """
    Exception raised when no reports are found
    """
    def __init__(self):
        super().__init__("No reports found")

class ReportNotFound(ApiException):
    """
    Exception raised when a report is not found
    
    Args:
        report_id: id of the report
    """
    def __init__(self, report_id: str):
        super().__init__(f"Report '{report_id}' not found")
