import calendar, datetime

def main():
    c = calendar.Calendar()
    for i in range(1,13):

        dates = c.itermonthdates(2026,i)
        for date in dates:
            print(date.strftime("%d/%m/%Y"))


if __name__ == "__main__":
    main()
