import calendar, datetime
from db import get_db_conn

def silly_func():
    c = calendar.Calendar()
    for i in range(1,13):

        dates = c.itermonthdates(2026,i)
        for date in dates:
            print(date.strftime("%d/%m/%Y"))

def main():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchone())

    
    conn.close()

if __name__ == "__main__":
    main()
