
''' [{{{{{{{{{{{{{{{{   WORKING  }}}}}}}}}}}}}}}}]     '''
#METHOD 1: 
def is_leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

#METHOD 2:

def is_leap(year):
    if(year%4==0 and year%100!=0):  
        return True
    elif(year%400==0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))



''' [{{{{{{{{{{{{{{{{   NOT WORKING  }}}}}}}}}}}}}}}}]
def is_leap(year):
    if year%4==0:
        return True
    elif(year%100==0):
        return False
    elif(year%400==0):
        return True
    

year = int(input())
print(is_leap(year))


if (year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
    
    '''