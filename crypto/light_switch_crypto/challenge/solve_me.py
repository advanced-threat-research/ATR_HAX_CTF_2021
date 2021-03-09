
"""
	This script reads from "key" and "encrypted_flag" and uses "magic_func" to
	convert the encrypted flag into its decoded version.

	You are asked to implement the magic_func as described in CTF_1.png
	Successful decryption should print a valid flag (ATR[....]) in the console.

	This script is expected to run with python3.

"""
import string

def magic_func(A, B):

    #################################################################################
    #                                                                               #
    #                     Modify the function starting here                         #
    #                                                                               #
    #################################################################################

    # Implement here the circuit logic described in "CTF_1.png"
    # The output of magic_func is the variable 'o'
    # 'o' needs to be a bit (a python integer that is either 0 or 1)
    # Input are A and B as seen in the diagram, and are also bits as defined above.
    # You can use logical operators such as & | ^ ~ on A and B

    o = 0
    return o



def tobits(s):
    # This function coverts a list of bytes (represented as a string)
    # into its binary representation
    result = []
    for c in s:
        bits = bin(ord(c))[2:] #convert unicode of every character to binary ([2:] since remove 0b)
        bits = '00000000'[len(bits):] + bits #append 0's in front
        result.extend([int(b) for b in bits]) #add to list and return
    return result

def frombits(bits):
    # This function converts a list of bits (reprenseted as integer in the range 0,1)
    # into a a list of bytes (represented as a string)
    chars = []
    for b in range(int(len(bits)/8)): #divide by 8
        byte = bits[b*8:(b+1)*8] #take chunks of 8 bits and convert to string
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def main():
    # First load the key and the encrypted flag
    with open('key', 'r') as fa:
        key = ''.join(fa.readlines())
        print('\n Reading my key: ', key, '\n')
    with open('encrypted_flag', 'r') as f:
        msg = ''.join(f.readlines())
        print('\n Reading encrypted flag: ', msg, '\n')

    # Convert key and message as their binary representation
    b_msg = tobits(msg)
    b_key = tobits(key)

    o = [] # Array of bits that will contains the decoded message
    print('\n *** Complete magic_func *** \n')

    for i in range(len(b_msg)):
        # Iterates over each byte of the message and the key
        # And feed them to the magic function for "decoding"
        o.append(magic_func(b_msg[i], b_key[i]))

    new_o = frombits(o) # Converts the decoded message from bit to string
    print("\n Output: ", new_o, '\n')


if __name__== "__main__":
    main()
