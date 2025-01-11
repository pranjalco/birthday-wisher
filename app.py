import datetime as dt
import pandas
import random
import smtplib

"""
# Project 22: Birthday Wisher

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 03 Jan 2025

## Description
This project automates the process of sending birthday wishes to individuals listed in a CSV file. The program reads the `birthday.csv` file to identify people whose birthdays match the current date. If a match is found, it selects a random letter template from the `letter_templates` folder, replaces the placeholder `[NAME]` with the person's name, and sends an email to their address using Python's `smtplib` module.

## How to Use
1. Ensure the required modules (`datetime`, `pandas`, `random`, `smtplib`) are installed using pip install cmd.
2. Place a properly formatted `birthday.csv` file in the project folder. The file should contain the following columns:
   - `name`
   - `email`
   - `year`
   - `month`
   - `day`
3. Add three letter templates to the `letter_templates` folder with the placeholder `[NAME]` where the recipient's name should appear.
4. Configure the SMTP settings in the `app.py` file to use your email credentials.

## Level
- **Level**: Intermediate
- **Skills**: File handling, CSV manipulation, Email automation, Random module usage
- **Domain**: Automation, Email Communication

## Features
- Reads and processes a `birthday.csv` file to check for birthdays matching the current date.
- Randomly selects a letter template from a folder of predefined templates.
- Dynamically personalizes the letter by replacing placeholders with the recipient's name.
- Sends emails using Python's `smtplib` module.
- Includes a modular structure for easy modification and enhancement.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/birthday-wisher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd birthday-wisher
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

## File Structure
```
project-folder/
|
├── app.py                # Main script to run the program
├── birthday.csv          # CSV file containing birthday data
├── letter_templates/     # Folder containing letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   ├── letter_3.txt
├── README.md             # Project documentation
```
---
**Created by Pranjal Sarnaik**  
*© 2025. All rights reserved.*
"""

MY_EMAIL = "pranjal@gmail.com"
MY_PASSWORD = "msdflegxspklezpe"

with open("birthdays.csv") as file:
    birth_info = file.read()

today = dt.datetime.now()
month = today.month
day = today.day
# birthday = f"0{month},0{day}"

birthday = "01,03"

if birthday in birth_info:
    df = pandas.read_csv("birthdays.csv")
    birth_info_dict = df.to_dict(orient="records")

    for d in birth_info_dict:
        if month == d['month'] and day == d['day']:
            name = d['name']
            to_email = d["email"]

    if name:
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        send_letter = random.choice(letters)

        with open(f"./letter_templates/{send_letter}") as file:
            letter_info = file.read()
            updated_letter_info = letter_info.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"subject:Happy Birthday {name}\n\n{updated_letter_info}"
            )
