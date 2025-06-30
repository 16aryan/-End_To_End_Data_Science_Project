import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from exception import CustomException


try:
    x = 1 / 0
except Exception as e:
    raise CustomException(e)