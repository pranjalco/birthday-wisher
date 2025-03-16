# Birthday Wisher
An automated birthday wisher that reads a CSV file, picks a random letter template, personalizes it, and sends an email to the recipient using SMTP. 

## Author
Pranjal Sarnaik

## Features
- Reads `birthday.csv` to find matching birthdays.  
- Randomly selects a letter template.  
- Replaces placeholders with recipient names.  
- Sends emails using `smtplib`.  
- Modular design for easy customization.  

## Level
Intermediate

## Tech Stack
Python | File Handling | CSV Manipulation | Email Automation | Random Module | SMTP

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/birthday-wisher.git

2. Ensure the required modules (`datetime`, `pandas`, `random`, `smtplib`) are installed using pip install cmd.

3. Run(Also install required libraries):
    ```bash  
   python app.py

## File Structure:
project-folder/
|
├── app.py                # Main script to run the program
├── birthday.csv          # CSV file containing birthday data
├── letter_templates/     # Folder containing letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   ├── letter_3.txt
├── README.md             # Project documentation

**Created by Pranjal Sarnaik**  
*Released under the MIT License*