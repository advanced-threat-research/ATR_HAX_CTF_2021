# Solution Write Up to I've Seen Sites Like This Before!

Upon loading link 1, there appear to be some clues in the HTML source code.
![Developer comments in HTML source code](assets/images/00.png)
**Figure:** Developer comments in HTML source code

![Error message displayed via link1](assets/images/01.png)
**Figure:** Error message displayed via link1

By manipulating the “iv=” parameter, we get addition error output.
![Error output “invalid IV length”](assets/images/02.png)
**Figure:** Error output “invalid IV length”

By changing the last two digits of the “iv” parameter to 00, the UID changes to 27.

iv=f15188446e6e3100
![UID changed to 27](assets/images/03.png)
**Figure:** UID changed to 27

By changing the last two digits of the “iv” parameter to 27, the flag was revealed!
![flag](assets/images/04.png)
