import datetime


class Date(object):
    def get_date(self):
        return '{day}-{month}-{year}'.format(day = datetime.date.today().day,
                                month = datetime.date.today().month,
                                year = datetime.date.today().year)

class Time(Date):
    def get_time(self):
        return '16:15:00'

df = Date()
print(df.get_date())

tm = Time()
print(tm.get_date())
print(tm.get_time())



