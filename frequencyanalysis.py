from operator import itemgetter
import json


def create_decryption_dictionary(plaintext_filepath, encrypted_filepath, dictionary_filepath):

    """
    Create an estimated mapping between encrypted letters and
    plaintext letters by comparing the frequencies in the
    plaintext and encrypted text.
    The dictionary is then saved as a JSON file.
    """

    sample_plaintext = _readfile(plaintext_filepath)
    encrypted_text = _readfile(encrypted_filepath)

    sample_plaintext_frequencies = _count_letter_frequencies(sample_plaintext)
    encrypted_text_frequencies = _count_letter_frequencies(encrypted_text)

    decryption_dict = {}
    for i in range(0, 26):
        decryption_dict[encrypted_text_frequencies[i][0]] = sample_plaintext_frequencies[i][0].lower()

    f = open(dictionary_filepath, "w")
    json.dump(decryption_dict, f)
    f.close()


def decrypt_file(encrypted_filepath, decrypted_filepath, dictionary_filepath):

    """
    Use the dictionary to decrypt the encrypted file
    and save the result.
    """

    encrypted_text = _readfile(encrypted_filepath)

    f = open(dictionary_filepath, "r")
    decryption_dict = json.load(f)
    f.close()

    decrypted_list = []

    for letter in encrypted_text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            decrypted_list.append(decryption_dict[letter])

    decrypted_text = "".join(decrypted_list)

    f = open(decrypted_filepath, "w")
    f.write(decrypted_text)
    f.close()


def _count_letter_frequencies(text):

    """
    Create a dictionary of letters A-Z and count the frequency
    of each in the supplied text.
    Lower case letters are converted to upper case.
    All other characters are ignored.
    The returned data structure is a list as we need to sort it by frequency.
    """

    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    return sorted_by_frequency


def _readfile(path):

    f = open(path, "r")
    text = f.read()
    f.close()
    return text
