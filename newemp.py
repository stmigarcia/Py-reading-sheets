#!/usr/bin/env python3

# The goal of this is to further automate the process of bringing new employees into Blinker.  Once a new employee
# signs offer, HR will will out a Goole Form that will auto-populate a Google Sheet.  That data will then be used to 
# create a new Gmail account within the Blinker Domain via Gadmin and place them in the Blinekr orginization within 
# Google.


import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import gspread 
import pandas as pd
from pandas import read_csv, DataFrame
import json
import sys
import os

# Providing credentials for New Employee On-Boarding Checklist in gsheets
''' googtteste sheets '''
app_credential_file = os.environ.get('GOOGLE_API_CRED_FILE', 'client_secret.json')
app_credential_file_contents = os.environ.get('GOOGLE_API_CRED_CONTENTS', None)
app_sheet_id = os.environ.get('GOOGLE_SHEETS_ID', '1DlBQ8VOk0YwdTNFukgplLfetIZQaNwuIv1cFbMpJgfg')

# Accessing the New Employee On-Boarding Checklist sheet
''' es sheets connection '''
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(app_credential_file, scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key(app_sheet_id)

# Reading all the data from the New Employee On-Boarding Checklist sheet
worksheet = sheet.worksheet('Sheet2').get_all_values()
dataframe = pd.DataFrame(worksheet)
df = dataframe
#print(df)

# This will orginize the date vertically per row.  row1=Zack Piper, row2=Angela Lindow
# Need to change first number to show individual row from sheet
# The '0-19' (all temes that can be input from Google form) can be changed to isolate information. If you only 
# wanted the new person's name then you would replace '0-19' with '2'
user_info = df.iloc[2,0:7]

for user in user_info:
    print(user)

# How can I get the previous lines to be automatic? Meaning, how can I get this script to 
# run and read/run on the newest row when it is populated.  When HR fills the out the form, the 
# script only reads the new-new. Also, need to make it read relivant data and make that data easily
# identifiable. 