import smtplib
import datetime as dt
import random

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
quote = random.choice(quote_list)

date = dt.datetime.now()
current_day_of_week = date.weekday()
if current_day_of_week == 6:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="email@gmail.com", password="")
        connection.sendmail(from_addr="email@gmail.com", to_addrs="email2@gmail.com",
                            msg=f"Subject: Quote of the week\n\n{quote}")
