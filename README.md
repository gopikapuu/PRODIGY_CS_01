# Caesar Cipher 🔐

A clean, interactive Python implementation of the classic **Caesar Cipher** — one of the oldest and simplest encryption techniques in history. Supports both encryption and decryption with any shift value from 1 to 25.

---

## What is the Caesar Cipher?

The Caesar Cipher shifts every letter in a message by a fixed number of positions in the alphabet. For example, with a shift of 3:

```
Plain:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

So `Hello` → `Khoor` with shift 3, and decrypting `Khoor` with shift 3 gives back `Hello`.

---

## Features

- Encrypt any message with a custom shift value (1–25)
- Decrypt any Caesar-encrypted message
- Preserves spaces, digits, and punctuation unchanged
- Preserves original letter casing (upper/lowercase)
- Displays a live alphabet cipher map for the chosen shift
- Interactive CLI with loop — encrypt/decrypt multiple messages in one session
- Clean reusable `caesar_cipher()` function for use as a module

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies — uses only the Python standard library

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/caesar-cipher.git

# Navigate into the project folder
cd caesar-cipher
```

### Run the Program

```bash
python caesar_cipher.py
```

---

## Usage

### Interactive CLI

```
==================================================
          CAESAR CIPHER
==================================================
Enter shift value (1–25): 3
Mode — (E)ncrypt or (D)ecrypt? E

  Plain:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  Cipher:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

Enter your message: Hello, World!

  Encrypted: Khoor, Zruog!

--------------------------------------------------
Go again? (Y/N): Y

Enter shift value (1–25): 3
Mode — (E)ncrypt or (D)ecrypt? D

Enter your message: Khoor, Zruog!

  Decrypted: Hello, World!
```

### Use as a Module

You can import `caesar_cipher` directly into your own Python scripts:

```python
from caesar_cipher import caesar_cipher

# Encrypt
encrypted = caesar_cipher("Hello, World!", shift=3, mode="encrypt")
print(encrypted)  # → Khoor, Zruog!

# Decrypt
decrypted = caesar_cipher("Khoor, Zruog!", shift=3, mode="decrypt")
print(decrypted)  # → Hello, World!
```

---

## How It Works

The core logic shifts each alphabetic character by the shift amount using modular arithmetic:

```
encrypted_char = (char_index + shift) % 26
decrypted_char = (char_index + (26 - shift)) % 26
```

This ensures the shift wraps around the alphabet (e.g. `X` + 3 = `A`). Non-alphabetic characters (spaces, numbers, punctuation) pass through unchanged.

---

## Project Structure

```
caesar-cipher/
├── caesar_cipher.py   # Main program — run this
└── README.md          # Project documentation
```

---

## Limitations

The Caesar Cipher is a **classical/educational cipher** and is **not secure** for real-world use:

- Only 25 possible keys — trivially broken by brute force
- Vulnerable to frequency analysis
- Use modern encryption (AES, RSA) for any actual security needs

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Author

Built as part of a Python programming exercises series.
