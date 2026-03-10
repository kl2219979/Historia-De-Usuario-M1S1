def name_validation():
    """Validates the name input from the user. The name should only contain alphabetic characters."""
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Invalid name. Please enter a valid name.")
        return name_validation()
    return name

def price_validation():
    """Validates the price input from the user. The price should be a positive number."""
    price = input("Enter the price: ")
    try:
        price = float(price)
        if price <= 0:
            print("Invalid price. Please enter a positive number.")
            return price_validation()
        return price
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return price_validation()

def quantity_validation():
    """Validates the quantity input from the user. The quantity should be a positive integer."""
    quantity = input("Enter the quantity: ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Invalid quantity. Please enter a positive integer.")
            return quantity_validation()
        return quantity
    except ValueError:
        print("Invalid quantity. Please enter a valid integer.")
        return quantity_validation()