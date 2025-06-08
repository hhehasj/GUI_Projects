from google.oauth2.service_account import Credentials
import gspread as gs
import re

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentails = Credentials.from_service_account_file(filename="credentials.json", scopes=scopes)
client = gs.authorize(credentails)

google_sheet_id = "1M-x50F-A7iQqjbrmDYSI2uDrRgh6L91G0FgZTgi4y0E"
google_sheet = client.open_by_key(google_sheet_id)
# -------------------------------------------------------------------------------------------------------------------------------------------


def which_sheet(date: str):
    quarters_months_pairs: dict[int: list[str]] = {
        1: ["January", "February", "March"],
        2: ["April", "May", "June"],
        3: ["July", "August", "September"],
        4: ["October", "November", "December"],
    }
    month = date.split(" ", maxsplit=2)[0]  # Gets only the month name

    for key, quarters in quarters_months_pairs.items():
        if month in quarters:
            return google_sheet.get_worksheet(key)  # returns the sheet that the data gets edited in


def main(data: dict[str: str, str: int]):
    row_id: int = 0
    col_id: int = 0
    starting_row: int = 0
    not_finish_editing: bool = True  # To stop the code when label == "Time Ended: "
    sheet = which_sheet(data["Date"])

    def attendance_testimonies_discussion():
        nonlocal row_id, col_id

        row_id += 1
        sheet.update_cell(row_id, col_id, value)

        # To skip all the blank cells of the gray areas
        while True:
            row_id += 1
            next_value = sheet.cell(row_id, col_id).value

            if label == "Discussion" and next_value is not None:
                col_id += 2
                row_id = starting_row

            if next_value is not None:  # rows after the most top-left corner always returns None
                break

    pattern = re.compile(r"^LG Leader:\s*$")
    while sheet.find(pattern) and not_finish_editing:
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
                    not_finish_editing = False

            else:
                sheet.update_cell(row_id, col_id, f"{label}: {value}")
                row_id += 1
