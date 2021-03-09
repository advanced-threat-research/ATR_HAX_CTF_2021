# Know your header (Part I)

### 200 Points

## Description
The next challenge was encoded and we don't know the key. 
We were able to recover the script used to encode the challenge and a hint binary. 

What we know is that it is a Linux binary running on a x64 Ubuntu 18.04. 
Maybe by looking at the encoding algorithm and the hint binary you can figure out how to decode it? 

The flag for this challenge is the ATR[key] where key is the key you found, in hex, and lower case 
(for example, if the key is 5566778899aabbcc, the flag will be ATR[5566778899aabbcc])

Good luck! 

## Hint
The hint is in the file ".hint"