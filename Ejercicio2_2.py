# -------------------------------- 
# Author: Custo Blanch, Christian 
# Project: Inceptia Job Application
# --------------------------------

# Import the requests library
import pandas as pd

# --------------------------------

# Define DataFrame
_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity":[3,10,0,5]})

# --------------------------------

# Define is_product_available method
def is_product_available(product_name, quantity):
    """ Returns True if the product is available in the DataFrame and the available quantity is enough, False otherwise."""

    # Set the maximum number of tries
    max_tries = 5

    # Search for the product in the DataFrame
    product = _PRODUCT_DF.loc[_PRODUCT_DF["product_name"] == product_name]

    # Check if the product was found    
    tries = 0
    while product.empty:
        tries += 1
        if tries > max_tries:
            print("Maximum number of tries reached.")
            return False # The product was not found and the maximum number of tries was reached
        print("Product not found, please try again.")
        product_name = input("Enter the product name: ")
        product = _PRODUCT_DF.loc[_PRODUCT_DF["product_name"] == product_name]

    # Retrieve the available quantity for the product
    available_quantity = product["quantity"].values[0]

    # Check if the available quantity is enough
    tries = 0
    while quantity > available_quantity:
        tries += 1
        if tries > max_tries:
            print("Maximum number of tries reached.")
            return False # The available quantity is not enough and the maximum number of tries was reached
        print("Not enough quantity, the quantity available is: ", available_quantity)
        quantity = int(input("Enter the desired quantity: "))        

    return True, product_name

# --------------------------------

# Test
product_name = input("Enter the product name: ")
quantity = int(input("Enter the desired quantity: "))
availability, product_name = is_product_available(product_name, quantity)
print(f"Product '{product_name}' is available: {availability}")
