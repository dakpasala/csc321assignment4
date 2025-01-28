import bcrypt
import time
from concurrent.futures import ProcessPoolExecutor
import os
from nltk.corpus import words
import nltk
import ssl
from tqdm import tqdm

# Disable SSL verification for NLTK
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK words if not already present
nltk.download('words', quiet=True)

# Function to hash a word using bcrypt
def hash_and_compare(word, salt, target_hash):
    hashed_word = bcrypt.hashpw(word.encode('utf-8'), salt)
    if hashed_word == target_hash:
        return word
    return None

# Function to process a chunk of the wordlist
def process_chunk(wordlist_chunk, salt, target_hash):
    for word in wordlist_chunk:
        result = hash_and_compare(word, salt, target_hash)
        if result:
            return result
    return None

# Function to crack a single user's password using subprocesses
def crack_password(user_entry, wordlist, num_workers):
    user, bcrypt_hash = user_entry.split(':')[0], user_entry.split(':')[1]
    salt = bcrypt_hash[:29].encode('utf-8')
    target_hash = bcrypt_hash.encode('utf-8')

    print(f"\nCracking password for user: {user}")

    # Divide wordlist into chunks
    chunk_size = max(5000, len(wordlist) // num_workers)
    wordlist_chunks = [wordlist[i:i + chunk_size] for i in range(0, len(wordlist), chunk_size)]

    start_time = time.time()

    # Use subprocesses to process each chunk in parallel
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(process_chunk, chunk, salt, target_hash) for chunk in wordlist_chunks]

        for future in tqdm(futures, desc=f"Testing passwords for {user}"):
            result = future.result()
            if result:
                end_time = time.time()
                print(f"\nPassword found for {user}: {result}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return result

    print(f"Password not found for {user}.")
    return None

# Main function to crack all passwords
def crack_passwords(shadow_entries, wordlist, num_workers):
    results = {}
    for entry in shadow_entries:
        result = crack_password(entry, wordlist, num_workers)
        if result:
            user = entry.split(':')[0]
            results[user] = result
    return results

if __name__ == "__main__":
    # Shadow entries from shadow.pdf
    shadow_entries = [
        "Bifur:$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
        "Bofur:$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
        "Durin:$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
    ]

    # Generate wordlist from NLTK
    print("Generating wordlist from NLTK...")
    wordlist = [word.lower() for word in words.words() if 6 <= len(word) <= 10]

    # Number of parallel processes
    num_workers = max(os.cpu_count() - 1, 1)  # Leave one core free
    print(f"Using {num_workers} CPU cores")

    # Crack the passwords
    cracked_passwords = crack_passwords(shadow_entries, wordlist, num_workers)

    print("\nCracked Passwords:")
    for user, password in cracked_passwords.items():
        print(f"{user}: {password}")
