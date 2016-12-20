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


#25
def first_last6(nums):
  #Get the length of the array
  length = len(nums)
  #Check if the beginning or end of the array is 6
  if(nums[0] == 6 or nums[length-1] == 6):
    return True
  return False

#26
def same_first_last(nums):
  #Get the length of the array 
  length = len(nums)
  #Check if the array is not empty and the beg and end are equal
  if(length > 0 and nums[0] == nums[length-1]):
    return True
  return False

#27
def make_pi():
  #Creater and return the array
  pi = [3,1,4]
  return pi

#28
def common_end(a, b):
  #Get the lengths of the two given arrays
  length_a = len(a)
  length_b = len(b)
  #check if the first or last elements are equal
  if(a[0] == b[0] or a[length_a-1] == b[length_b-1]):
    return True
  return False

#29
def sum3(nums):
  #get the lnegth of the array
  length = len(nums)
  #Variable to store the sum
  sum = 0
  #loop through the whole array and add the numbers to sum
  for i in range(length):
    sum += nums[i]

  return sum

#30
def rotate_left3(nums):
  #Get the length of the array
  length = len(nums)
  #loop length - 1 (to not go off the array)
  for i in range(length-1):
    #save the current value
    temp = nums[i]
    #swap
    nums[i] = nums[i+1]
    #Insert temp
    nums[i+1] = temp

  return nums

#31
def reverse3(nums):
  #get the length of the array
  length = len(nums)
  #save the current value
  temp = nums[0]
  #swap
  nums[0] = nums[length-1]
  #Insert temp
  nums[length-1] = temp
  
  return nums

#32
#This methodology works from beginning to middle and from end to middle swapping the values (middle won't swap)
def reverse_array(nums):
  #Get the length of the array
  length = len(nums)
  loop = length//2
  #loop half the length (to not do unecessary looping) (middle wont change place)
  for i in range(loop):
    #save the current value
    temp = nums[i]
    #swap
    nums[i] = nums[length-1]
    #Insert temp
    nums[length-1] = temp
    #reduce length to move from end to middle 
    length -= 1
    
  return nums

#33
def max_end3(nums):
  #Get the length
  length = len(nums)
  #Check which one is greater
  max_value = max(nums[0],nums[length-1])
  #loop to change all variables with the max_value
  for i in range(length):
    nums[i] = max_value

  return nums

#34
def sum2(nums):
  #Get the length
  length = len(nums)
  #Variable for iterations 
  loop = 2
  sum = 0
  #If length is smaller than 2, loop length times
  if(length < 2):
    loop = length
  #loop and add the numbers
  for i in range(loop):
    sum += nums[i]

  return sum

#35
def middle_way(a, b):
  #Get the lengths of a and b
  length_a = len(a)
  length_b = len(b)
  #Get the middle int form a and b
  mid_a = a[length_a // 2]
  mid_b = b[length_b // 2]
  #Set them in an array
  mid_a_b = [mid_a,mid_b]

  return mid_a_b

#36
def make_ends(nums):
  #Get the length
  length = len(nums)
  #Get the variables from the beginning and end
  beg = nums[0]
  end = nums[length-1]
  #Set them in an array
  answer = [beg,end]

  return answer

#37
def has23(nums):
  #Get the length
  length = len(nums)
  #loop length times
  for i in range(length):
    #Check if the array has 2 or 3 
    if(nums[i] == 2 or nums[i] == 3):
      return True

  return False

#38
def cigar_party(cigars, is_weekend):
  #Check if the cigars are between 40 and 60 and is not a weekend
  if(cigars >= 40 and cigars <= 60 and (not is_weekend)):
    return True
  #Check if it is a weekend and they have more than 40 cigars
  elif(is_weekend and cigars >= 40):
    return True
  else:
    return False
  
#39
def date_fashion(you, date):
  #Get the smaller number
  smaller = min(you,date)
  #Check if either is equal or greater than 8
  if(you >= 8 or date >=8):
    #Check if the smallest is smaller or equal than 2
    if(smaller <= 2):
      return 0
    return 2   
  #Check if either is less than or equal to 2
  elif(you <= 2 or date <= 2):
    return 0
  else:
    return 1

#40
def squirrel_play(temp, is_summer):
  #Max temperature
  max = 90
  #Check if its summer and therefore increase the max temperature
  if(is_summer == True):
    max = 100
   #Check if the temp is between 60 or max
  if(temp >= 60 and temp <= max):
    return True
  else:
    return False

#41
def caught_speeding(speed, is_birthday):
  #Variable depending on your birthday
  birth_d = 0
  #Check if it is your birthday if so add 5 to all the speed constrains
  if(is_birthday == True):
    birth_d = 5
  #Check if it is smaller 60 (+5 if birthday)
  if(speed <= 60+birth_d):
    return 0
  #Check if 61 and 80 (+5 if birthday)
  elif(speed >= 61+birth_d and speed <= 80+birth_d):
    return 1

  else:
    return 2

#42
def sorta_sum(a, b):
  #Get the sum
  sum = a + b
  #Check if the sum is between 10 and 19
  if(sum >= 10 and sum <= 19):
    return 20
  else:
    return sum

#43
def alarm_clock(day, vacation):
  #Variables for each clock time
  alarm_7 = "7:00"
  alarm_10 = "10:00"
  alarm_off = "off"
  #Check if it is a weekday and is not vacation
  if(day >= 1 and day <= 5 and not vacation):
    return alarm_7
  #Check if it is a weekend and is vacation
  elif( (day == 0 or day == 6) and vacation):
    return alarm_off
  
  else:
    return alarm_10
    
#44
def love6(a, b):
  #Get the sum
  sum = a+b
  #Get the difference
  difference = abs(a - b)
  #Check if either the numbers, sum or difference is 6
  if(a == 6 or b == 6 or sum == 6 or difference == 6):
    return True
  else:
    return False

#45
def in1to10(n, outside_mode):
  #Check Inside boundaries (False)
  if(outside_mode == False):
    if(n >= 1 and n <= 10):
      return True
    else:
      return False
  else:
    #Check Outside boundaries (True)
    if(n <= 1 or n >= 10):
      return True
    else:
      return False

#46
def near_ten(num):
  #Get the remainder (Mod)
  remainder = num % 10
  #Check if it is within 2
  if(remainder <= 2 or remainder >= 8):
    return True
  else:
    return False

