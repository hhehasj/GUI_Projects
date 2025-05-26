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

sheet = google_sheet.get_worksheet(3)


def main(data: dict[str: str, str: int]):
    row_id: int = 0
    col_id: int = 0
    starting_row: int = 0
    not_finish_entering: bool = True

    def attendance_testimonies_discussion():
        nonlocal row_id, col_id
        row_id += 1
        sheet.update_cell(row_id, col_id, value)
        while True:
            row_id += 1
            next_value = sheet.cell(row_id, col_id).value

            if label == "Discussion" and next_value is not None:
                col_id += 2
                row_id = starting_row

            if next_value is not None:
                break

    pattern = re.compile(r"^LG Leader:\s*$")
    while sheet.find(pattern) and not_finish_entering:
        row_id = sheet.find(pattern).row
        col_id = sheet.find(pattern).col
        starting_row = sheet.find(pattern).row

        for label, value in data.items():
            if sheet.cell(row_id, col_id).value == "Lessons Learned/Feedbacks:":
                row_id += 1

            if label in ["Attendance", "Testimonies", "Discussion"]:
                attendance_testimonies_discussion()

            elif label in ["Time Started", "Time Ended"]:
                sheet.update_cell(row_id, col_id, value)
                row_id += 1

                if row_id == starting_row + 1:
                    not_finish_entering = False

            else:
                sheet.update_cell(row_id, col_id, f"{label}: {value}")
                row_id += 1
