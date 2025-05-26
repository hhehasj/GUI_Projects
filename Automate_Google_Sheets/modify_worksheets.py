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
section_id: int = 0


def main(data: dict[str: str, str: int]):
    row_id: int = 0
    col_id: int = 0
    starting_row: int = 0
    end_row: int = 0
    not_finish_entering: bool = True

    pattern = re.compile(r"^LG Leader:\s*$")
    while sheet.find(pattern) and not_finish_entering:
        row_id = sheet.find(pattern).row
        col_id = sheet.find(pattern).col
        starting_row = sheet.find(pattern).row
        end_row = sheet.find("Prayer Request/Other Concerns:").row

        for label, value in data.items():
            if sheet.cell(row_id, col_id).value == "Lessons Learned/Feedbacks:":
                row_id += 1

            if row_id == end_row:
                col_id += 2
                row_id = starting_row

            if label in ["Attendance", "Testimonies", "Discussion"]:

                row_id += 1
                sheet.update_cell(row_id, col_id, value)
                while True:
                    row_id += 1
                    next_value = sheet.cell(row_id, col_id).value

                    if next_value is not None:
                        break

            elif label in ["Time Started", "Time Ended"]:
                sheet.update_cell(row_id, col_id, value)
                row_id += 1

                if row_id == starting_row + 1:
                    not_finish_entering = False

            else:
                sheet.update_cell(row_id, col_id, f"{label}: {value}")
                row_id += 1


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


def right_side_empty(label: str):
    pattern = re.compile(r"^[^:]+:\s*$")
    matches = pattern.finditer(label)
    for match in matches:
        return bool(match)


main({
    "LG Leader": "Kuya Elisha",
    "Date": "May 15, 2025",
    "Offering": 100,
    "Attendance": "Alfred, Aaron, Cristof, EJ",
    "Lesson Title": "God is Good",
    "Testimonies": "testimony",
    "Discussion": "discussion",
    "Time Started": "7:00 PM",
    "Time Ended": "10:00 PM",
}
)
