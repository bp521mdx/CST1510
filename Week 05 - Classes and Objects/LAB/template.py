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

# ==================================================================== RECORDS CLASS
class Record:
    # Class-level attribute keeping a running total of over-limit instances
    over_limit_count = 0 

    def __init__(self, label, value, limit):
        """Initialize a Record instance with a label, current value, and maximum limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)
        
        # Check status upon creation to keep the class-level tally accurate
        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Return OK, WARNING (90%+), or OVER LIMIT (100%+) based on capacity."""
        percentage = (self.value / self.limit) * 100
        
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"



def load_records(path):
    """Read comma-separated record data from a file and return a list of Record objects."""
    loaded_records = []
    
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                # Unpack the three comma-separated values
                label, value, limit = line.split(",")
                # Instantiate a new Record and add it to our list
                new_record = Record(label, value, limit)
                loaded_records.append(new_record)
                
    return loaded_records

records = load_records("Week 05 - Classes and Objects/LAB/records_sample.txt")



for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    
    # Core report lines
    print(f"  Value:   {record.value}")
    print(f"  Limit:   {record.limit}")
    print(f"  Status:  {record.status()}")
    
    print("=" * 34)


print(f"\nTotal records OVER LIMIT across the system: {Record.over_limit_count}")
