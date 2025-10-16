def calculate_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    quot_result = a / b

    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {diff_result}")
    print(f"{a} * {b} = {prod_result}")
    print(f"{a} / {b} = {quot_result:.3f}")


a = int(input())
b = int(input())

calculate_operations(a, b)

