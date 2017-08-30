#!/usr/bin/env python

def lcd(n):
    t = " _   _ _     _  _ _  _  _ " 
    m = "| || _|_||_||_ |_  ||_||_|"  
    b=  "|_|||_ _|  | _||_| ||_| _|"
    w = [3, 1, 3, 2, 3, 3, 3, 2, 3, 3]
    pos = [sum(w[0:i[0]]) for i in enumerate(w)]
    pos.append(len(t))
    
    top = ''
    mid = '' 
    btm = ''

    while n>0:
        ctop = ''
        cmid = '' 
        cbtm = ''
        ch_begin = pos[n%10]
        ch_end = pos[(n%10) + 1]
        ctop += t[pos[n%10]:pos[(n%10)+1]]
        top = ctop + ' ' + top
        cmid += m[pos[n%10]:pos[(n%10)+1]]
        mid = cmid + ' ' + mid
        cbtm += b[pos[n%10]:pos[(n%10)+1]]
        btm = cbtm + ' '+ btm
        n = n/10    
    return top + '\n' + mid + '\n' + btm + '\n'

# for i in range(20):
#     print lcd(i)


print lcd(100)

