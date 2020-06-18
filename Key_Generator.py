""" 
This program generates Encryption key, Decryption key and Modulo 'N' using the RSA Algorithm. 
It can work with custom values for 'p' and 'q' provided by the user.
"""
import math

def is_prime(n):
    """ 
    Checks whether the given input is prime.

    Parameters : 
    n (int) : number to be checked

    Returns :
    True : If number is prime.
    False : If number is not prime.
    """
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def set_p_q(flag):
    """  
    Take values of 'p' and 'q' from the user. If input is invalid, it displays an Error message.

    Parameters :
    flag (boolean) 

    Returns :
    p (int) : Value of p taken from the user.
    q (int) : Value of q taken from the user.
    flag (boolean) : True, if correct inputs provided. False, it incorrect inputs provided.
    """
    p, q = None, None
    try:
        p = int(input("[ Prime Number ] Enter value for p : "))
        q = int(input("[ Prime Number ] Enter value for q : "))
        flag = False
    except ValueError:
        print("VALUE_ERROR | Enter value again!")

    return p, q, flag 

def custom_or_default():
    """  
    Checks whether the user wants to use the default values or provide custom inputs.
    If user enters any number other than 0 or 1, it displays an Error message and keeps asking for the correct inputs.

    Returns :
    decision (int) : 0(use default values) OR 1(user will provide custom values).
    """
    flag = None
    while flag==None:
        decision = input("Enter '0' for using default values \n\tOR \n'1' for custom inputs for p, q :")
        if int(decision) in [0, 1]:
            decision = flag = int(decision)
        else:
            print("- - - - - \nERROR! Enter integer values of '0' or '1'\n- - - - - ")
    
    return decision

def set_e_d():
    """  
    Calculates the encryption and decryption keys.

    Returns : 
    x (int) : Encryption key.
    y (int) : Decryption key.
    """
    x = 1

    eq = (p - 1) * (q - 1) + 1

    y = 1
    xy = x*y

    while xy != eq:
        x += 1
        y = int(eq / x)
        xy = x*y

    return x, y

if __name__ == "__main__":
    decision = custom_or_default()

    flag = True
    if decision == 1:
        while flag == True:
            p, q, flag = set_p_q(flag)
    else:
        p = 1009
        q = 2741

    if not is_prime(p) or not is_prime(q):
        raise ValueError('P or Q were not prime')

    x, y = set_e_d()

    print("---------------------------\n", end="")
    print ("public key / encryption key 'e' : " + str(x))
    print ("private key / decryption key 'd' : " + str(y))
    print ("modulo (pq) / 'N': " + str(p*q))
    

