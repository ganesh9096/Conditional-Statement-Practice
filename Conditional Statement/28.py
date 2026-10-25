'''Write a program to calculate discounts based on total shopping amount.'''
total_shopping_amount = float(input("Enter the total shopping amount: "))

if total_shopping_amount >= 1000:
    discount = 0.2 * total_shopping_amount
    print(f"Discount applied: ${discount:.2f}")
else:
    print("No discount applied.")