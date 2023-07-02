

def randomize_case(string):
    import random
    new_string = ""
    for char in string:
        if char != " ":
            if random.randint(0, 1) == 0:
                new_string += char.upper()
            else:
                new_string += char.lower()
    return new_string


class VigenereCipher:
    ENCODE = 'encode'
    DECODE = 'decode'

    def __init__(self, keyword):
        self.keyword = keyword

    def cipher(self, message, operation):
        message = self.clean_word(message)
        keyword = self.clean_word(self.keyword)
        keyword = self.trim_or_extend_word(keyword, len(message))

        if len(message) < len(keyword):
            raise ValueError("Keyword cannot be longer than message.")
        return "".join(self.process_character(m, k, operation) for m, k in zip(message, keyword))

    def trim_or_extend_word(self, keyword, number):

        if number > len(keyword):
            repeats = number // len(keyword) + 1
            return (keyword * repeats)[:number]
        elif number < len(keyword):
            return keyword[:number]
        else:
            return keyword

    def clean_word(self, word):
        word = word.replace(" ", "").upper()
        return "".join(char for char in word if char.isalpha())

    def process_character(self, message_char, keyword_char, operation):
        message = self.clean_word(message_char)
        keyword = self.clean_word(keyword_char)
        message_num = ord(message) - ord('A')
        keyword_num = ord(keyword) - ord('A')

        if operation == self.ENCODE:
            result_num = (message_num + keyword_num) % 26
        elif operation == self.DECODE:
            result_num = (message_num - keyword_num) % 26
        else:
            raise ValueError(
                "Invalid operation. Expected 'encode' or 'decode'.")

        return chr(ord('A') + result_num)
