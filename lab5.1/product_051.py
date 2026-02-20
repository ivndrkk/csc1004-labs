import sys

def removeZeros(num_str):
    result = ""
    for i in range(len(num_str)):
        if num_str[i] != '0':
            result += num_str[i]
    return result if result else "0"

def product(num_str_without_zeros):
    num_list = list(map(int, num_str_without_zeros))
    product_result = 1
    for num in num_list:
        product_result *= num
    return product_result

for line in sys.stdin:
    line = line.strip()
    product_int = product(removeZeros(line))
    while product_int >= 10:
        product_int = product(removeZeros(str(product_int)))
    print(product_int)