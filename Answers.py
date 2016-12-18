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

#12
'''
@parameters
nums = array of numbers
'''
def array123(nums):
  #Get the length of the array
  length = len(nums)
  #loop length-2 times (to not get off the array)
  for i in range(length-2):
    #check if the sequence is in the array
    if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
      return True

  return False

#13
'''
@parameters
a = string
b = string
'''
def string_match(a, b):
  #Get the length of the two given strings
  length_a = len(a)
  length_b = len(b)
  #Get the smallest string
  min_length = min(length_b, length_a)
  #Keep track of the # of times they contain the same length 2 substring
  count = 0
  #Check if length is less than 2
  if(min_length < 2):
    return count

  else:
    #loop length-1 (to not go off the array)
    for i in range(min_length-1):
      #check if the length 2 substring are the same (if so add 1 to count)
      if(a[i] == b[i] and a[i+1] == b[i+1]):
        count += 1

  return count

#14
'''
@parameters
name = string
'''
def hello_name(name):
  #create greeting
  greeting= "Hello " + name + "!"
  return greeting

#15
'''
@parameters
a = string
b = string
'''
def make_abba(a, b):
  #concatenate the words in the proper abba order
  combined= a + b + b + a
  return combined

#16
'''
@parameters
tag = string
word = string
'''
def make_tags(tag, word):
  #Create the beginning tag
  HTML_tag_1= "<" + tag + ">"
  #Create the end tag
  HTML_tag_2= "</" + tag + ">"
  
  #Concatenate in proper order
  HTML_string = HTML_tag_1 + word + HTML_tag_2

  return HTML_string

#17
'''
@parameters
out = string
word = string
'''
def make_out_word(out, word):
  #Break the out word in half
  out_b = out[0:2]
  out_e = out[2:4]
  
  #Concatenate in proper order (sandwich)
  combined= out_b + word + out_e

  return combined

#18
'''
@parameters
str = string
'''
def extra_end(str):
  #Get the proper lengths 
  length = len(str)
  prev_len = length - 2
  #Get the last 2 characters
  last_c = str[prev_len:length]
  #Variable to hold the answer
  new = ""
  #loop 3 times to concatenate the last characters
  for i in range(3):
    new += last_c

  return new

#19
'''
@parameters
str = string
'''
def first_two(str):
  #Get the length of strings
  length = len(str)
  end= 2
  #Check if the length is smaller than two (to not go off the array 
  if(length < 2):
    n = length
  #get the first end characters of the string
  first = str[0:end]

  return first
  
    
#20
'''
@parameters
str = string
'''
def first_half(str):
  #Get the length of the string
  length = len(str)
  #Return the first half of the given string
  return str[0:length/2]

#21
'''
@parameters
str = string
'''
def without_end(str):
  #get the length of the string
  length = len(str)
  #variable to hold the answer
  new= ""
  #check if length is smaller than 2 
  if(length <= 2):
    return new
  
  else:
    #save the middle characters of the given string
    middle = str[1:length-1]

  return middle
    
#22
'''
@parameters
a = string
b = string
'''
def combo_string(a, b):
  #Get the lengths of the two given strings
  length_a = len(a)
  length_b = len(b)
  #if a is bigger do bab
  if(length_a >= length_b):
    return b + a + b
  else:
    #if b is bigger do aba
    return a + b + a

#23
'''
@parameters
a = string
b = string
'''
def non_start(a, b):
  #Get the lengths of the two hiven strings
  length_a = len(a)
  length_b = len(b)
  #remove the first characters of each string 
  new_a = a[1:length_a]
  new_b = b[1:length_b]
  #concatenate the words
  combined = new_a + new_b

  return combined

#24
'''
@parameters
str = string
'''
def left2(str):
  #get the length of the string
  length = len(str)
  #Check if less than or equal to 2
  if(length <= 2):
    return str

  else:
    #Get the first two characters 
    beg = str[0:2]
    #Get the remaining of the string
    rem = str[2:length]
    
    #Concatenate remaining and beginning
    combined = rem + beg

    return combined
    

