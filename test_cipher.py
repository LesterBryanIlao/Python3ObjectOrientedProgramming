import random
from vigenere_cipher import randomize_case, VigenereCipher


def test_randomize_case():
    random.seed(42)  # Set the seed for reproducible results
    assert randomize_case("Hello, World!") != "HELlo, WorlD!"
    assert randomize_case("Python is awesome") != "PyThOn is aWEsoME"
    assert randomize_case("") == ""


def test_vigenere_cipher():
    cipher = VigenereCipher("KEYWORD")

    # Test encode operation
    assert cipher.cipher("HELLO", VigenereCipher.ENCODE) == "RIJHC"
    assert cipher.cipher("WORLD", VigenereCipher.ENCODE) == "GSPHR"

    # Test decode operation
    assert cipher.cipher("RIJHC", VigenereCipher.DECODE) == "HELLO"
    assert cipher.cipher("GSPHR", VigenereCipher.DECODE) == "WORLD"

    # Test invalid operation
    try:
        cipher.cipher("MESSAGE", "invalid")
        assert False, "Expected ValueError for invalid operation"
    except ValueError:
        assert True


def test_vigenere_cipher_trim_or_extend_word():
    cipher = VigenereCipher("KEYWORD")

    # Test trimming
    assert cipher.trim_or_extend_word("KEYWORD", 3) == "KEY"
    assert cipher.trim_or_extend_word("LONGKEYWORD", 5) == "LONGK"

    # Test extending
    assert cipher.trim_or_extend_word("KEY", 7) == "KEYKEYK"
    assert cipher.trim_or_extend_word("WORD", 8) == "WORDWORD"

    # Test same length
    assert cipher.trim_or_extend_word("SAME", 4) == "SAME"


def test_vigenere_cipher_clean_word():
    cipher = VigenereCipher("KEYWORD")

    assert cipher.clean_word("Hello, World!") == "HELLOWORLD"
    assert cipher.clean_word("Python is awesome") == "PYTHONISAWESOME"
    assert cipher.clean_word("") == ""


def test_vigenere_cipher_process_character():
    cipher = VigenereCipher("KEYWORD")

    # Test encode operation
    assert cipher.process_character("H", "K", VigenereCipher.ENCODE) == "R"
    assert cipher.process_character("E", "E", VigenereCipher.ENCODE) == "I"

    # Test decode operation
    assert cipher.process_character("R", "K", VigenereCipher.DECODE) == "H"
    assert cipher.process_character("I", "E", VigenereCipher.DECODE) == "E"


# Run the tests
if __name__ == "__main__":
    test_randomize_case()
    test_vigenere_cipher()
    test_vigenere_cipher_trim_or_extend_word()
    test_vigenere_cipher_clean_word()
    test_vigenere_cipher_process_character()
