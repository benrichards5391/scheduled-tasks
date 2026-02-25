# necessary imports
import datetime as dt
import pandas as pd
import random
import os
import smtplib

# define variables for email
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# data manipulation
data = pd.read_csv('birthdays.csv') # read data from pandas
df = data.to_dict(orient='records') # convert data to a dictionary...orient='records' for formatting

# get the current time from datetime module
now = dt.datetime.now() # today
month = now.month # current month
day = now.day # current day

# convert different birthday letter templates into a list that can later randomly choose from
path = "./letter_templates"
dir_list = os.listdir(path)

for i in range(len(df)):
    if df[i]['month'] == month and df[i]['day'] == day:
        random_letter_file = random.choice(dir_list) # randomly choose letter template
        with open('./letter_templates/' + random_letter_file) as file: # make sure to include parent directory
            letter = file.read()
            new_letter = letter.replace("[NAME]", df[i]['name']) # replace with the person's name
            # establish a new connection for sending emails using SMTP
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=df[i]['email'],
                msg=f"Subject:Happy Birthday!!!\n\n{new_letter}"
            )







