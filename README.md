## Key Generation, File Encryption and File Decryption using RSA Algorithm.

To read up on RSA Algorithm, it's [Wiki](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) gives a good exaplanation.

Once the file is encrypted, the program requires the user to remember just the decryption key and N to decrypt it.

### Breakdown
- `Key_Generator.py` : 
  - Generates _**keys -> e, d, N**_ required for encryption and decryption for any file.
  - It takes values of "p" and "q" from the user.
  - If the user doesn't want to give inputs, default values are used.
  
- `Encryptor.py` : 
  - Encrypts file using _**encryptor -> e**_ and _**modulo multiplier -> N**_ generated from `Key_Generator.py`.
  - It takes the name of the file which you want to encrypt as a command line argument.
  - It modifies the file thus, encrypting it permanently.
  - NOTE : file should be in this same directory.
  
- `Decryptor.py` : 
  - Decrypts file using _**decryptor -> d**_ and _**modulo multiplier -> N**_ generated from `Key_Generator.py`.
  - It takes the name of the file which you want to encrypt as a command line argument.
  - It doesn't modify the file, instead it displays decrypted contents on the terminal thus keep the file encrypted.
  - NOTE : file should be in this same directory.
  
---
This folder also has two .txt files. One, `plaintext.txt` and another, `ciphertext.txt`.  
`plaintext.txt`'s encrypted version looks like `ciphertext.txt`.  
Try to decrypt `ciphertext.txt` using `Decryptor.py` with d = 13879 and N = 2765669.  
Or Try to encrypt `plaintext.txt` using `Encryptor.py` with e = 199 and N = 2765669.