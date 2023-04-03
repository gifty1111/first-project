def multiplication_sum(num1, num2):
    product = num1*num2
    if product <=1000:
        return product
    else:
       return  num1 + num2
result = multiplication_sum(20, 30)
print("the result is ", result)

result = multiplication_sum(40, 50)
print("the result is ", result)


