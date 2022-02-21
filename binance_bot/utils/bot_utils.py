import datetime
import time


def convert_time_from_unix(time_unix):
    return datetime.datetime.fromtimestamp(time_unix // 1000)


def convert_time_to_unix(*args):
    """example of args - tuple = (2021,1,1,1,1,1)"""
    date_time = datetime.datetime(args[0], args[1], args[2], args[3], args[4], args[5])
    unix_time = int(time.mktime(date_time.timetuple())) * 1000
    return unix_time
