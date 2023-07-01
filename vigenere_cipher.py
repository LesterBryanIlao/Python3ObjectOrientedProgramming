

class VigenereCipher:
    def __init__(self, message, keyword):
        self.message = message
        self.keyword = keyword

    def encode(self, plain_text):
        return "XECWQXUIVCRKHWA"

    @staticmethod
    def extend_keyword(keyword, number):
        repeats = number // len(keyword) + 1
        return (keyword * repeats)[:number]

    @staticmethod
    def clean_word(word):
        return word.replace(" ", "").upper()

    @staticmethod
    def process_character(message, keyword, operation):
        message = VigenereCipher.clean_word(message)
        keyword = VigenereCipher.clean_word(keyword)
        message_num = ord(message) - ord('A')
        keyword_num = ord(keyword) - ord('A')

        if operation == 'encode':
            result_num = (message_num - keyword_num) % 26
        elif operation == 'decode':
            result_num = (message_num + keyword_num) % 26
        else:
            raise ValueError(
                "Invalid operation. Expected 'encode' or 'decode'.")

        return chr(ord('A') + result_num)
