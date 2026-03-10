# functions module contains functions for handling product information and cost calculation.

from validations import name_validation, price_validation, quantity_validation

def product():
    """Collects product information from the user and returns it as a dictionary."""
    name = name_validation()
    price = price_validation()
    quantity = quantity_validation()
    
    return {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def calculate_cost(product):
    """Calculates the total cost of the product based on its price and quantity."""
    return product["price"] * product["quantity"]

