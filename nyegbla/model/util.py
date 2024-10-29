from time import time, strftime, localtime
import uuid

def get_to_timedate()-> str:
    '''Compute and return today's date and what time this function is called'''
    time_formatter = '%Y/%m/%d %H:%M:%S'
    current_loccal_time = time()
    timedate = strftime(time_formatter, localtime(current_loccal_time))
    return timedate


def generate_uuid():
    return str(uuid.uuid4())[:23]
    