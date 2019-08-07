import frequencyanalysis


def main():

    """
    Demonstration of the frequencyanalysis module.
    """

    print("----------------------")
    print("| codedrome.com      |")
    print("| Frequency Analysis |")
    print("----------------------\n")

    try:
        frequencyanalysis.create_decryption_dictionary("the_sign_of_four_plaintext.txt",
                                                       "encrypted.txt",
                                                       "decryption_dict.json")
    except Exception as e:
        print(e)

    try:
        frequencyanalysis.decrypt_file("encrypted.txt",
                                       "decrypted.txt",
                                       "decryption_dict.json")
    except Exception as e:
        print(e)


main()
