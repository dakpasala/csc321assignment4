import hashlib

def hash_input(input_string):
    # Encode the input string to bytes
    byte_input = input_string.encode('utf-8')
    # Create a SHA256 hash object
    hash_object = hashlib.sha256(byte_input)
    # Return the hexadecimal digest
    return hash_object.hexdigest()

def main():
    print("SHA-256 Hash Generator")
    print("Type 'exit' to stop the program.")
    while True:
        user_input = input("Enter the string to hash: ")
        if user_input.lower() == 'exit':
            break
        hash_result = hash_input(user_input)
        print(f"SHA-256 Digest (hex): {hash_result}\n")

if __name__ == "__main__":
    main()
