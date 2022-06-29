from operator import mod


def extract_digits(n):
    digits = []
    r = 0
    while n != 0:
        r = n%10
        n = n//10
        digits.append(r)
    return digits

def power_tower(arr):
    # print(arr)
    product = arr[0]
    for d in arr[1:]:
        product = pow(d, product)
    # print(product)
    if len(str(product)) > 1:
        power_tower(extract_digits(product))
    else:
        return product

if __name__=="__main__":
    print(power_tower(extract_digits(28)))