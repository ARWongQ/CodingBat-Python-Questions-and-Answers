#1
'''
@parameters
a= int
b= int
negative = boolean
'''
def pos_neg(a, b, negative):
  #check if negative
  if(negative):
    #return true if both numbers are negative
    return (a < 0) and (b < 0)
    
  else:
    #check if a is positive and b is negative
    if( a > 0) and (b < 0):
      return True
    
    #check if a is negative and b is positive
    elif( a < 0) and (b > 0):
      return True
    #return False is neither case was achieved
    else:
      return False

#2
'''
@parameters
str = string
'''
def not_string(str):
  #check if the first 3 letter of the given string is "not"
  if( str[:3] == "not"):
    return str
  #else add "not"
  else:
    return "not " + str

#3
'''
@parameters
str = string
n = chracter to be removed
'''
def missing_char(str, n):
  #length of the string
  str_length = len(str)
  #letter to be removed
  removing = str[n]
  #remove it
  removed= str.replace(removing,"")
  
  return removed

#4
'''
@parameters
str = string
'''
def front_back(str):
  #length of the string
  str_length = len(str)
  #if the string is empty of has only one letter (to not go off the array)
  if(str_length <= 1):
    return str
    
  else:
    #Get the first letter
    first_letter= str[0]
    #Get the last letter
    last_letter = str[str_length - 1]
    #Get the middle letters of the strings
    middle = str[1:str_length -1]
    
    #return the string with last and first letter flipped
    return last_letter + middle + first_letter

#5
'''
@parameters
str = string
'''
def front3(str):
  #length of the string
  str_length = len(str)
  #Check if the length less than 3 
  if(str_length < 3):
    #Store the front of the str
    first_letters = str[0:str_length]
    #loop twice to add the front_letters
    for i in range(0,2):
      str += first_letters
      
    return str
  else:
    #get the front of the letter
    first_letter= str[0:3]
    #variable to store the answer
    new = ""
    #loop three times to add the front_letters
    for i in range(0,3):
      new += first_letter

    return new

  
#6
'''
@parameters
str = string
n = n copies
'''
def string_times(str, n):
  #variable to store the new sring
  new= ""
  #if empty return empty string
  if(n == 0):
    return "";
    
  else:
    #loop n times to and add to thenew string
    for i in range(0,n):
      new += str
    
  return new

#7
'''
@parameters
str = string
n = number of times to copy the front
'''
def front_times(str, n):
  #variable to store the answer
  new = ""
  #length of the string
  str_length = len(str)
  
  #Check if the length is less than 3 (to not go off the array)
  if(str_length < 3):
    #loop n times to add front
    for i in range(0,n):
      new += str
  else:
    #get the first letters of the string 
    first_letters = str[0:3]
    #loop n times and add the front
    for i in range(0,n):
      new += first_letters

  return new

#8
'''
@parameters
str = sring
'''
def string_bits(str):
  #variable to store the answer
  new = ""
  #length of the string
  str_length = len(str)
  #if the given sring is non-empty
  if(str_length > 0):
    #loop in counts of two and add the indexed letter
    for i in range(0,str_length, 2):
      new += str[i]
  return new

#9
'''
@parameters
str = string
'''
def string_splosion(str):
  #variable to store the answer 
  new = ""
  #get the length of the string
  str_length = len(str)
  
  #loop length+1 and add the array of indexes
  for i in range(0,str_length+1):
    new += str[0:i]
  return new

#10
'''
@parameters
nums = array of numbers
'''
def array_count9(nums):
  #length of the array
  length = len(nums)
  #variable to store the answer
  count = 0
  #loop through the whole array
  for i in range(length):
    #if the current index is 9 add to the count
    if(nums[i] == 9):
      count += 1

  return count

#11
'''
@parameters
nums = array of numbers
'''
def array_front9(nums):
  #flag if there is a 9 at the beginning
  Flag_9 = False
  #get the length of the array
  length = len(nums)
  #If the length is greater than 4
  if(length > 4):
    #change the number of times we need to iterate
    length = 4
  #loop 4 times to se if there is a 9 in the array 
  for i in range(length):
    #if found return true
    if(nums[i] == 9):
      Flag_9 = True
      return Flag_9
  #if not found return false
  return Flag_9

