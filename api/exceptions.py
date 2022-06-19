"""Api exceptions list"""

# General
class ApiException(Exception):
    """Base class for Api exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MissingParameters(ApiException):
    """Raised when one or more parameters are missing"""
    def __init__(self, missing_params: list):
        super().__init__(f"Missing parameters: {missing_params}")

class InvalidParameters(ApiException):
    """Raised when one or more parameters are invalid"""
    def __init__(self, invalid_params: list):
        super().__init__(f"Invalid parameters: {invalid_params}")

# Reports
class NoReportsFound(ApiException):
    """
    Exception raised when no reports are found in the database.
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

class ReportAlreadyExists(ApiException):
    """
    Exception raised when a report already exists (duplicated report_id)
    
    Args:
        report_id: id of the report
    """
    def __init__(self, report_id: str):
        super().__init__(f"Report with report_id '{report_id}' already exists")
