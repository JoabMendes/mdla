import time
from datetime import date, datetime, timedelta


def getNextDay(last_day):
    #Returns tomorrows timestamp at two times: 00:00 and 23:59
    last_day = datetime.utcfromtimestamp(last_day)
    tomorrow = last_day + timedelta(days=1)
    tomorrow_start = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0, 0)
    tomorrow_end = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 23, 59, 0, 0)
    return [tomorrow_start, tomorrow_end]


last_day = 1370054073

print "The day is:"
print datetime.utcfromtimestamp(last_day)

print "The next day is:"
print getNextDay(last_day)
