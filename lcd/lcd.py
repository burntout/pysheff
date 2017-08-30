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

    #  Case n = 0 
    if n == 0:
        ch_begin = 0
        ch_end = 1
        ch_begin = pos[n%10]
        ch_end = pos[(n%10) + 1]
        top = t[ch_begin:ch_end] + ' ' + top
        mid = m[ch_begin:ch_end] + ' ' + mid
        btm = b[ch_begin:ch_end] + ' ' + btm
    #  All other case n > 0
    else: 
        while n>0:
            ch_begin = pos[n%10]
            ch_end = pos[(n%10) + 1]
            top = t[ch_begin:ch_end] + ' ' + top
            mid = m[ch_begin:ch_end] + ' ' + mid
            btm = b[ch_begin:ch_end] + ' ' + btm
            n = n/10    
    return top + '\n' + mid + '\n' + btm + '\n'

for i in range(20):
    print lcd(i)


#print lcd(100)

