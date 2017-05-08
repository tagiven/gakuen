# Problem Set 2
hours_per_day=24
days_per_week=7

print(7 * hours_per_day * days_per_week)

# Problem Set 4
speed_of_light = 299800000.  # m per s
nano_per_sec = 1000000000.  # 1 Billion
nanodistance = speed_of_light / nano_per_sec
print(nanodistance)

# Problem Set 6
s = 'udacity'
t = 'bodacious'
print(s[:1] + t[2:])

# Problem set 7
text = "first hoo"
print(text.find('hoo'))

# Problem set 8
text = "all zip files are zipped"

first_index = text.find('zip')
print(text.find('zip',first_index+1))

# Problem set 9

# Problem set 2.2
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow"

marker_index = line.find(marker)
replaced = line[:marker_index] + replacement + line[marker_index + len(marker):]
print(replaced)

# Problem Set 2.6
## Note: print(string backwards with following syntax
##       string[::-1]

word = "madam"
is_palindrome = word.find(word[::-1])
print(is_palindrome)
