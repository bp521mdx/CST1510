a = 4
b = 5

while True:
    answer = int(input(f"what is {a} + {b}? "))
    if answer == a + b:
        print("Correct!")
        break
    else:
        print("Try Again.")