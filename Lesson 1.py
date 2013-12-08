__author__ = 'FossilizedCarlos'

# Lesson 1: How to get started

# This is a Python comment. Lines that begin with a '#' are ignored by the
# Python interpreter. Comments are useful for documenting code or explaining
# quiz questions!

# Write a Python program that prints out the number of minutes in seven weeks.
# Click the "Run" button below to try running your code and see the output,
# and click "Submit" to submit your answer.

print 7 * 7 * 24 * 60

# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print (1.0/1000000000) * 100 * 299792458

# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print speed_of_light / cycles_per_second

# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.
age = 32
print age * 365

# Define a variable, name, and assign to it a string that is your name.
name = "Carlos"

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.

s = 'audacity'
print 'U'+s[2:]

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
url = page[page.find('"',start_link)+1:page.find('>',start_link)-1]
print url

# Lesson 1: Problem Set

# Write Python code that prints out the number of hours in 7 weeks.
print 7 * 7 * 24

# Write Python code that stores the distance
# in meters that light travels in one
# nanosecond in the variable, nanodistance.

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code,running
# print nanodistance
# should output 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line
nanodistance = speed_of_light/nano_per_sec

print nanodistance

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[:3]+t[4:]

# Assume text is a variable that holds a string. Write Python code
# that prints out the position of the first occurrence of 'hoo'
# in the value of text, or -1 if it does not occur at all.

text = "first hoo"

# ENTER CODE BELOW HERE

print text.find('hoo')

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

#ENTER CODE BELOW HERE

print text.find('zip', text.find('zip')+1)

# Given a variable, x, that stores the
# value of any decimal number, write Python
# code that prints out the nearest whole
# number to x.
# If x is exactly half way between two
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159
# >>> 3 (not 3.0)
# x = 27.63
# >>> 28 (not 28.0)
# x = 3.5
# >>> 4 (not 4.0)

x = 3.14159
x = x + .5

#ENTER CODE BELOW HERE
number = str(x)
period = number.find('.')
print number[:period]

# Lesson 1: Problem Set (Optional)

###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace
# the tricky parts with a marker.
# Write a program that takes a line of text and
# finds the first occurrence of a certain marker
# and replaces it with a replacement text.
# The resulting line of text should be stored in a variable.
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
#marker = "EY"
#replacement = "Eyjafjallajokull"
#line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

replaced = line[:line.find(marker)] + replacement + line[line.find(marker)+len(marker):]

print replaced
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.

###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads
# the same backwards as forwards. Make a program
# that checks if a word is a palindrome.
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise.
# The word contains lowercase letters a-z and
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
# word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###

is_palindrome = word.find(word[::-1])

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"