
def rotate_right(binary, positions):
    print("Original number:", binary)
    current = binary

    for i in range(positions):
        last_bit = current[-1]
        current = last_bit + current[:-1]
        print("Step", i + 1, ":", current)

    print("Final result:", current)


def rotate_right_carry(binary, positions, carry):
    print("Original number:", binary)
    print("Initial Carry Flag:", carry)
    current = binary

    for i in range(positions):
        new_carry = int(current[-1])
        current = str(carry) + current[:-1]
        carry = new_carry

        print("Step", i + 1, ":", current,
              "Carry Flag:", carry)

    print("Final result:", current)
    print("Final Carry Flag:", carry)


print("a) ROR")
rotate_right("11010101", 3)

print("\nb) RCR")
rotate_right_carry("11010101", 3, 0)
