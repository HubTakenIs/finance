import calendar, datetime
from db import get_db_conn

def silly_func():
    out = []
    c = calendar.Calendar()
    for i in range(1,13):
        dates = c.itermonthdates(2026,i)
        for date in dates:
            out.append(date.strftime("%d/%m/%Y"))
    return out

def list_dates_for_month(year, month):
    c = calendar.Calendar()
    dates = c.itermonthdates(year,month)
    out = []
    for date in dates:
        out.append(date.strftime("%d/%m/%Y"))
    return out

def list_days_for_month(year, month):
    c = calendar.Calendar()
    days = c.itermonthdays(year,month)
    out = []
    return days

def main():
   list_of_dates = list_dates_for_month(2026, calendar.JANUARY)
   print(list_of_dates)
   print("days?")
   list_of_days = list_days_for_month(2026, calendar.JANUARY)
   print(list(list_of_days))
   c = calendar.Calendar()
   jan_weeks = c.monthdayscalendar(2026, calendar.JANUARY)
   print("jan")
   print(jan_weeks)
   

if __name__ == "__main__":
    main()
