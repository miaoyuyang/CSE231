

import string
word = string.ascii_lowercase 
ciphertext = ""   
answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")

while answer.upper() != 'Q':
        k = input("Please enter a keyword: ")
        k_l = k.lower() 

        while len(k_l) > 26 or not k_l.isalpha():
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            k = input("Please enter a keyword: ")
            k_l = k.lower()
        for i in k_l:
            if i not in ciphertext:
                ciphertext += i
        for t in word:
            if t not in ciphertext:
                ciphertext += t

        if answer.upper()=='E':
            m = input("Enter your message: ")
            m_l = m.lower()
            y = ""
            for i in m_l:
                if i.isalpha() == True:
                    n = word.find(i)
                    x = ciphertext[(n*5+8)%26]
                    y += x   
                else:
                    y += i
            print("your encoded message: ", y)
        
        if answer.upper()=='D':
            m_d = input("Enter your message: ")
            m_d = m_d.lower()
            q = ""
            for p in m_d:
                if p.isalpha() == True:
                    o = ciphertext.find(p)
                    r = 1
                    v = (o + r*26) - 8
                    while v%5 != 0:
                        r +=1
                        v = (o + r*26) - 8
                    z = word[int(v/5)]
                    q += z
                else:
                    q += p
            print("your decoded message: ", q)
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
        
else:
    print("See you again soon!")