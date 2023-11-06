import sys
import logging
from src.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    error_message="error occured in the python script name[{0}] line no[{1}] and error message[{2}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_messags=error_message_details(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_messags
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info('Divide by zero')
        raise CustomException(e,sys)