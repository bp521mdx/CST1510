"""
RECORD CHECK  -  my version
===========================

Name  : Bhavya Parmar
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """Calculate the diff and percent for values in record"""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "WITHIN LIMIT"

    return difference, percent, status



def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print(f"\nRecord: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")

records = [
    {"label": "Record A", "value": 120, "limit": 100},
    {"label": "Record B", "value": 80, "limit": 100},
    {"label": "Record C", "value": 150, "limit": 120}
]

over_limit_count = 0

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"\nTotal records OVER LIMIT: {over_limit_count}")



