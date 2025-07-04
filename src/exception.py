import sys
from src.logger import logging

def error_message_detail(error, detail: sys):
    tb = detail.exc_info()[2]
    return f"Error in [{tb.tb_frame.f_code.co_filename}] at line [{tb.tb_lineno}]: {error}"

class CustomException(Exception):
    def __init__(self, error, detail: sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, detail)

        # 🔥 Log the error message immediately
        logging.error(self.error_message)
    
    def __str__(self):
        return self.error_message