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
  
  
