from vigenere_cipher import VigenereCipher, combine_character

cipher = VigenereCipher("TRAIN")
# print(combine_character("E", "X"))
plain_num = ord("X") - ord('A')
keyword_num = ord("E") - ord('A')
result = chr(ord('A') + (plain_num + keyword_num) % 26)

print(plain_num, keyword_num, result)
print(ord('A') + (plain_num + keyword_num) % 26)
print(65+27 % 26)
