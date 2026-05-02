"""
Caesar Cipher — encrypt and decrypt text using a shift value.
Usage: python caesar_cipher.py
"""


def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    Args:
        text:  The input message.
        shift: Number of positions to shift (1–25).
        mode:  'encrypt' or 'decrypt'.

    Returns:
        The transformed text.
    """
    if mode == "decrypt":
        shift = (26 - shift % 26) % 26

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)          # preserve spaces, digits, punctuation
    return "".join(result)


def print_cipher_map(shift: int) -> None:
    """Display a visual mapping of the alphabet for the given shift."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted  = alphabet[shift:] + alphabet[:shift]
    print("\n  Plain:  ", " ".join(alphabet))
    print("  Cipher: ", " ".join(shifted))


def get_shift() -> int:
    while True:
        try:
            shift = int(input("Enter shift value (1–25): "))
            if 1 <= shift <= 25:
                return shift
            print("  Please enter a number between 1 and 25.")
        except ValueError:
            print("  Invalid input — please enter an integer.")


def get_mode() -> str:
    while True:
        mode = input("Mode — (E)ncrypt or (D)ecrypt? ").strip().upper()
        if mode in ("E", "ENCRYPT"):
            return "encrypt"
        if mode in ("D", "DECRYPT"):
            return "decrypt"
        print("  Please enter E or D.")


def main() -> None:
    print("=" * 50)
    print("          CAESAR CIPHER")
    print("=" * 50)

    while True:
        shift = get_shift()
        mode  = get_mode()

        print_cipher_map(shift)

        message = input("\nEnter your message: ")
        output  = caesar_cipher(message, shift, mode)

        label = "Encrypted" if mode == "encrypt" else "Decrypted"
        print(f"\n  {label}: {output}\n")
        print("-" * 50)

        again = input("Go again? (Y/N): ").strip().upper()
        if again != "Y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
