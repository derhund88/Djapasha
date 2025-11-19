╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                      DJAPASHA v1.0                            ║
║            Django PBKDF2:SHA256 Hash Cracker                  ║
║                                                               ║
║  A fast and efficient tool to crack Django password hashes    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

How to Use:

  python3 djapasha.py -w wordlist.txt
  python3 djapasha.py -w wordlist.txt -v
  python3 djapasha.py -w /path/to/wordlist.txt -hash "pbkdf2:sha256:600000$SALT$HASH" -v
