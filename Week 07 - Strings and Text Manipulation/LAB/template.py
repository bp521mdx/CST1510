"""
RECORD CHECK  -  my version
===========================

Name  : bhavya
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




def parse_line(raw_line):
    """Clean and convert one server record into a dictionary."""

    raw_line = raw_line.strip()

   
    hostname, rest = raw_line.split(",", 1)

    data = {
        "hostname": hostname.strip().lower()
    }

    for item in rest.split(","):
        key, value = item.split("=")

        key = key.strip().lower()
        value = float(value.strip())

        data[key] = value

    return data



def status_of(record):
    """Check whether server usage is normal or over the limit."""

    percentage = record["used"] / record["total"] * 100

    if percentage >= 100:
        return "OVER LIMIT"

    elif percentage >= 90:
        return "WARNING"

    else:
        return "OK"

raw_records = []

with open(r"C:\Users\Bhavya\CST1510\Week 07 - Strings and Text Manipulation\LAB\messy_lines.txt") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


total_records = 0
flagged_records = 0

for raw_record in raw_records:

    record = parse_line(raw_record)

    status = status_of(record)

    print(record, "-", status)

    total_records += 1

    if status != "OK":
        flagged_records += 1



print("\n----- SUMMARY -----")

print("Total records:", total_records)
print("Flagged records:", flagged_records)
