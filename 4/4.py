pc1_key = int("11110000110011001010101011110101010101100110011110001111", 2)

# Split the key into C0 and D0
c0 = (pc1_key >> 28) & 0xFFFFFFF
d0 = pc1_key & 0xFFFFFFF

# Initialize C0 and D0
c_round, d_round = c0, d0


def next_round(c_current, d_current, round_number):
    # Define the number of left shifts for this round
    if round_number in [1, 2, 9, 16]:
        shift_count = 1
    else:
        shift_count = 2

    # Perform circular left shifts on C and D
    c_next = ((c_current << shift_count) | (c_current >> (28 - shift_count))) & 0xFFFFFFF
    d_next = ((d_current << shift_count) | (d_current >> (28 - shift_count))) & 0xFFFFFFF

    return c_next, d_next


permutation_table =[14, 17, 11, 24, 1,  5,
                    3,  28, 15, 6,  21, 10,
                    23, 19, 12, 4,  26, 8,
                    16, 7,  27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]

for round_number in range(1, 17):
    print(f"Round {round_number}:")
    print(f"C{round_number}:", bin(c_round)[2:].zfill(28))
    print(f"D{round_number}:", bin(d_round)[2:].zfill(28))

    temp = (c_round << 28) | d_round
    temp_str = ""
    
    for index in range(48):
        temp_str += bin(temp)[2:].zfill(56)[permutation_table[index] - 1]

    k_round = int(temp_str, 2)

    print(f"K{round_number}:", bin(k_round)[2:].zfill(48))

    print()

    # Update c_round and d_round for the next round
    c_round, d_round = next_round(c_round, d_round, round_number)