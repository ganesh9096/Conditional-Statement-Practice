'''Write a program to check salary bonus based on years of service.'''

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 5:
    bonus = salary * 0.10
else:
    bonus = 0

print("Bonus =", bonus)
print("Total Salary =", salary + bonus)