"""  
This program takes a ciphertext[file encrypted] using Encryptor.py [RSA Algorithm], 
converts it into plaintext and displays it on the command line keeping the ciphertext as is.
"""

import getpass
import sys
import os

def filename():
    """  
    It checks whether the file provided as argument exists in the directory.
    It also checks whether a filename was provided as an argument.

    Returns :
    filename (str) : Filename only if the given command line argument is given and exists in the directory. 
    """
    file_list = os.listdir()

    if len(sys.argv)> 1:
        for filename in file_list:
            if sys.argv[1] == filename:
                return filename
        return None
    else:
        return None

filename = filename()

if filename != None:
    try:
        decryptor = getpass.getpass(prompt="[PASSWORD won't display what you're writing] Enter 'd' or 'decryptor' : ")
        N = int(input("Enter 'N' from 'modN' : "))

        with open("new.txt", "r") as fr:
            sentence = fr.read()

            # Putting all values from the txt file as individual list indices.
            split_sentence = sentence.split(" ")

            # FORMULA : (CT ** decryptor) % N. Here CT i.e. CipherText are the list elements of "split_sentence".
            decrypt_pow = [int(numd) ** int(decryptor) for numd in split_sentence]
            decrypt = [int(numd) % N for numd in decrypt_pow]

            # Convert decrypted ASCII numbers to their character equivalent. 
            decrypt_to_words = [chr(i) for i in decrypt]

            # Concatenating all list elements separated by " " and printing them to the terminal.
            sep = ""
            decrypt_to_words_display = sep.join(decrypt_to_words)
            print(decrypt_to_words_display)

    except ValueError:
        print("Enter correct answer!")

else:
    print(f"File doesn't exist in this directory. Pass valid filename as an argument in the execution command. \nFor example : python {os.path.basename(sys.argv[0])} filename.txt")