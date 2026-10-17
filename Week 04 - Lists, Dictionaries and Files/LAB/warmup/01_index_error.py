# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]
try:
   result = (labels[3])
except IndexError:
   print("index out of range. recheck index")
else:
   print("index is valid", result)