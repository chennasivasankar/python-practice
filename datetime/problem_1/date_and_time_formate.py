def date_and_time(date_string: str):
    from datetime import datetime

    date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print("year:", date_object.year)
    print("month:", date_object.month)
    print("day:", date_object.day)
    print("time:", date_object.time())
    print("date and time:", date_string)
