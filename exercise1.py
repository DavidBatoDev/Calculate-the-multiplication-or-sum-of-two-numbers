# define a function that has a parameter of two numbers that checks the ff:
def calculate_product_or_sum(num1, num2):
    product_result = num1 * num2
    if int(product_result) <= 1000:
        # if the two numbers product is equal or lower than 1000, return product of two number
        return product_result
    else:
        # else return their sum
        return num1 + num2