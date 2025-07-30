from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys
logging.info("Logging is set up successfully.")


try:
    a = 1 / 0
except Exception as e:
    logging.error("An error occurred: %s", e)
    raise USvisaException(e, sys) from e