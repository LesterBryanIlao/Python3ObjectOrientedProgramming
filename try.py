from vigenere_cipher import VigenereCipher, randomize_case

cipher = VigenereCipher("KEYWORD")
encoded = cipher.cipher(randomize_case(
    "WORLD"), VigenereCipher.ENCODE)
decoded = cipher.cipher(encoded, VigenereCipher.DECODE)

print(encoded)
print(decoded)
