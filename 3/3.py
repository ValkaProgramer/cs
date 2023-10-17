alphabet = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Î', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'Ș', 'T', 'Ț', 'U', 'V', 'W', 'X', 'Y', 'Z']

keyword = input("Enter the keyword longer than 6 characters\n").upper()
if len(keyword) < 7:
    print('Invalid keyword length')
    exit()
else:
    for char in keyword:
        if char not in alphabet:
            print('Invalid characters in the keyword')
            exit()

choice = input("Choose:\n1. Encryption\n2. Decryption\n")
if choice not in ['1', '2']:
    print('Invalid choice option')
    exit()
else:
    choice = int(choice)

input_m = input(f"Enter the {'message' if choice == 1 else 'cryptogram'}:\n").upper()

key_list = [alphabet.index(char) for char in keyword]

output_m = ''

match choice:
    case 1:
        for char in input_m:
            output_m += alphabet[(alphabet.index(char) + key_list[len(output_m) % len(key_list)]) % len(alphabet)]
    case 2:
        for char in input_m:
            output_m += alphabet[(alphabet.index(char) - key_list[len(output_m) % len(key_list)]) % len(alphabet)]

print(f"Received {'message' if choice == 2 else 'cryptogram'}: {output_m}")