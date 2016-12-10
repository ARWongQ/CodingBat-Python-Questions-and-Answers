#1
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
