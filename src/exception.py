import sys


def error_msg_detail(error):
    _, _, exc_tb = sys.exc_info() 
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_num = exc_tb.tb_lineno
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, line_num, str(error)
        )
        return error_message
    else:
        return str(error)


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_msg = error_message
    
    def __str__(self):
        return self.error_msg
    

try:
    x = 1 / 0
except Exception as e:
    formatted_error = error_msg_detail(e)
    
    raise CustomException(formatted_error)