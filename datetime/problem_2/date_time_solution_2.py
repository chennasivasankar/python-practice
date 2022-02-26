def datetime_solution(date_string: str):

    from datetime import datetime

    date_object = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    output_1 = str(date_object.day) + "-" + str(date_object.month) + "-" + str(date_object.year) + " " + str(
        date_object.time())
    output_2 = str(date_object.month) + "-" + str(date_object.day) + "-" + str(date_object.year) + " " + str(
        date_object.time())
    print(output_1)
    print(output_2)
