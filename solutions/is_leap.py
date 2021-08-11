def is_leap(year):
    
    first = year % 4 == 0 
    second = year % 100 == 0
    third = year % 400 == 0
    
    if first:
        if second:
            if third:
                return True
            return False
        return True
    return False