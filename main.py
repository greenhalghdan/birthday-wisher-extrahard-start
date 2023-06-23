##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as td
import random
import smtplib

FROM_EMAIL_ADDRESS = "HappyBirthday@suffolkmotorcyclespares.co.uk"
EMAIL_ADDRESS = "*****@****.co.uk"
PASSWORD = "*****"
# 1. Update the birthdays.csv
NewBirthdayDict = {
    "name": "Amy",
    "email": "amyleighton92@hotmail.com",
    "year": 1990,
    "month": 6,
    "day": 23
}

df = pd.DataFrame(NewBirthdayDict, index=[0])
df.to_csv("birthdays.csv", mode="a", index=False, header=False)


# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
now = td.datetime.now()
month = now.month
day = now.day
letters = []
for index, birthday in birthdays.iterrows():

    if birthday["month"] == month and birthday["day"] == day:
# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
        with open("letter_templates/letter_1.txt") as letter:
            letters.append(letter.read())
        with open("letter_templates/letter_2.txt") as letter:
            letters.append(letter.read())
        with open("letter_templates/letter_3.txt") as letter:
            letters.append(letter.read())
        chosen_letter = random.choice(letters)
        chosen_letter = chosen_letter.replace("[NAME]", birthday["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL_ADDRESS, to_addrs=birthday["email"],
                                msg=f"subject:Happy Birthday\n\n{chosen_letter}")


