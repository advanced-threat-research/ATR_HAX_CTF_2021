#!/usr/bin/env python2
import sys


def encode(data, key):
    
    # Initialize the return value of the function to an empty string
    res = ""

    # Iterate over all the bytes in data
    for i in xrange(0, len(data)):
        # Get the i-th character in the data
        c = data[i]

        # Get the i-th character of the key (modulo the length of the key)
        # Fore example, if the key length is 10 characters, and i is 12, (i % 10) equals 2 
        # We do that so that when we reach the end of the key, we loop back to the begining
        k = key[i % len(key)] 

        # ord converts a character into its ascii value (i.e. a number)
        # chr converts an ascii value (a number < 256) into a character (a byte) 
        # ^ is the xor operator 
        # Info about xor: 
        #  a ^ a  = 0  (every value is its own opposite)
        #  a ^ b = b ^ a (the order does not matter)
        # a ^ b ^ c  = c ^ b ^ a = ...   (same with more values) 
        # 0 ^ a = a (xoring with 0 doesn't change the value) 
        
        encoded_val = chr(ord(c) ^ ord(k))
        res += encoded_val
    return res






if __name__ == "__main__":
    
    # Verifiy the arguments passed to the script 
    # are ok.
    if len(sys.argv) < 4:
        print "Usage: {} key_hex input output".format(sys.argv[0])
        sys.exit(-1)
    if (len(sys.argv[1]) % 2 == 1):
        print "Invalid key length. It needs to be an even number."
        sys.exit(-1)
   
    # Converts the hex representation of a string into the actual bytes
    key = sys.argv[1].decode("hex") 

    if (len(key) > 8):
        print "This version of the encoder only works with short keys"
        sys.exit(-1)

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # Open the file
    # rb means reading in binary mode
    with open(input_file, "rb") as f:
        data = f.read()
    
    # Now we encode the data using the key we've read
    encoded_data = encode(data, key)

    # Open or create the output fule
    # wb means writing binary data
    with open(output_file,"wb") as f:
        f.write(encoded_data)






