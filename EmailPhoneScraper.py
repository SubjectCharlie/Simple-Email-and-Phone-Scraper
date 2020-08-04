# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:10:51 2020

@author: SubjectCharlie
This is a simple Email and Phone Number scraper that will extract 
from whatever is currently copied onto the clipboard. This was made 
for learning purposes, guided by the Automate the Boring with Python
by Al Sweigart. 
"""

import re, pyperclip

#Regex for phone numbers

phoneNumberRegex = re.compile('''
(((\d\d\d) | (\(\d\d\d\)))?  #area code
(-)                          #first dash
(\d\d\d)                     #first 3 numbers
(-)                          #second dash
(\d\d\d\d))                  #last 4 numbers''', re.VERBOSE)

#Regex for emails

emailRegex = re.compile('''
[a-zA-Z0-9._+]+              #email name
@                            #@ symbol
[a-zA-Z0-9._+]+              #domain name''', re.VERBOSE)

#Gets the text from clipboard

inputText = pyperclip.paste()

#Extracts the phone numbers and emails from the text

extractedPhoneNumbers = phoneNumberRegex.findall(inputText)
extractedEmails = emailRegex.findall(inputText)

fullPhoneNumbers = []
for phoneNumbers in extractedPhoneNumbers:
    fullPhoneNumbers.append(phoneNumbers[0])

#Copies the extracted info to the clipboard

results = '\n'.join(fullPhoneNumbers) + '\n\n\n\n' + '\n'.join(extractedEmails)
pyperclip.copy(results)
