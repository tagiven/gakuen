###############################################################################
#
#  Lesson 01 
#
###############################################################################

print 4 - 5
print 365.25 * 24

###############################################################################
## Arithmetic Expressions
#
# Recrusive Definition Grammer
#   Expression -> Expression Operator Expression
#   Expression -> Number
#   Operator -> +
#   Operator -> *
#   Number -> 0..N
#   Expression -> ( Expression )

# Speed of light per nanosec
speed_of_light = 299792458
centimeters = 100
nanosecond = 1.0/1000000000
epn = speed_of_light * centimeters * nanosecond
print epn

################################################################################
## Processors
# 
# 2.7 GHz == 2.7 Billion cycles per second
#  cycle: time computer requires to complete a single step
#  1/2.7 cycles per nanosecond
#  11.1034 cm per cycle

###############################################################################
## Grace Hopper
#
# Admiral Grace Hopper - wrote COBOL
# 

###############################################################################
## Variables
#
# Assignement Statement
#  Name = Expression
# 
#  
speed_of_light = 299792458                  # meters per second
billionth =  1.0/1000000000
cycles_per_second = 2700000000.             # 2.7 GHz
nanostick = speed_of_light * billionth * 100
print nanostick
print speed_of_light * 100
print speed_of_light / cycles_per_second    # meters light travels in one cycle

###############################################################################
## Variables can Vary
# 
cycles_per_second = 2800000000.
print cycles_per_second

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance

days = 7
print days
days -= 1
print days

age = 36
days_per_year = 365.25
print int(round(age * days_per_year))
###############################################################################
## Strings
#
# String - Sequence of characters surrounded by quotes

print 'Hello'
print "Hello"
hello = "Howdy"
print hello

###############################################################################
#
# Ada
#
# Countess of Lovelace
name = 'Grey'
print 'Hello ' + name

# Concatenation
#
#   <string> + <string> 

##############################################################################
## Strings and Numbers
#
#  Can not concatenate string and int types
#  Can multiply string values using *
name = 'Dave'
print 'Hello ' + name + '!' + '!' + '!'
print 'Hello ' + name + '!' * 3
print 'My name is ' + name + '!' * 3

###############################################################################
## Indexing Strings
#
# <string>[<expression>]
print 'udacity'[0]
print 'udacity'[1+1]
name = 'Grey'
print name[0]
print name[3]
print name[-1]
print name[-2]

## Quiz

###############################################################################
## Selecting Sub Sequences
#
# <string>[<expression>:<expression>]
#           number       number
#
#   string that is a subsequence of the characters in str starting 
#   from position start, and ending with position stop
word = 'assume'
print word[3]
print word[3:4]
print word[4:6] # select from index 4 to before 6
print word[4:]  # select from index 4 to end of word
print word[:2]  # select from beginning of word to before index 2
print word[:]   # select from beginning of word to end

s = 'audacity'
print 'U' + s[2:]

# Examplue using string function
import string
print string.capwords(s[1:])

s = 's'
print s[:]
print s + s[0:-1+1]
print s[0:]
print s[:-1]
print s[:3] + s[3:]

###############################################################################
## Finding Strings in Strings
#
# <string>.find(<string>)
#   - result is position index of first character of target string
#   - -1 if result not found
pythagoras = "There is geometry in the humming of the strings, there is \
              music in the spacing of the spheres."

print pythagoras.find('string')
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('sphere')
print pythagoras[pythagoras.find('sphere'):]
print pythagoras.find('algegra')

print s.find('')            # empty string is always found
print s.find(s + '!!!')+ 1

###############################################################################
## Finding the Numbers
#
# Using find with 2nd parameter
#
# <string>.find(<string>,<number>)
#   - number that gives first position in search string where the target 
#     string appears [at or after <number>
#
danton = "De l'audace, encore de l'audace, toujours de l'audace."
print danton.find('audace')
print danton.find('audace',0)
print danton.find('audace',5)
print danton.find('audace',6)
print danton[6:]
print danton[25:]
print danton.find('audace',26)
print danton[47:]
print danton.find('audace',48)

###############################################################################
## Extracting Links 
# 
# Match '<a href="<url>" to find link
#
import urllib2
response = urllib2.urlopen('http://xkcd.com/353/')
page = response.read()
print page
next_link = '<a href='
start_link = page.find(next_link)
end_link = page.find('"',start_link+9)
print "start_link: " + str(start_link) + ", end_link: " + str(end_link)
url = page[start_link+9:end_link]
print url

## Option 2
start_link = page.find(next_link)
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print url

###############################################################################




