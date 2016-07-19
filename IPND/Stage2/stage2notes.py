#Computer Science is a systematic method of taking a prolem and
#breaking it down into stages that can be described explicitly enough for a computer to solve

#Advice from Sergey Brin re building a search engine - FIND A GOOD CORPUS OF INFORMATION THAT YOU WIL BE EXCITED TO SEARCH
## Applicable to data journey - where is the data that I would be most excited to explore???

"""In the next few videos, Dave will explain what programming is and why it's such a powerful tool.

He will use terms like:

computer
program
precise sequence of steps
computation
high-level language
input
interpreter"""

#compared a toaster (1 function, with some variations of that single function possible)
#to a computer, which can essentially do anything but it needs instructions = programs
#Python (named after Monty) acts as an interpreter:
## allowing us to use a high level language that interprets our commands into a language the computer can understand -- C?

"""What Dave Just Said
In the answer video for the previous quiz, Dave said

"The programs you'll write in this class will be Python code. Those will be input to another program which is a
Python interpreter that follows the instructions in your code and it does that by following the instruction in its code... and you'll be able to run all that using your web browser."

Hidden in these two sentences are examples of 3 of the 5 ways you can think like a programmer:

The line "...follows the instructions in your code..." references the *procedural thinking* required of programmers.

The entire quote demonstrates a deep *technological empathy* (which you don't need to have at this point) for how
computers and programs work.

When Dave thinks of a Python program, a Python interpreter, and a web browser as different versions of the same
thing (a computer program) he's showing *abstract thinking*."""

#Natural language is too ambiguous for computers. The same word can have different meanings, other words or sentences need context and they are generally
#only good if you've spent a long time learning

#Backus-Naur form is a systematic way of structuring the grammar of computers. It came when John Backus (lead designer of Fortran in 1950s at IBM) tried to
#translate Fortran and found the language to be too vagueself.

#The idea is that you start with 'non-terminals', which are essentially variables with set rules and through a process of derivation you arrive at a set of 'terminals'
#which can be thought of as explicit representations of each non-terminal variable as defined in the programs rules.
#(See https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4180729266/concepts/487134810923)

#Backus-Naur is an example of recursive grammar, which is very powerful and can generate almost infite possibilities from a few basic rules
#It is possible to derive the whole Python language from a similar starting point to video: https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4180729266/concepts/487043110923

Lightspeed quiz

# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
speed_of_light = 299792458   #meters per second
centimeters = 100            #one meter is 100 centimeters
nanosecond = 1.0/1000000000  #one billionth of a second

light_cm_nanosec = speed_of_light * centimeters * nanosecond
print(light_cm_nanosec)

""" Practice Debugging
This practice session will focus on debugging, which is one of the five ways programmers think. Python requires code be written with a very specific syntax. This means that small typos can lead to big problems!

In each of the following exercises, you'll be given code. Sometimes the code will work and sometimes it won't. For each exercise, do the following:

Read through the code and try to predict what it is supposed to do.
Make a guess about whether or not it will actually work.
Without modifying the code yet, press the Test Run button.
Observe the output that's displayed.
If there's an error message, read through it.
These error messages are usually very cryptic. That's okay. Go through each message and try to decipher what the actual problem was. If you can figure it out, fix the code and then press Test Run again.
HINT: It's often a good idea to start at the last line of the error message."""

"""
Before You Continue
The purpose of the previous three exercises was to show you just how easy it is to write code that doesn't work.

In the next lesson you will write more sophisticated code. As you add sophistication, you will also add more ways to make mistakes. And you will make mistakes.

The trick to dealing with programming mistakes (called "bugs") is not to avoid making them entirely. That's impossible. The trick is to develop a system for finding and fixing them.

Whether you know it or not, you're already developing a system. That system will continue to improve throughout the Nanodegree.

This is one of the most important lessons you will take in this Nanodegree because it introduces one of the most important (and potentially confusing) topics in all of programming: the variable.

As you watch the next few segments, focus on these three questions (these questions could go into your notes web page):

1. What is a variable?
2. What does it mean to assign a value to a variable?
3. What is the difference between what the equals = means in math versus in programming. What's the difference between this: 2 + 3 = 5 and this: my_variable = 5?
"""

###Variables:

#Make programs easier to understand
#Enable us to resuse items or bits of code, or change parts as we see fit

#Variables vary, so remember that changes in variables used in a program will change the output
# useful feature for iteration e.g.
days = 7*7
days = days - 1
#In the second line, the RHS is evaluated first, so each time it will take 1 off the starting value of days and save a
#new version of the variable days

##ASSIGNMENT - in Python (and many programming languages, equal does not mean mathematically equal - but assignment)
#Think of it as an arrow (like in R). Reason most programming languages don't use an arrow is that it is harder to type and likely to be used a lot

"""Question When Python deals with code like
days = days - 1,
which side of the = does it evaluate first: the left or the right? Why do you think it works this way?"""

#I think it does this as it is following something similar to the Backus Naur form; meaning it needs to derive the variables and operations
#in the statement to their terminal values in order to make changes to the variable itself that is the output of that statement


# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.

my_age = 34.15
leap_years = int(my_age / 4)
print(leap_years)
days_alive = (my_age * 365) - leap_years
print(days_alive)

Strings

###Subsetting strings - abstraction

<string>[<expression>(number)] #one character string returned
<string>[<expression>(start number):<expression>(stop number)]
#string that is subsequence of the characters in s from first poistion to stop -1

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.
s = 'audacity'
print("U"+s[2:])

Use function <string>.find(<substring>) to find strings within strings
#returns index number substring starts at
# output of -1 means string was not found

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1


###Adding extra parameter to find
#a second number in parameters to find enable us to specify where the search should start from

<string>.find(<substring>, <startpoint>)


# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string


#strings practise

"""For most strings, all of these options would work.


But if s is the '' empty string, then s[0] will cause an error because there is no character at position 0.


This is called an edge case in programming. It's a situation that doesn't come up too often (you usually don't need to use an empty string), but it does happen sometime.


It's easy to forget about edge cases and doing so is a common cause of bugs."""


# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print(s[0:2]+t[3:])


# Insert the proper slicing indices for the substring variable
# so that the slice is a string that contains everything after "A NOUN".
# For example, if we wanted to store everything after "went", the returned
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."
substring = sentence[6:]

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB"
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]


# Set noun_replacement and verb_replacement to your own noun and verb strings.
# Then, concatenate the variables substring1-3, noun_replacement, and
# verb_replacement and assign the result to the variable new_sentence so that
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "dog" # your noun here
verb_replacement = "dribble" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
# your code here
print(new_sentence)

#note the following two lines of code are equivalent

new_sentence += substring1
new_sentence = new_sentence + substring1



# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America.
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

mary = "Mary"
# Your code goes here
gabriel = kathleen = salwa = katie = randa = mary

# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
gabriel = kathleen

# Test to see if all of these variables will print out the string "Mary"
print gabriel
print kathleen
print salwa
print katie
print randa
print mary



# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find("NOUN")
verb_position = text.find("VERB")

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

# ENTER CODE BELOW HERE
first = text.find("zip")
print text.find("zip", first + 1)

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function


### replace function
text.replace("old", "new")


# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "duck")
sentence = sentence.replace("VERB", "waddle")
print sentence
