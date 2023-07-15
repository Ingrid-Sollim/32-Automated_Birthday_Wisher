import smtplib
import datetime as dt
from random import choice
#My email details
MY_EMAIL = "xxxxxxx@gmail.com"
PASSWORD = "xxxxxxxx"

#TODO 1: Create function to send email
def email_sender(subj,message,email_receiver):
    global MY_EMAIL,PASSWORD
    email_msg = f"{subj}\n\n{message}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email_receiver, msg=email_msg)
    except:
        print("Connection fail")


# hj = dt.datetime.now()
# ano = hj.year
# semana = hj.weekday()
# print(semana)
#
# date_of_birth=dt.datetime(year=1994,month=3,day=7).date()
# print(date_of_birth)
# print(date_of_birth.weekday())

#This application will look into an specific day of week then we are going to email a motivational quote
#It's going to check if the day of week matches today's day of week, then is going to send a random motivational quote

#TODO 2: Read quotes text file
with open("quotes.txt") as file:
    contents = file.read()
    #print(contents)
    file_into_list = contents.split("\n")
    #print(file_into_list)

#TODO 3: Message to be send
todays_quote = choice(file_into_list)
print(todays_quote)
send_to = "xxxxxx@gmail.com"
mail_subject = "Subject: Motivational Quote of the Day"

#TODO 4: Condition to check if today is the day to send a message
hj = dt.datetime.now().weekday()
#print(hj)
if hj == 5:
    email_sender(mail_subject, todays_quote, send_to)
else:
    print("We dont send email today")
