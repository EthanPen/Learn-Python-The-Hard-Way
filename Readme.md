##LEARN PYTHON THE HARD WAY

Tags: Summarize

---

[Table Of Contents](http://learnpythonthehardway.org/book/)

1. Ex0 - Ex5
2. Ex6 - Ex10
3. Ex11 - EX15
4. Ex16 - EX20
5. Ex21 - Ex25
6. Ex26 - Ex30
7. Ex31 - Ex35
8. Ex36 - Ex40
9. Ex41 - Ex45
10. Ex46 - Ex50
11. Ex51 & Ex52



####1. Ex0-EX5

1. Sys: MAC OS X EI Capitan  
2. Text Editor: **TextWrangler**  

**Variables and Names**

consist with letters, numbers, underscore. start with letters or underscore.  

**Comments and Pound Characters**  

	"# A comment, this is so you can read your program later."  
	"# Anything after the # is ignored by python."  

**keyword:**  

1. **print** --> print "Hello World!"

####2. Ex06-Ex10

Here's a tiny piece of fun code to try out:

	while True:
    	for i in ["/","-","|","\\","|"]:
        	print "%s\r" % i,

**Q:What is the difference between %r and %s?**  
**A:** Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.

**Q:What's the point of %s and %d when you can just use %r?**  
**A:** The %r is best for debugging, and the other formats are for actually displaying variables to users.

**Q:Should I use %s or %r for formatting?**  
**A:** You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."

**Q:Why does %r sometimes print things with single-quotes when I wrote them with double-quotes?**  
**A:** Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for debugging and inspection, so it's not necessary that it be pretty.

####3. Ex11-Ex15

	from sys import argv

	script, first, second, third = argv

	print "The script is called:", script
	print "Your first variable is:", first
	print "Your second variable is:", second
	print "Your third variable is:", third
	
The argv is the "argument variable,", This variable holds the arguments you pass to your Python script when you run it.


**Q:What's the difference between _input()_ and _raw_input()_?**  
**A:**The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.

**Q:Does txt = open(filename) return the contents of the file?**  
**A:** No, it doesn't. It actually makes something called a "file object." You can think of a file like an old tape drive that you saw on mainframe computers in the 1950s, or even like a DVD player from today. You can move around inside them, and then "read" them, but the DVD player is not the DVD the same way the file object is not the file's contents.

####4. Ex16-Ex20


**Q:Does just doing open(filename) open it in 'r' (read) mode?**  
**A:** Yes, that's the default for the open() function.


	def print_two(*args):
    	arg1, arg2 = args
	    print "arg1: %r, arg2: %r" % (arg1, arg2)

**Q:What does the * in (*args) do?**  
**A:** That tells Python to take all the arguments to the function and then put them in args as a list. It's like argv that you've been using, but for functions. It's not normally used too often unless specifically needed.

**Q:How does readline() know where each line is?**  
**A:** Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far. The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.


####5. Ex21-Ex25

**Read Some Code**


1. Go to bitbucket.org, github.com, or gitorious.org with your favorite web browser and search for "python."
2. Pick a random project and click on it.
3. Click on the Source tab and browse through the list of files and directories until you find a .py file.
4. Start at the top and read through the code, taking notes on what you think it does.
5. If any symbols or strange words seem to interest you, write them down to research later.

Your job is to use what you know so far and see if you can read the code and get a grasp of what it does. Try **skimming the code first**, and then **read it in detail.** Try taking very difficult parts and read each symbol you know out loud.

Now try some of these other sites:

* [github.com](http://github.com)  
* [launchpad.net](http://launchpad.net)
* [gitorious.org](http://gitorious.org)
* [sourceforge.net](http://sourceforge.net)


####6. Ex26-Ex30

[**Memorizing Logic**](http://learnpythonthehardway.org/book/ex27.html)

**Q:What happens if multiple elif blocks are True?**  
**A:** Python starts and the top runs the first block that is True, so it will run only the first one.


####7. Ex31-EX35
  
**While Loops:**  

1. Make sure that you use while-loops sparingly. Usually a for-loop is better.  
2. Review your while statements and make sure that the boolean test will become False at some point.  
3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.  


####8. EX36-Ex40

**_Designing and Debugging_:** 
 
1.Rules for If-Statements:

a. Every if-statement must have an else.  
b. If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.

2.Rules for Loops:

a. Use a while-loop **only** to loop forever, and that means probably never. This only applies to Python; other languages are different.
b. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.

3.Tips for Debugging:

a. The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.
b. Code a little, run a little, fix a little.

**_Symbol Review_**  

**1. Reading Code**  

a. Functions and what they do.
b. Where each variable is first given a value.
c. Any variables with the same names in different parts of the program. These may be trouble later.
d. Any if-statements without else clauses. Are they right?
e. Any while-loops that might not end.
f. Any parts of code that you can't understand for whatever reason.  

**2. Doing Things to Lists**  

When to Use Lists:  

a. If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.  
b. If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.  
c. If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.

**3. Dictionary**  

When to Use Dictionary or Lists

1. You have to retrieve things based on some identifier, like names, addresses, or anything that can be a key.
2. You don't need things to be in order. Dictionaries do not normally have any notion of order, so you have to use a list for that.
3. You are going to be adding and removing elements and their keys.


**4. Module, Classes, and Objects**  

1. Modules Are Like Dictionary  
2. Classes Are Like Modules, a "mini-module" 
3. Objects Are Like Import

**5. Getting Things from Things**  

	#dict style	
	mystuff['apples']

	#module style
	mystuff.apples()  
	print mystuff.tangerine  

	#class style
	thing = MyStuff()  
	thing.apples()  
	print thing.tangerine  
	
**Q:Why do I need self when I make __init__ or other functions for classes?**  
**A:**If you don't have self, then code like cheese = 'Frank' is ambiguous. That code isn't clear about whether you mean the instance's cheese attribute, or a local variable named cheese. With self.cheese = 'Frank' it's very clear you mean the instance attribute self.cheese.


####9. EX41-EX45

**1. _EX41 --> oop_test.py_**

	str.strip([chars])
	Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

	random.shuffle(x[, random])
	Shuffle the sequence x in place. The optional argument random is a 0-argument function returning a random float in [0.0, 1.0); by default, this is the function random().
	Note that for even rather small len(x), the total number of permutations of x is larger than the period of most random number generators; this implies that most permutations of a long sequence can never be generated.

	random.sample(population, k)
	Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.

	random.randint(a, b)
	Return a random integer N such that a <= N <= b.

	str.replace(old, new[, count])
	Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

**Q:What does result = sentence[:] do?**  
**A:**That's a Python way of copying a list. You're using the list slice syntax [:] to effectively make a slice from the very first element to the very last one.


**2. Basic Object-Oriented Analysis and Design**

a. Write or draw about the problem.
b. Extract key concepts from 1 and research them.
c. Create a class hierarchy and object map for the concepts.
d. Code the classes and a test to run them.
e. Repeat and refine.


**3. Inheritance Vs. Composition**

a. Implicit Inheritance
b. Override Explicitly
c. Alter Before or After (**super()**)

**MRO:** "method resolution order"

**When to Use Inheritance or Composition**

The question of "inheritance versus composition" comes down to an attempt to solve the problem of **reusable** code. You don't want to have duplicated code all over your software, since that's not clean and efficient. **Inheritance** solves this problem by creating a mechanism for you to have implied features in base classes. **Composition** solves this by giving you modules and the ability to call functions in other classes.

a. Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
b. Use composition to package code into modules that are used in many different unrelated places and situations.
c. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

####10. Ex46-Ex50

**1. Advanced User Input**

**Breaking Up a Sentence**
	
	stuff = raw_input('> ')
	words = stuff.split()

**"tuple":** A tuple is nothing more than a list that you can't modify.It's created by putting data inside two () with a comma, like a list:

	first_word = ('verb', 'go')
	second_word = ('direction', 'north')
	third_word = ('direction', 'west')
	sentence = [first_word, second_word, third_word]
	
This creates a pair (TYPE, WORD) that lets you look at the word and do things with it.



####11. Ex51 & Ex52

**Web Game**


![A representation of Octdrey Catburn](http://octodex.github.com/images/octdrey-catburn.jpg)






