import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(credentials)

sheet_id = "1M-x50F-A7iQqjbrmDYSI2uDrRgh6L91G0FgZTgi4y0E"
sheet = client.open_by_key(sheet_id)
# -----------------------------------------------------------------------------------------------------------------------------------------------
