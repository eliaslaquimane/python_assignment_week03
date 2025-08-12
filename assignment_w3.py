def calculate_discount(price: float, discount_percent: float):
    
    """Verify if the discount_percent >= 20 if not return original price"""
    
    if discount_percent >= 20:
        # applying the formula of discount and final price
        discount = (price * (discount_percent / 100)) 
        final_price = price - discount
        
        return final_price
    # original price return if the if is not True
    return price

# allow user enter value price and discount
price_value = float(input("Price value to apply discount: "))
discount_value = float(input("How much discont do you want?: "))

# printing the returned value
print(calculate_discount(price_value, discount_value))