import smtplib
import datetime as dt
import random

email = "" #your e-mail
password = ""#your password
with open("quotes.txt") as file:
    quotes = file.readlines()

dt = dt.datetime.now()
day_of_week = dt.weekday()

if day_of_week == 0:
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="",
                            msg=f"Subject:Quote of Monday\n\n{quote}")
