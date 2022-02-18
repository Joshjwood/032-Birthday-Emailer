import datetime as dt
import smtplib
import pandas
import random
import time
from privates import *

################ Email ##################

my_email = my_email
password = password

my_main_email = my_main_email

now = dt.datetime.now()
print(now)

day = now.day
month = now.month

print(f"{month}/{day}")

with open("birthdays_sheet.csv") as birthday_data:
    birthdays = pandas.read_csv(birthday_data)
    birthdays = birthdays.to_dict()


    for index in range(0, len(birthdays["name"])):

        #letters = (letter_1, letter_2, letter_3)
        #print(f'{birthdays["month"]} + {birthdays["name"]}')
        #print(f'{birthdays["month"][index]}/{birthdays["day"][index]} {birthdays["name"][index]}')

        if int(month) == int(birthdays["month"][index]) and int(day) == int(birthdays["day"][index]):
            print("Someones birthday")
            file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
            #file_path = f"./letter_templates/letter_1.txt"
            with open(file_path, "r") as letter:
                print("opened letter")
                contents = letter.read()
                contents = contents.replace("[NAME]", birthdays["name"][index])
                print(f'It\'s {birthdays["name"][index]}\'s birthday. They were born {birthdays["day"][index]}/{birthdays["month"][index]}/{birthdays["year"][index]}')
                print("Trying to send to recipient")
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=birthdays["email"][index], msg=f"Subject:It's your birthday!\n\n{contents}")
                time.sleep(10)
                print("Trying to send notification to Josh")
                connection.sendmail(from_addr=my_email, to_addrs=my_main_email, msg=f'Subject:It\'s {birthdays["name"][index]}\'s birthday!\n\nGive them a shout.')
                connection.close()
                print(f'Email sent to {birthdays["name"][index]}')
        else:
            continue