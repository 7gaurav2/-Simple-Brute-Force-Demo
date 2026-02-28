import hashlib
import time

def hash_password(plain_text_password):
    """
    Hash a plain text password using SHA-256.
    In real systems, passwords are stored as hashes, not plain text.
    """
    return hashlib.sha256(plain_text_password.encode()).hexdigest()


def load_wordlist(wordlist_file_path):
    """
    Load a list of candidate passwords from a text file.
    Each line in the file is treated as one candidate password.
    """
    try:
        with open(wordlist_file_path, 'r') as wordlist_file:
            candidate_passwords = [line.strip() for line in wordlist_file]
        return candidate_passwords

    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_file_path}' not found.")
        return []


def run_brute_force(target_hash, candidate_passwords):
    """
    Try each candidate password by hashing it and comparing
    it to the target hash. Returns the matched password or None.
    """
    total_attempts = 0

    print("\nStarting brute force attack...\n")

    for candidate_password in candidate_passwords:
        total_attempts += 1
        candidate_hash = hash_password(candidate_password)

        print(f"  Trying: {candidate_password:<20} -> {candidate_hash[:20]}...")

        # Compare hashes instead of plain text passwords
        if candidate_hash == target_hash:
            return candidate_password, total_attempts

    return None, total_attempts


def run_brute_force_demo():
    """
    Main demo function: simulates a stored hashed password
    and attempts to crack it using a wordlist.
    """
    print("=" * 50)
    print("     Simple Brute Force Demo (Local Lab Only)")
    print("=" * 50)

    # Simulate a stored hashed password (like in a real database)
    secret_password      = "check@15697"
    stored_password_hash = hash_password(secret_password)

    print(f"\nTarget Hash (SHA-256): {stored_password_hash}\n")

    # Load wordlist from a file or use a built-in demo list
    use_demo_list = input("Use built-in demo wordlist? (yes/no): ").strip().lower()

    if use_demo_list == "yes":
        # Small built-in wordlist for demonstration
        candidate_passwords = [
            "password", "123456", "letmein", "qwerty",
            "monkey", "admin", "admin123", "pass1234",
            "welcome", "sunshine", "iloveyou", "dragon" , "check@15697"
        ]
    else:
        wordlist_path       = input("Enter path to your wordlist file: ").strip()
        candidate_passwords = load_wordlist(wordlist_path)

        if not candidate_passwords:
            print("No passwords loaded. Exiting.")
            return

    start_time = time.time()

    matched_password, total_attempts = run_brute_force(stored_password_hash, candidate_passwords)

    elapsed_time = time.time() - start_time

    print("\n" + "=" * 50)

    if matched_password:
        print(f"  ✅ Password FOUND    : {matched_password}")
    else:
        print("  ❌ Password NOT found in wordlist.")

    print(f"  Total Attempts      : {total_attempts}")
    print(f"  Time Taken          : {elapsed_time:.4f} seconds")
    print("=" * 50)


if __name__ == "__main__":    run_brute_force_demo()