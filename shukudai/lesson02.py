###############################################################################
## 
##  Lesson 2-2
##  Motivating Procedures
##
###############################################################################

############################################################################### 
##
##  Lesson 2-3
##  Introducting Procedures
##
############################################################################### 

#  syntax:
#  def <name> (<parameters>):      <name>,<name>, ...
#      <block>

############################################################################### 
##
##  Lesson 2-4..6
##  Quiz - Procedure Code, Output, Return Statement
##
############################################################################### 

def get_next_target(s)
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[start_quote + 1:end_quote]
    return url, end_quote


