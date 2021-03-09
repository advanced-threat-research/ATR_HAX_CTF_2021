# Solution Write Up for Password in a Haystack

**rules**
1. All passwords must be 6-12 printable characters in length. 
2. Each password must contain at least 3 unique digits 
3. Passwords cannot contain 3 consecutive characters of your username nor it's reverse. This is case insensitive. 

The simplest way to solve this is to write a program. Read in output.txt and use single function for each rule to filter it down. You could probably use a text editor filter if it's powerful enough. However, let's do this in REGEX... because.

Also, I'm on OSX. This becomes important later.

1. Take a look at the file and file length for reference

```
#File output
cat output.txt 
```
```
#File length
wc -l output.txt
```

2. Write a regex for rule #1 and check to ensure it's filtering reasonably.

```
grep '^.\{6,12\}$' output.txt | wc -l
```

3. Seems good so write that to a new file.

```
grep '^.\{6,12\}$' output.txt >> rule1
```

4. I'm going to break rule 2 into two parts. One that ensures the user name characters don't show up consecuatively forwards, but also another to ensure they don't show up backwards. I use -i for case insensitivity and use -v to trigger on all strings EXCEPT what is found in my regex. For the forwards one:

```
grep -iv 'ste\|tev\|eve\|ve5\|e55\|577' rule1 >> rule2-part1
```

5. Again, I checked the strings and count using wc -l to ensure everything seems reasonable. Now for the backwards one I can just reverse every character in my regex. I even did 'eve' even though it's not necessary.

```
grep -iv 'ets\|vet\|eve\|5ev\|55e\|775' rule2-part1 >> rule2-part2
```

Again, I check the strings and the count. Everything look reasonable.

Now this is where it gets tricky. For rule number 3 I need to have at least 3 unique numbers. I know I can do this with a negative lookhead paired with groups but they are harder to write then normal rules. For a sanity check lets try a simple one. Negative look aheads are in the format \(?!xxx\) and groups are just pattern inside \(\) such as \(hello\). I can access group one by using \\1, group 2 using \\2 and so on. Of course, you need to use the proper syntax for your regex implimenation. OSX needs the \\ escape characters in front of the parenthesis so we have...

```
grep '^.*\(\d\).*\(?!.*\1\)\(\d\).*' rule2-part2
```

Nothing?

Does my grouping work?
```
grep '^.*\(\d\)\1' rule2-part2
```

I should see strings with consecutive digits and I do. Grouping is working as expected. Does my negative lookahead work?
```
grep '^.*\(a\)\(?!.*\1\)$' rule2-part2
```
Nothing. I expect this to give only one 'a'. I know they exist. I also know 55 exists. Lets try a regular lookahead to try those.

```
grep '^.*5\(!=5\)' rule2-part2
```

Nothing....urgh. Turns out OSX grep doesn't support lookaheads and lookbehinds. The homebrew version does if we use perl syntax! It has the added bonus of not needing escape characters before parathensis. 

```
brew install grep
```

Now to use the brew binary we use ggrep with the flag '-P' for perl syntax.

```
ggrep -P '^.*(\d)(?=\1)'
```

I see consecutive digits so all is well. Now to build rule #3. I need three distinct numbers so I'll need multiple groups. I'm allowed to have duplicates but 3 must be unique... so we'll do a little trick here.

.\* will find all characters regardless if they are numbers. This will allow for duplicates. Then all I really need to do is find a number, and look ahead for a number that's not that. Then I'll do it again, but also ensure it's not the same as the last number I found.

```
ggrep -P '^.*(\d).*(?!.*\1)(\d).*(?!.*\2)(?!.*\1)(\d).*' rule2-part2
```

note ^.\*\(\\d\).\*\(?!.\*\\1\)\(\\d\) just finds a string with two digits with ANY second digit not being the first.

Then I can add .\*\(?!.\*\\2\)\(?!.\*\\1)\(\\d\) which this says continue to find a ANY digit BUT NOT THE SECOND DIGIT, NOR THE FIRST DIGIT.

I then follow it by whatever I want with .*.

Afer running it I get the unique string **1-r-d4-n33d1** 
\(I ARE THE NEEDLE\)
Wrap that in the flag format and we have our flag **ATR\[1-r-d4-n33d1\]**

