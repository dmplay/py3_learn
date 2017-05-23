# !/usr/bin/python
# -*- coding: UTF-8 -*-
import pyperclip, re
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r'''(
    (\w+) # separator
    (@) # first 3 digits
    (\w+) # separator
    \.com
    )''', re.VERBOSE)
# TODO: Find matches in clipboard text.
text=pyperclip.paste()
print(text)
list =emailRegex.findall(text)
# TODO: Copy results to the clipboard.
pyperclip.copy(','.join([x[0] for x in list]))
print(pyperclip.paste())