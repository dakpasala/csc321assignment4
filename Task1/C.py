import hashlib
import random
import string
import time

# function to truncate SHA-256 hash
def sha256_truncated(input_string, bits):
    full_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    binary_hash = bin(int(full_hash, 16))[2:].zfill(256)
    return binary_hash[:bits]

# function to generate random strings
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# this part of the code is very important because of how we need to generate various different strings
# to make sure we can check each possible combination

# function to find a collision using the Birthday Attack
def find_collision_birthday(bits):
    seen_hashes = {}  # dictionary to store truncated hashes and their inputs
    start_time = time.time()
    
    while True:
        candidate = generate_random_string()
        truncated_hash = sha256_truncated(candidate, bits)
        
        # check if this hash already exists in the dictionary
        if truncated_hash in seen_hashes:
            collision_time = time.time() - start_time
            return (candidate, seen_hashes[truncated_hash], collision_time)
        
        # this part of the code is very important because of how we won't be looking at the duplicates over and over again
        # from the previous methods a lot of them keep looking at the repeats
        
        # otherwise, store the hash and input
        seen_hashes[truncated_hash] = candidate

# main function to test multiple digest sizes
def main():
    for bits in range(8, 51, 2):  # Test for digest sizes 8, 10, 12, ..., 50
        print(f"Finding collision for {bits}-bit truncated hash...")
        m0, m1, time_taken = find_collision_birthday(bits)
        print(f"Collision found for {bits} bits:")
        print(f"  Input 1: {m0}")
        print(f"  Input 2: {m1}")
        print(f"  Time Taken: {time_taken:.2f} seconds\n")

if __name__ == "__main__":
    main()
