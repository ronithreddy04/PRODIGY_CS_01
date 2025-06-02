def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    mode = input("Enter E to encrypt or D to decrypt: ").upper()
    if mode not in ['E', 'D']:
        print("Invalid option.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if mode == 'E':
        print("Encrypted:", caesar_encrypt(message, shift))
    else:
        print("Decrypted:", caesar_decrypt(message, shift))

if __name__ == "__main__":
    main()
