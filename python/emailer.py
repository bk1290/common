# -*- coding: utf-8 -*-
"""
Simple command to demonstrate email send via smtplib
Assumes Gmail account and password are stored in a separate json file
https://docs.python.org/3/library/email.examples.html#email-examples
"""

import smtplib
import json
from string import Template
from email.parser import BytesParser
from email.parser import Parser
from email.policy import default

# Set variables
sender_account_cfg="E:/script_configs/robo_account.json"
email_filepath="E:/script_files/emailer_template.txt"
attachment_fp="E:/script_files/text_attachment_test.txt"

# Gmail account information is stored in a JSON file
with open(sender_account_cfg) as json_data_file:
    data = json.load(json_data_file)
gmail_user = data['email_address']
gmail_password = data['email_password']

# Email template file stored in a .TXT file
with open(email_filepath, 'rb') as email_file:
    parsed_file=BytesParser(policy=default).parse(email_file)

# perform text replacements on the email file contents
email_template = Template(parsed_file.as_string())
email_str = email_template.safe_substitute(
        SENDER = gmail_user,
        VAR1 = 'Value1',
        VAR2 = 'Value2'
        # add as many variables as needed...
        )


print(parsed_file.get_body())

final_email = Parser(policy=default).parsestr(email_str)

final_email.add_header('Content-Disposition', 'attachment', filename=attachment_fp)


try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()  
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.send_message(final_email)
    server_ssl.close()
    print('Email Sent!')
except:
    print('Something went wrong...')
    