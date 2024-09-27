import gspread
from google.oauth2.service_account import Credentials

'''
https://docs.gspread.org/en/v6.0.0/user-guide.html#creating-a-spreadsheet
'''


scopes = ['https://www.googleapis.com/auth/spreadsheets']
crdentials = Credentials.from_service_account_file('service-account-credentials.json', scopes=scopes)
client = gspread.authorize(crdentials)

SPREADSHEET_ID = '1lfT1lDwcEGYZUqjuz4XMufk5pQ1WruzMnnKjro9Mnbo'

sheet = client.open_by_key(SPREADSHEET_ID)

values_list = sheet.sheet1.row_values(1)
print(values_list)