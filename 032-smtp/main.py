import datetime as dt
import random as r
import pandas as pd
from smtplib import SMTP

# Read the CSV file into a DataFrame
df = pd.read_csv('birthdays.csv')

# Strip whitespace from the 'dob' column
df['dob'] = df['dob'].str.strip()

# Ensure the 'dob' column is in datetime format
df['dob'] = pd.to_datetime(df['dob'], format='%m/%d/%Y')

# Extract the month and day from the 'dob' column
df['month'] = df['dob'].dt.month
df['day'] = df['dob'].dt.day

# Get today's date
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# Find birthdays that match today's date
matched_birthdays = df[(df['month'] == today_month) & (df['day'] == today_day)]

# Send quote to each matched birthday
for index, row in matched_birthdays.iterrows():
    name = row['name']
    email = row['email']

    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = r.choice(all_quotes)

        my_email = ''
        my_pass = ''

        with open('template.txt') as template:
            content = template.read()
            content = content.replace('[NAME]', name)
            content = content.replace('[QUOTE]', quote)

            with SMTP(host='smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row.email,
                    msg=content
                )
