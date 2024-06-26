from Sensor.exception import SensorException
from Sensor.logger import logging
import os
import sys

def test_exception():
    """
    Function to test the custom SensorException by deliberately causing a ZeroDivisionError.
    """
    try:
        logging.info("Here is the error")
        a = 1 / 0  # Deliberate division by zero to trigger an exception
    except Exception as e:
        # Raise custom SensorException with the original exception and sys module for traceback
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        # Call the test_exception function to test the custom exception handling
        test_exception()
    except SensorException as e:
        # Print the custom error message from SensorException
        print(e)
