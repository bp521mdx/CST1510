name = input("What is your name? ")
age_1 = 20
age_2 = 30
age_3 = 40
new_person = input("Enter a new person's age: ")
average_age = (age_1 + age_2 + age_3 + int(new_person)) / 4
print(f'Hello, ' + name + '! The average age is: ' + str(average_age))