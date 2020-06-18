"""  
This program takes a plaintext file and ecrypts it using the RSA Algorithm.
It permanently modifies the plaintext contents to ciphertext.
"""

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
    encryptor = int(input("Enter 'e' or 'encryptor' : "))
    N = int(input("Enter 'N' from 'modN' : "))

    with open(filename, "r") as fr:
        sentence = fr.read()
        with open(filename, "w") as fw:
            # Convert alphabets to their ASCII equivalents.
            ascii_version = [ord(number) for number in sentence]

            # FORMULA : (PT ** encryptor) % N, Here PT i.e. PlainText are the list elements of ascii_version.
            encrypt_pow = [int(nume) ** encryptor for nume in ascii_version]
            encrypt = [int(nume) % N for nume in encrypt_pow]

            # Convert "encrypt" from 'int' to 'str' using map().
            # Since, map() returns a map object, list() is used to convert it into list.
            encrypt_str = list(map(str, encrypt))

            # Concatenating all list elements separated by " " and writing them back to the txt file.
            sep = " "
            fw.write(sep.join(encrypt_str))
else:
    print(f"File doesn't exist in this directory. Pass valid filename as an argument in the execution command. \nFor example : python {os.path.basename(sys.argv[0])} filename.txt")