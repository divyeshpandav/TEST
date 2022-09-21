import decimal
def INR_Convert(n):
    d = decimal.Decimal(str(n))  #string to decimal number
    if d.as_tuple().exponent < -2:
        s = str(n)
    else:
        s = '{0:.1f}'.format(n)
    l = len(s) #check string lentgh
    i = l - 1
    res, flag, k = '', 0, 0 #for use of formation number
    while i >= 0:
        if flag == 0:
            res += s[i]
            if s[i] == '.':
                flag = 1
        elif flag == 1:
            k += 1
            res += s[i]
            if k == 3 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        else:
            k += 1
            res += s[i]
            if k == 2 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        i -= 1
    return res[::-1]

print(INR_Convert(504678))
