# Solution Write Up for Know Your Header (Part 1)

1. Xor'ed the first 10 bytes of the encrypted file and the hint together, until the resulting 
number pattern started repeating. Resulting key: 9f05a8dd940a15dd
2. Used the key to decrypt the program with the provided decrypt program
3. Ran the program and it worked
4. Input the key into the Ctf as the flag

```python
#!/usr/bin/env python3
with open("challenge_encoded","rb") as f:
	enc = f.read()

with open("hint", "rb") as f:
	hint = f.read()

keylen=8
vals = [x ^ y for x,y in zip(enc[:keylen],hint[:keylen])]
key = [format (x, "02x") for x in bytearray(vals)]
print (''.join(key))
```

Output from ./decode.py is 9f05a8dd940a15dd which can be submitted as flag with 
**ATR[9f05a8dd940a15dd]**.

