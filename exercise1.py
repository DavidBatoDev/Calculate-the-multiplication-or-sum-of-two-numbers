# define a function that has a parameter of two numbers that checks the ff:
def calculate_product_or_sum(num1, num2):
    product_result = num1 * num2
    if int(product_result) <= 1000:
        # if the two numbers product is equal or lower than 1000, return product of two number
        return product_result
    else:
        # else return their sum
        return num1 + num2
    
test1 = calculate_product_or_sum(20, 30)
print(f'The result is {test1}') # Output: The result is 600
test2 = calculate_product_or_sum(30, 40)
print(f'The result is {test2}') # Output: The result is 70