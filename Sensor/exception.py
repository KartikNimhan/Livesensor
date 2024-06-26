import sys
import os

def error_message_details(error, error_detail):
    """
    This function extracts and formats error details.
    :param error: The error message or exception instance.
    :param error_detail: The sys module to extract error details.
    :return: A formatted error message string.
    """
    exc_type, exc_value, exc_tb = error_detail.exc_info()  # Correct way to get the exception info
    filename = exc_tb.tb_frame.f_code.co_filename  # Extract the filename where the exception occurred
    line_number = exc_tb.tb_lineno  # Extract the line number where the exception occurred

    # Correctly format the error message string
    error_message = "Error occurred in file [{0}] at line [{1}]: {2}".format(
        filename, line_number, str(error)
    )

    return error_message


class SensorException(Exception):
    """
    Custom exception class for handling sensor errors.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize SensorException with an error message and error details.
        :param error_message: The error message or exception instance.
        :param error_detail: The sys module to extract error details.
        """
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        """
        Return a string representation of the error message.
        """
        return self.error_message


