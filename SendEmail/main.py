import smtplib

my_email = "gtest4py@gmail.com"
password = "wwhq svkw vjac qpgq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ytest4py@outlook.com", msg="Subject:Hello\n\nThis is the body of my email")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2003, month=10, day=16)
# print(date_of_birth)