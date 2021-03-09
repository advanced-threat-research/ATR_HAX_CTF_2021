# Solution Write Up to One Time Only!

1. Created 4 keys for each message that produced "ATR\[" starting at position 0,1,2,3
2. Decrypted the other messages with the same key and searched for human readable
words.
3. Found one key that in column 23, produced "Neba" for message 1, " are" for message 2,
and "ATR\[" for message 3
4. I assumed that the rest of "Neba" is "Nebakanezzer", so I found a key that produced
"Nebakanezzer" at position 23 for message 1, " are absurd " for message 2, and
"ATR\[Youllnev" for message 3
5. I assumed that the rest of "Youllnev" is "er". This resulted in "Nebakanezzer, " are
absurd Ac", and "ATR\[Youllnever"
6. I assumed the rest of "absurd Ac" is "absurd AcidicZero". This resulted in
"Nebakanezzer, di", " are absurd AcidicZero" "ATR\[YoullneverbreakMe\]"

### Source code of Solver (Python)
```python
characters = [' ','!','"','#','$','%','&', "'",'(',')','*','+',',','-
 ','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F',' G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`' ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z
 ','{','|','}','~']
files=["encryption1.txt", "encryption2.txt", "encryption3.txt"]
result="ATR["
#result="Nebakanezzer"
#result="ATR[Youllnever"
#result=" are absurd AcidicZero"

keys = []
#files=["encryption1.txt"]
for filename in files:
  data = ""
    with open(filename) as f:
      data = f.read()
    # generate a key starting at different positions
  #for p in [23]:
  for p in range(0,len(result)):
    # pad the beginning with 'x'
    key = "x" * p
    for n in range(p, len(data) - len(result)):
      if (n-p) % len(result) != 0:
        continue

      for n2, k in enumerate(result):
        if n2+n >= len(data):
          continue
        key += characters[(ord(data[n2+n]) - ord(k) - 32) % 95]

    # add extra padding to the key incase the message is longer
    key = key + "x" * 60
    keys.append(key)

#with open("d4.txt", "w") as f:
# f.write(keys[0])

outfiles = ["k" + str(i+1) + ".txt" for i in range(0,len(keys))]
for n,filename in enumerate(outfiles):
with open(filename,'w') as f:
  f.write(keys[n])
 ```
