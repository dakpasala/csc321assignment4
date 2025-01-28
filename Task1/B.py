import hashlib

def compute_sha256(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

def flip_bit(binary_string, position):
    # flip the bit at the specified position
    flipped = list(binary_string)
    flipped[position] = '1' if binary_string[position] == '0' else '0'
    return ''.join(flipped)

def main():
    # define the original binary string (must be at least 8 bits for testing)
    original_binary = "01010101"
    # flip one bit at position 3
    modified_binary = flip_bit(original_binary, 3)
    
    print(f"Original Binary: {original_binary}")
    print(f"Modified Binary: {modified_binary}")

    # convert binary strings to ASCII strings for hashing
    original_ascii = ''.join(chr(int(original_binary[i:i+8], 2)) for i in range(0, len(original_binary), 8))
    modified_ascii = ''.join(chr(int(modified_binary[i:i+8], 2)) for i in range(0, len(modified_binary), 8))

    # compute SHA-256 hashes
    hash_original = compute_sha256(original_ascii)
    hash_modified = compute_sha256(modified_ascii)

    print(f"SHA-256 Hash (Original): {hash_original}")
    print(f"SHA-256 Hash (Modified): {hash_modified}")

    # compare the hashes
    print("\nComparing Digests:")
    print(f"Hamming Distance between Hashes: {sum(a != b for a, b in zip(hash_original, hash_modified))}")

if __name__ == "__main__":
    main()
