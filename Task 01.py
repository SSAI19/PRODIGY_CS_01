def encrypt_caesar(text, shift_value):
    encrypted_result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_result.append(chr((ord(char) - base + shift_value) % 26 + base))
        else:
            encrypted_result.append(char)
    return ''.join(encrypted_result)

def decrypt_caesar(text, shift_value):
    return encrypt_caesar(text, -shift_value)

def user_interface():
    print("Welcome to Caesar Cipher!")
    operation = input("Encrypt (E) or Decrypt (D): ").strip().upper()
    message = input("Enter the message: ")
    shift_value = int(input("Enter shift value: "))

    if operation == 'E':
        print(f"Encrypted: {encrypt_caesar(message, shift_value)}")
    elif operation == 'D':
        print(f"Decrypted: {decrypt_caesar(message, shift_value)}")
    else:
        print("Invalid option. Please enter E or D.")

if __name__ == "__main__":
    user_interface()
