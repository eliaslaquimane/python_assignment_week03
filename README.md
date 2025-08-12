# Discount Calculator 
A simple Python script to calculate a final price after applying a discount, with a rule that the discount must be at least 20%.
If the discount is less than 20%, the original price will be returned without any change.

Features
Takes a product price and desired discount percentage as user input.

Applies the discount only if it is greater than or equal to 20%.

Returns the original price if the discount is too low.

Simple and beginner-friendly code.

Usage
1. Clone or Download
bash
```bash
git clone https://github.com/eliaslaquimane/python_assignment_week03.git
cd python_assignment_week03
``` 
2. Run the Script
Make sure you have Python installed (version 3.6 or higher).
```bash
python discount_calculator.py
Example
Input:
```vbnet
Price value to apply discount: 100
How much discont do you want?: 25
Output:
```plaintext
75.0
# Discount Calculator
A simple Python script to calculate a final price after applying a discount, with a rule that the discount must be at least 20%.
If the discount is less than 20%, the original price will be returned without any change.

Usage
1. Clone or Download
bash
Copy
git clone https://github.com/eliaslaquimane/python_assignment_week03.git
cd python_assignment_week03
2. Run the Script
Make sure you have Python installed (version 3.6 or higher).

bash
Copy
Edit
python discount_calculator.py
Example
Input:

vbnet
Copy
Edit
Price value to apply discount: 100
How much discont do you want?: 25
Output:

Copy
Edit
75.0
Code Overview
python
Copy
Edit
def calculate_discount(price: float, discount_percent: float):
    """Verify if the discount_percent >= 20, otherwise return original price"""
    if discount_percent >= 20:
        discount = (price * (discount_percent / 100))
        final_price = price - discount
        return final_price
    return price

# User input
price_value = float(input("Price value to apply discount: "))
discount_value = float(input("How much discont do you want?: "))

print(calculate_discount(price_value, discount_value))