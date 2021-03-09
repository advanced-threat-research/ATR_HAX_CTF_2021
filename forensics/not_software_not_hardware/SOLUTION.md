# Solution Write Up Not Software Not Hardware

1. Extract squashfs

```
binwalk -e download_b2ab6c5e9464f087508bd368bf116204.bin
```

2. Determine version

```
/etc/openwrt_release
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='18.06.2'
DISTRIB_REVISION='r7676-cddd7b4c77'
DISTRIB_TARGET='ramips/rt288x'
DISTRIB_ARCH='mipsel_24kc'
DISTRIB_DESCRIPTION='OpenWrt 18.06.2 r7676-cddd7b4c77'
DISTRIB_TAINTS=''
	/etc/openwrt_version

r7676-cddd7b4c77
```
By comparing the shasum hash with the listed hashes from openwrt.org, it can be determined 
that this firmware has been modified.

```
$ shasum -a 256 download_b2ab6c5e9464f087508bd368bf116204.bin e55f8441963e7fe819368112e86ef549825ef792cec3afd2f1adc3ef62cf849f download_b2ab6c5e9464f087508bd368bf116204.bin
```
No sha256 matches when compared to:
[https://downloads.openwrt.org/releases/18.06.2/targets/ramips/rt288x/](https://downloads.openwrt.org/releases/18.06.2/targets/ramips/rt288x/)

3. Found /root/.secret/
	- file.txt
	- flag.enc
	- README.txt
![image](assets/images/00.png)
	- test.enc

**flag.enc:**
U2FsdGVkX18rSgKPz/Y7N6HBK3/FG5OZeuQdjB+9DiY8gMvAF/IRSWGWn8P8s60q

4. The README.txt provides some clues. First the encryption key is likely the password of the login user store in /etc/shadow. When compared against the original OpenWRT image, it is obvious that /etc/shadow has been modified for the CTF. The second clue is “so I took the fasttrack”. After some Google searches, it was determined that fasttrack is likely a reference to the Kali wordlist used when cracking hashes with John.

```
# /etc/shadow
root:$6$19yJir3t$DKemu8nRjxvuPbDZdZcdtsJiiVd7zAXN7Q63.eepYT.R0LqsDMYCzwetEO58sPROWiVfhY1Aeu3O3awr57fv50:17994:0:99999:7:::
# Cracking hashes with John
https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/
```

**Hint** "fast track":
```
john --wordlist=/usr/share/wordlists/fasttrack.txt
```

'P@55w0rd!

```
# Decrypt flag.enc with root password
openssl enc -aes256 -in flag.enc -out flag.txt -d -a -pbkdf2 -k 
'P@55w0rd!'
```
Flag
ATR[F1rMW4r315N750H4rD]