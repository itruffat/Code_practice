## Why do I have these modules and write my pieces of code the way I do?

It all started with the idea to optimize my competitive programming practices by reducing the ammount of time expent dealing with input/output handling, allowing me to focus on the problems themselves. Since many online judges have their own approach of dealing with IO (or in UVA's case, each problem does it diffently), I decided to streamline the process as much as possible. 

As such, I priorized comfort and speed. This lead to code, tools and practices that may not be ideal or even well-polished.

* For input handling, I decided to use of Python's iterators. If we treat the input-flow as an iterator, then it doesn't matter from which source the input is coming from. Moreover, for those problems that need exception handling, every exception is the same. (StopIteration)

* For output handle, I decided to make use of Python's print parameter. By adding a library that includes output file (or "None" for standard output) and an output string termination (or "None", for the standard "\n")

* Since I was always repeating the same lines of code, I decided to use an "execfile" ("exec(open(<file>).read())"). 

* With a handful of exceptions (such as Google's Kickstart), most the judges require the answer to be on a single file. To be ready for those cases, I have a keyboard shortcut to "replaceFileExecForFileLines.py", which copies the code into a file (or to the clipboard), replacing every "execfile" for the appropiated lines. 

* Since files may be moved from time to time, I use the code from "auxiliaryReRoute.py" to re-furbish all the relative paths to these snippets. (under the asumption that each file makes AT MOST one reference to _auxiliary)

* In the future I might replace the "execfile" equivalents for simple imports. There are many valid reasons why "exec" is considered bad code practice. For the time being, I found it easier to do it this way since parsing+replacing the "execfile" commands for the appropiate lines was almost trivial.

* I may also write a handful of "IO-templates" in case I deem them neccesary.

I am fully aware of many short-comings of this technique, and of the existence of other workflows that might help me improve beyond them. Should I find these methods insufficient, I might rework them or throw them out all together.