# -*- coding: utf-8 -*-
"""
Simple command to demonstrate email send via smtplib
"""

import smtplib


gmail_user = input("Enter sender email: ")
gmail_password = input("Enter password: ")

email_from = gmail_user
email_to = input("Enter receiver email: ")
email_subject = 'Test Email !'
email_body = 'Test Email Content. \nContent on new line.'

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    server_ssl.login(gmail_user, gmail_password)
    # ...send emails
    
    server_ssl.sendmail(email_from, email_to, email_body)
    server_ssl.close()
    
    print('Email Sent!')
except:
    print('Something went wrong...')