
def to_binary(n):
    return format(n & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def add_binary(a, b):
    result = a + b
    binary_result = to_binary(result)
    overflow = (a >= 0 and b >= 0 and signed_value(binary_result) < 0) or \
               (a < 0 and b < 0 and signed_value(binary_result) >= 0)

    print("Operand 1:", to_binary(a))
    print("Operand 2:", to_binary(b))
    print("Binary result:", binary_result)
    print("Decimal result:", signed_value(binary_result))
    print("Overflow:", overflow)


def subtract_binary(a, b):
    result = a - b
    binary_result = to_binary(result)
    overflow = (a >= 0 and b < 0 and signed_value(binary_result) < 0) or \
               (a < 0 and b >= 0 and signed_value(binary_result) >= 0)

    print("Operand 1:", to_binary(a))
    print("Operand 2:", to_binary(-b))
    print("Binary result:", binary_result)
    print("Decimal result:", signed_value(binary_result))
    print("Overflow:", overflow)


print("a) +46 + (+29)")
add_binary(46, 29)

print("\nb) (-48) - (-23)")
subtract_binary(-48, -23)
