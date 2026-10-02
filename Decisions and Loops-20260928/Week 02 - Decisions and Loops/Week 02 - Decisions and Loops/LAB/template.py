"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

dataset_name = input("Dataset_name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

difference = rows_expected - rows_loaded
percent_loaded = (rows_loaded / rows_expected) * 100

if percent_loaded < 100:
    status = "UNDER Limit"
elif percent_loaded > 100:
    status = "OVER Limit"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {status}")
print("=" * 34)

print(f"Rows loaded:    {rows_loaded:>10,.2f}")
print(f"Rows expected:  {rows_expected:>10,.2f}")
print(f"Difference:     {difference:>10,.2f}")
print(f"Percent loaded: {percent_loaded:>10,.2f}%")
print(f"Status:         {status:>10}")

print("=" * 34)


