# Auxiliary Folder

## What are these modules and why are they written this way?

The idea was to optimize the time spent tackling the juicy part of the competitive programming challanges by the reducing the time spent doing busy work. In particular, the idea was to streamline the I/O handling as much as possible. 

As such these solutions are somewhat Quick and Dirty and not entirely ideal, but they are serviceable, comfortable and fast.

* For input handling, I decided to use of Python's iterators. If we treat the input-flow as an iterator, then it doesn't matter from which source the input is coming from. Moreover, for those problems that need exception handling to know when the input ends, every exception is the same. (StopIteration)

* For output handle, I decided to make use of Python3's "print" parameter. By adding a library that includes output file (or "None" for standard output) and an output string termination (or "None", for the standard "\n")

* Keeping in mind most online Judges require a single self-contained file as answer, I decided to use the an *execfile expression* ("exec(open(<file>).read())") to include the solutions implemented here. While *execfile* is universally considered bad code practice, it's a cost worth paying for a QnD tool due to how stramlined the proccess ends up being.
  
* To merge the different files into a single answer, one must simply replace the *excefile expression* for the content of that particular file. To speed things up, there is a file called *replaceFileExecForFileLines.py*, which copies the code into a file, replacing every "execfile" for the appropiated set of lines.
 
  * *replaceFileExeceForLines.py* actually has 3 modes, mode0 prints to the screen (for self-debugging purposes), mode1 copies to the clipboard and mode2 creates a newfile. For challenges that require you to paste the code into a webpage (example: UVA), mode1 is more advisable.
  
  * As a side-note, I have a keyboard shortcut to *python3 -m replaceFileExecForFileLines.py 2 "%f" "%p"*, where *"%f"* is the name of the file and *"%p"* is the path of the file. This accelerates the commiting process, as one key-press is all that's the required to have a single file.

* Taking into consideration that files may be moved from time to time, the tool "auxiliaryReRoute.py" can be used to fix all the *excefile expressions* relative paths to these solutions. (currently the tool only works with a single reference to *_auxiliary*)

* Simple libraries like basic line manipulation and tree structures have been added, but they are still on beta and should not be used.

## What could be changed?

* I might replace the *execfile* equivalents for simple imports. There are many valid reasons why "exec" is considered bad code practice. This would require me to change both tools for compiling and fixing paths, while dealing with the native Python libraries.

* Finish, Improve and Expand the subset of aditional libraries, particularly the structures.

## Disclaimer 

I am fully aware of many short-comings of this technique, and of the existence of other workflows that might help me improve beyond them. Should I find these methods insufficient, I might rework them or throw them out all together.
