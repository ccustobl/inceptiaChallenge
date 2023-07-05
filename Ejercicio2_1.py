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

    # Search for the product in the DataFrame
    product = _PRODUCT_DF.loc[_PRODUCT_DF["product_name"] == product_name]

    # Check if the product was found
    if not product.empty:

        # Retrieve the available quantity for the product
        available_quantity = product["quantity"].values[0]
        
        # Check if the available quantity is enough
        if available_quantity >= quantity:
            return True # The product is available and the available quantity is enough
            
    return False # The product was not found or the available quantity is not enough

# --------------------------------

# Test
product_name = "Chocolate"
quantity = 2
availability = is_product_available(product_name, quantity)
print(f"Product '{product_name}' is available: {availability}")
