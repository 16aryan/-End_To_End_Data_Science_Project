import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from logger import logging         # ✅ Correct — both files are in the same folder

class CustomException(Exception):
    def __init__(self, error, detail=sys):
        tb = detail.exc_info()[2]
        msg = f"Error in [{tb.tb_frame.f_code.co_filename}] at line [{tb.tb_lineno}]: {error}"
        logging.error(msg)
        super().__init__(msg)