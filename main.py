import secrets
'''d=int(input("Enter the Block Size in bits:  "))'''
d=128
bl=d/8
bl=int(bl)
print("Select the size of n around",2*d)
n = int(input("Enter The Size of n: "))
h=int(input("\nWithout Eve Enter 1 \n With Eve Enter 2\n"))
if (h==1):
    import bb84
    bits_alice,states_alice, palice = bb84.requestQbits(n)
    ids=[]
    bits_bob, states_bob, pbob = bb84.dissolveQbits(states_alice,n)
    diff = bb84.diff(palice, pbob)
    kalice = bb84.discard(bits_alice, diff)
    kbob = bb84.discard(bits_bob, diff)
    l=len(kalice)
    while l>d:
        import os
        os.system("cls")
        import bb84
        bits_alice,states_alice, palice = bb84.requestQbits(n)
        ids=[]
        bits_bob, states_bob, pbob = bb84.dissolveQbits(states_alice,n)
        diff = bb84.diff(palice, pbob)
        kalice = bb84.discard(bits_alice, diff)
        kbob = bb84.discard(bits_bob, diff)
        l=len(kalice)
    
    a=[]
    b=[]
    k=0
    while k<n:
        if diff[k] == True:
            a.append(states_alice[k])
            b.append(states_bob[k])
            k+=1
        else:
            k+=1
    print("Alice and Bob Exchanging their Basises with each other")
    print("Alice and Bob Comparing their Basises with Basises got from other end")
    print("\nPolarised States left at Alice after comparision of Basises are ")
    print(a)
    print("\nPolarised States left at Bob after comparision of Basises are: ")
    print(b)
    print(" \nConsidering Polarised States (-,I) as bit 0\n\t    Polarised States (|,/) as bit 1\nSo,")
    import numpy as np
    a=np.array(kalice)
    b=np.array(kbob)
    print("Alice's Key: \n",a)
    print("Bob's Key:   \n",b)
    a1= int("".join(str(x) for x in kalice),2)
    a2= hex(a1)[2:1000]
    print("\n")
    print("Alice's Key in Hex Form:    ",a2)
    b1=int("".join(str(x) for x in kbob),2)
    b2= hex(b1)[2:1000]
    print("Bob's Key in Hex Form:      ",b2)
    print("\n")
    m1=[]
    m2=[]
    m1=kalice[0:32]
    m2=kbob[0:32]
    a10= int("".join(str(x) for x in m1),2)
    a11= hex(a10)[2:1000]
    b10= int("".join(str(x) for x in m2),2)
    b11= hex(b10)[2:1000]
    h1=hash(a11)
    h2=hash(b11)
    print(h1)
    print(h2)
    if h1==h2:
        print("Eve Was not Present")
    eff=1-(l/n)
    print("Efficiency is:",round(eff*100,2),"%")
    l=len(kalice)
    print(l)
    if(l<128):
        i=128-l
        while i>0:
            x=secrets.choice([0,1])
            kalice.append(x)
            kbob.append(x)
            i=i-1
            continue
    a3= int("".join(str(x) for x in kalice),2)
    a4= hex(a3)[2:1000]
    b3= int("".join(str(x) for x in kbob),2)
    b4= hex(b3)[2:1000]
    from tkinter import *
    import sys
    from Crypto.Cipher import AES
    import base64
    import os

    def encryption(privateInfo):
        
        BLOCK_SIZE = 16
        PADDING = '{'

        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        secret= a4
        print('Secret key: \n', a2)

        obj = AES.new(secret)
        encoded = EncodeAES(obj, privateInfo)
        cipher= encoded.decode('UTF-8')
        print('\nCipher Text:\n', cipher)
        '''print(len(privateInfo))
        print(len(a2))'''

    root = Tk()
    root.title("Encryption")
    widget = Label(root, text='AES Encryption \n(Enter Message Below)',font = ('Bold',20))
    widget.config(bg='Yellow', fg='Red')
    widget.config(height=3, width=30)
    widget.pack(expand=YES, fill=BOTH)

    def fetch():
        encryption("%s" % ent.get('1.0', END+'-1c'))




    ent = Text(root)
    ent.config(width=20, height=10)
    ent.pack(side=TOP, fill=X)
    ent.focus()
    ent.config(font=('courier', 15, 'normal'))



    widget = Button(text='Encrypt', padx=10, pady=10)
    widget.pack(padx=20, pady=20)
    widget.config(cursor='gumby')
    widget.config(bd=8, relief=RAISED)
    widget.config(bg='Black', fg='white')
    widget.config(font=('helvetica', 20, 'italic'))
    widget.config(command=fetch)

    class StdoutRedirector(object):

        def __init__(self, text_area):
            self.text_area = text_area

        def write(self, str):
            self.text_area.insert(END, str)
            self.text_area.see(END)



    text = Text()
    text.config(font=('courier', 15, 'normal'))
    text.config(width=20, height=10)
    text.pack(expand=YES, fill=BOTH)
    text.insert('1.0', 'Highlight and Ctrl+C To Copy\n\n')


    sys.stdout = StdoutRedirector(text)




    mainloop()
    root.mainloop()

    from tkinter import *
    from Crypto.Cipher import AES
    import sys
    import base64
    import codecs

    def decrypt(cipher):

        PADDING = '{'
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode('utf-8').rstrip(PADDING)
        try:
            obj2 = AES.new(b4)
            print("Bob's Key is:\n", b2)
            decoded = DecodeAES(obj2, cipher)
            print('\nSecret Message:\n', decoded)
        except:
            print("Error in decoding the secret message")

    root = Tk()
    root.title("Decryption")
    widget = Label(root, text='AES Decryption \n(Enter The Cipher Below)',font = ('Bold',20))
    widget.config(bg='Yellow', fg='Red')
    widget.config(height=3, width=30)
    widget.pack(expand=YES, fill=BOTH)



    ent = Text(root)
    ent.config(width=20, height=10)
    ent.pack(side=TOP, fill=X)
    ent.focus()
    ent.config(font=('courier', 15, 'normal'))




    '''text = Text()
    text.insert('1.0', 'Paste (Ctrl+V) Your Cipher Text Here \nAfter Deleting This Text')
    text.config(width=30, height=3)
    text.pack(expand=YES, fill=BOTH)'''


    def decryption():
        decrypt("%s" % ent.get('1.0', END+'-1c'))
        



    widget = Button(text='Decrypt', padx=10, pady=10)
    widget.pack(padx=20, pady=20)
    widget.config(cursor='gumby')
    widget.config(bd=8, relief=RAISED)
    widget.config(bg='Black', fg='white')
    widget.config(font=('helvetica', 20, 'italic'))
    widget.config(command=decryption)

    class StdoutRedirector(object):

        def __init__(self, text_area):
            self.text_area = text_area

        def write(self, str):
            self.text_area.insert(END, str)
            self.text_area.see(END)

        
    plain = Text()
    plain.config(font=('courier', 15, 'normal'))
    plain.config(width=30, height=12)
    plain.pack(expand=YES, fill=BOTH)


    sys.stdout = StdoutRedirector(plain)



    mainloop()
    root.mainloop()


else :
    import bb84
    bits_alice,states_alice, palice = bb84.requestQbits(n)
    states_eve=bb84.eve(states_alice,n)
    ids=[]
    bits_bob, states_bob, pbob = bb84.dissolveQbits(states_eve,n)
    diff = bb84.diff(palice, pbob)
    kalice = bb84.discard(bits_alice, diff)
    kbob = bb84.discard(bits_bob, diff)
               
    diff = bb84.diff(palice, pbob)
    kalice = bb84.discard(bits_alice, diff)
    kbob = bb84.discard(bits_bob, diff)
    '''import os
    os.system("cls")
    import numpy as np
    a=np.array(kalice)
    b=np.array(kbob)
    print(a)
    print(b)'''
    a=[]
    b=[]
    k=0
    while k<n:
        if diff[k] == True:
            a.append(states_alice[k])
            b.append(states_bob[k])
            k+=1
        else:
            k+=1
    print("\nPolarised States left at Alice after comparing Polarisers of both Alice And Bob are ")
    print(a)
    print("\nPolarised States left at Bob after comparing Polarisers of both Alice And Bob are: ")
    print(b)
    print(" \nConsidering Polarised States (-,I) as bit 0\n\t    Polarised States (|,/) as bit 1\nSo,")
    import numpy as np
    a=np.array(kalice)
    b=np.array(kbob)
    print("Alice's Key: \n",a)
    print("Bob's Key:   \n",b)
    a1= int("".join(str(x) for x in kalice),2)
    a2= hex(a1)[2:1000]
    print("\n")
    print("Alice's Key in Hex Form:    ",a2)
    b1=int("".join(str(x) for x in kbob),2)
    b2= hex(b1)[2:1000]
    print("Bob's Key in Hex Form:      ",b2)
    '''m1=[]
    m2=[]
    l1=int(len(kalice)/4)
    l2=int(len(kbob)/4)
    m1=kalice[0:32]
    m2=kbob[0:32]
    x=[1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1]
    l3=len(x)
    import numpy as np
    m=np.array(m1)
    n=np.array(m2)
    def hashe(a,x,l1,l2):
        
        l2=len(x)
        i=l1-l2
        while i>0:
            x.append(0)
            i=i-1
            continue
        p=np.array(x)
        f=a^p
        m=list(f)
        l=len(m)
        s=hash("".join(str(x) for x in m))
        return s

    h1= hashe(m,x,l1,l3)
    h2= hashe(n,x,l2,l3)
    print(h1)
    print(h2)
    if h1!=h2:
        print("Eve Was Detected")'''
    m1=[]
    m2=[]
    m1=kalice[0:32]
    m2=kbob[0:32]
    a10= int("".join(str(x) for x in m1),2)
    a11= hex(a10)[2:1000]
    b10= int("".join(str(x) for x in m2),2)
    b11= hex(b10)[2:1000]
    h1=hash(a2)
    h2=hash(b2)
    print(h1)
    print(h2)
    if h1!=h2:
        print("Eve Was Detected")
