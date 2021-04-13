def D(a, b):
    if a > b:
        while b != 0:
            z = a % b
            a = b
            b = z
        return a
    else:
        while a != 0:
            z = b % a
            b = a
            a = z
        return b

print(D(125, 25))
print(D(25, 125))