from datetime import datetime


def return_current_time():
    return datetime.utcnow().strftime("%Y/%m/%d, %H:%M")
