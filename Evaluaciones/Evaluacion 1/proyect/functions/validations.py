def val_in_sis(num,sis):
    hexa=["0","1", "2", "3", "4", "5", "6", "7", "8", "9","a","b","c","d","e","f","A","B","C","D","E","F"]
    deci=["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    octa=["0","1", "2", "3", "4", "5", "6", "7"]
    cuat=["0","1", "2", "3"]
    tres=["0","1", "2", "3"]
    bina=["0","1"]

    list_num=list(num)
    
    if sis=="Hexadecimal":
        for i in list_num:
            if not(i in hexa):
                return False
        return True            
    
    elif sis=="Decimal":
        for i in list_num:
            if not(i in deci):
                return False
        return True    
    
    elif sis=="Octal":
        for i in list_num:
            if not(i in octa):
                return False
        return True    
    elif sis=="4":
        for i in list_num:
            if not(i in cuat):
                return False
        return True    
    elif sis=="3":
        for i in list_num:
            if not(i in tres):
                return False
        return True    
    elif sis=="Binario":
        for i in list_num:
            if not(i in bina):
                return False
        return True    

def ter(n: int):
    if n < 0:
        pass

    else:
        result = ""
        while n > 0:
            remainder = n % 3
            result = str(remainder) + result
            n //= 3

        return result

def cua(n: int):
    if n < 0:
        pass
    else:
        result = ""
        while n > 0:
            remainder = n % 4
            result = str(remainder) + result
            n //= 4

        return result