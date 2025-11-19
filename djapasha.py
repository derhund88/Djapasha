#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                      DJAPASHA v1.0                            ║
║            Django PBKDF2:SHA256 Hash Cracker                  ║
║                                                               ║
║  A fast and efficient tool to crack Django password hashes    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

import hashlib
import binascii
import sys
import argparse

def crack_pbkdf2_hash(hash_string, wordlist_file, verbose=False):
    """
    Crack a PBKDF2:SHA256 hash by testing passwords from a wordlist.
    
    Args:
        hash_string: The full hash string (e.g., pbkdf2:sha256:600000$salt$hash)
        wordlist_file: Path to wordlist file (one password per line)
        verbose: Show each password being tested
    """
    
    # Parse the hash
    parts = hash_string.split('$')
    if len(parts) != 3:
        print("Invalid hash format!")
        return
    
    algorithm_info = parts[0]  # pbkdf2:sha256:600000
    salt = parts[1]
    expected_hash = parts[2]
    
    # Extract iterations from algorithm info
    algo_parts = algorithm_info.split(':')
    iterations = int(algo_parts[2])
    
    print(f"[*] Algorithm: {algo_parts[0]}:{algo_parts[1]}")
    print(f"[*] Iterations: {iterations}")
    print(f"[*] Salt: {salt}")
    print(f"[*] Expected hash: {expected_hash}")
    print(f"[*] Starting crack...\n")
    
    count = 0
    try:
        with open(wordlist_file, 'r') as f:
            for line in f:
                password = line.strip()
                if not password:  # Skip empty lines
                    continue
                
                count += 1
                
                # PBKDF2 with SHA256
                hash_obj = hashlib.pbkdf2_hmac(
                    'sha256',
                    password.encode('utf-8'),
                    salt.encode('utf-8'),
                    iterations
                )
                
                # Convert to hex
                computed_hash = binascii.hexlify(hash_obj).decode('utf-8')
                
                # Show processed word and hash if verbose
                if verbose:
                    print(f"{password}={computed_hash}")
                elif count % 10000 == 0:
                    print(f"[*] Tested {count} passwords...")
                
                # Compare
                if computed_hash == expected_hash:
                    print(f"\n[+] PASSWORD FOUND: {password}")
                    print(f"[+] Hash: {computed_hash}")
                    print(f"[+] Total attempts: {count}")
                    return password
        
        print(f"\n[-] Password not found in wordlist. Tested {count} passwords.")
        return None
        
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_file}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='PBKDF2:SHA256 Hash Cracker',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python3 djapasha.py -w wordlist.txt
  python3 djapasha.py -w wordlist.txt -v
  python3 djapasha.py -w /path/to/wordlist.txt -hash "pbkdf2:sha256:600000$SALT$HASH" -v
        '''
    )
    
    parser.add_argument('-w', '--wordlist', 
                        default='wordlist.txt',
                        help='Path to wordlist file (default: wordlist.txt)')
    parser.add_argument('-hash', '--hash', 
                        default="pbkdf2:sha256:600000$AMtzteQIG7yAbZIa$0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133",
                        help='PBKDF2 hash to crack (default: admin@eighteen.htb hash)')
    parser.add_argument('-v', '--verbose', action='store_true', 
                        help='Show each password and its hash')
    
    args = parser.parse_args()
    
    result = crack_pbkdf2_hash(args.hash, args.wordlist, args.verbose)
    
    if result:
        print(f"\n[✓] Successfully cracked! Password is: '{result}'")
    else:
        print("\n[✗] Crack unsuccessful")
