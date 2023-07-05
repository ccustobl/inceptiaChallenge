# -------------------------------- 
# Author: Custo Blanch, Christian 
# Project: Inceptia Job Application
# --------------------------------

# Define variables
_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

# --------------------------------

# Define validate_discount_code method
def validate_discount_code(discount_code):
    """Returns True if the discount code is valid, False otherwise."""

    for code in _AVAILABLE_DISCOUNT_CODES:

        # Reset the difference counter and the list of different characters
        diff_count = 0
        diff_chars = []

        # Compare characters between the mentioned code and the available discount code
        for char in discount_code:
            if char not in code and char not in diff_chars:
                diff_count += 1
                diff_chars.append(char)
        for char in code:
            if char not in discount_code and char not in diff_chars:
                diff_count += 1
                diff_chars.append(char)

        # Print the results for each comparison
        #print(f"DS Code: {discount_code}")
        #print(f"Code: {code}")
        #print(f"Characters: {diff_chars}")
        #print(f"Number: {diff_count}")
        
        # Verify if the difference is less than three characters
        if diff_count < 3:            
            return True # The difference with a code is less than three characters
        
    return False # No code is valid 

# --------------------------------

# Test
def test_validate_discount_code():
    test_cases = [
        {"discount_code": "primavera2021", "expected_result": True},
        {"discount_code": "Primavera2021", "expected_result": True},
        {"discount_code": "pPrimavera2021", "expected_result": True},
        {"discount_code": "VERANO2021", "expected_result": False},
        {"discount_code": "Navidad2021", "expected_result": True},
        {"discount_code": "heladoFroz3n", "expected_result": True},
        {"discount_code": "HELADO_FROZEN", "expected_result": False},
        {"discount_code": "Invierno2021", "expected_result": False},
    ]

    for i, test_case in enumerate(test_cases):
        discount_code = test_case["discount_code"]
        expected_result = test_case["expected_result"]
        result = validate_discount_code(discount_code)
        status = "PASSED" if result == expected_result else "FAILED"
        print(f"Test case {i+1}: {status}")
        print(f"Discount code: {discount_code}")
        print(f"Expected result: {expected_result}")
        print(f"Actual result: {result}")
        print("---------------------")

# Run the testing code
test_validate_discount_code()
