from google.oauth2.service_account import Credentials
import gspread_formatting as gmt
import gspread as gs
import re

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentails = Credentials.from_service_account_file(filename="credentials.json", scopes=scopes)
client = gs.authorize(credentails)

google_sheet_id = "1M-x50F-A7iQqjbrmDYSI2uDrRgh6L91G0FgZTgi4y0E"
google_sheet = client.open_by_key(google_sheet_id)
# -------------------------------------------------------------------------------------------------------------------------------------------

sheet = google_sheet.get_worksheet(1)
section_id: int = 0


def main(data):
    for label, values in data.items():
        if label in ["Attendance", "Testimonies", "Discussion"]:
            input_blocks = sheet.findall(re.compile(pattern=f"^{label}:"))
            update_blocks(input_blocks, values)

            # print("Multiple_lines: ", input_blocks)

        else:
            one_liners = sheet.findall(re.compile(pattern=f"^{label}:"))
            # print("One_liners: ", one_liners)


def update_blocks(title_cells: list[str], content: str):
    for title_cell in title_cells:
        # The grey areas
        block_row = title_cell.row + 1
        block_col = title_cell.col

        block_content = sheet.cell(row=block_row, col=block_col).value
        if block_content is not None:
            print("Contains")

        else:
            sheet.update_cell(value=content, row=block_row, col=block_col)



def update_one_liners(single_line_inputs: list[str]):
    ...