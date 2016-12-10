#1
'''
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
str = string
n = chracter to be removed
'''
def missing_char(str, n):
  str_length = len(str)
  removing = str[n]
  removed= str.replace(removing,"")
  return removed

#4
def front_back(str):
  str_length = len(str)
  if(str_length <= 1):
    return str
    
  else:
    first_letter= str[0]
    last_letter = str[str_length - 1]
    middle = str[1:str_length -1]
    
    return last_letter + middle + first_letter

#5
def front3(str):
  str_length = len(str)
  if(str_length < 3):
    first_letters = str[0:str_length]

    for i in range(0,2):
      str += first_letters
    return str
    else:
      first_letter= str[0:3]
      new = ""
      for i in range(0,3):
          new += first_letter

      return new
