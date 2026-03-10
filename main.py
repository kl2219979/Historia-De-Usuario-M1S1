# main 
from functions import product, calculate_cost

def main():
    """Main function to run the product information collection and cost calculation."""
    print("Welcome to the Product Cost Calculator!")
    
    product_info = product()
    total_cost = calculate_cost(product_info)
    
    print(f"Product: {product_info['name']} | Price: {product_info['price']} | Quantity: {product_info['quantity']} | Total Cost: {total_cost}")

if __name__ == "__main__":
    main()
