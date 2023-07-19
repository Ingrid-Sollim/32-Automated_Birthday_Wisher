import smtplib
import datetime as dt
from random import choice
import pandas as pd
import os
import sys

#My email details
MY_EMAIL = "ingridsollim@gmail.com"
PASSWORD = "lumlwojdwiyqraqc"

#TODO 1: Create function to send email
def email_sender(message,email_receiver):
    global MY_EMAIL,PASSWORD
    #email_msg = f"{subj}\n\n{message}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email_receiver, msg=message)
    except:
        print("Connection fail")


#TODO 2: Read the birthday list file
birth_list = pd.read_csv("birthdays.csv",sep=",")

#Today's date
hoje=dt.datetime.now().date()
#print(hoje)

#Add date of birthday column
def create_actual_birthdat(row):
    return dt.datetime(hoje.year,row["month"],row["day"])
birth_list["actual_brithday"] = birth_list.apply(lambda row:create_actual_birthdat(row),axis=1)
birth_list["actual_brithday"] = birth_list["actual_brithday"].apply(dt.datetime.date)
#print(birth_list)

#TODO 3: Create the messages to send the email
#Function to read the message file and replace the Name for the person's name
def open_message_file(name):
    messages = os.listdir("letter_templates")
    #print(messages)
    with open(f"letter_templates/{choice(messages)}") as file:
        message = file.read()
        #file_into_list = contents.split("\n")
    message = message.replace("[NAME]",name)
    message = f"Subject:Happy Birthday\n\n{message}"
    #print(message)
    return message

#TODO 4: Check for the date to send an email
name_df = birth_list[birth_list["actual_brithday"]==hoje][["email","name"]]
#print(name_df)
if not name_df.empty:
    # TODO 5: Send email for every person that has birthday today
    # Dictionary with emails to send
    messages = {}
    for _, row in name_df.iterrows():
        messages[row["email"]] = open_message_file(row["name"])
    # print(messages)

    # Iterate over the dictionary to send the email
    for email, msg in messages.items():
        email_sender(msg, email)
        print("Email sent")
    
else:
    print("No birthday found")
    sys.exit()








