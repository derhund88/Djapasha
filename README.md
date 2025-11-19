# DJAPASHA - Django PBKDF2:SHA256 Hash Cracker
```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                      DJAPASHA v1.0                            ║
║            Django PBKDF2:SHA256 Hash Cracker                  ║
║                                                               ║
║  A fast and efficient tool to crack Django password hashes    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

## Description
A fast and efficient tool to crack Django PBKDF2:SHA256 password hashes using wordlist attacks.

## Installation
```bash
git clone <your-repo-url>
cd djapasha
```

## Usage
```bash
# Default usage (uses default hash and wordlist.txt)
python3 djapasha.py

# With custom wordlist
python3 djapasha.py -w /path/to/wordlist.txt

# Verbose mode (shows each word's hash)
python3 djapasha.py -w abc.txt -v

# With custom hash and verbose
python3 djapasha.py -w /path/to/wordlist.txt -hash "pbkdf2:sha256:600000$SALT$HASH" -v
```

## Examples
```bash
asu=cd6c589543d48bac11d12aacc467c6f3bc22a7665888a793b804864bd3965afc
abe=1d69711a7156e867d46755d3ad8fb02bbe243b8570f146d466e2058f9db3217c
anu=63ecfdec3c1e38103db3024d6a165acc706865944aaf0c234413874073c37be9
```

## Features
- Fast PBKDF2:SHA256 hash cracking
- Verbose mode to see computed hashes
- Custom hash and wordlist support
- Default configuration for quick testing

## Requirements
- Python 3.x

## License
MIT
