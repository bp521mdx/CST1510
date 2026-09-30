"""
RECORD CHECK  -  my version
===========================

Name  :bhavya parmar
Lane  :  AI
Date  :25-09-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


dataset_name =  input("Dataset_name")
rows_loaded = float(input("rows loaded:"))
rows_expected = float(input("rows expected:"))

difference = rows_expected - rows_loaded
percent_loaded = (rows_loaded / rows_expected) * 100

print()
print("=" * 34)
print(f"Record Check - {dataset_name} ")
print("=" * 34)

print(f"Rows loaded:   {rows_loaded:>10,.2f}")
print(f"Rows expected: {rows_expected:>10,.2f}")
print(f"Difference:    {difference:>10,.2f}")
print(f"Percent loaded: {percent_loaded:>10,.2f}%")

print("=" * 34)

