import secrets
import requests
def dissolveQbits(ids, length):
    print("                                 AT BOB")
    '''print("\n")'''
    print("Polarised states received by Bob are:")
    print(ids)
    polar=[secrets.choice(["+","X"]) for i in range(length)]
    print("\n")
    print("Basises took by Bob to measure Alice's Photons are:")
    print(polar)
    print("\n")
    print("Measuring Alice Polarised States using Basis taken:")
    print(list(zip(ids,polar)))
    print("\n")
    k=0
    bit=[]
    b=[]
    while k<length:
        if ids[k]=="/" and polar[k]=="X":
            bit.append(1)
            b.append("/")
            k+=1
        elif ids[k]=="/" and polar[k]=="+":
            bit.append(secrets.choice([0,1]))
            b.append(secrets.choice(["-","|"]))
            k+=1
        elif ids[k]=="I" and polar[k]=="X":
            bit.append(0)
            b.append("I")
            k+=1
        elif ids[k]=="I" and polar[k]=="+":
            bit.append(secrets.choice([0,1]))
            b.append(secrets.choice(["-","|"]))
            k+=1
        elif ids[k]=="-" and polar[k]=="+":
            bit.append(0)
            b.append("-")
            k+=1
        elif ids[k]=="-" and polar[k]=="X":
            bit.append(secrets.choice([0,1]))
            b.append(secrets.choice(["/","I"]))
            k+=1
        elif ids[k]=="|" and polar[k]=="+":
            bit.append(1)
            b.append("|")
            k+=1
        elif ids[k]=="|" and polar[k]=="X":
            bit.append(secrets.choice([0,1]))
            b.append(secrets.choice(["/","I"]))
            k+=1
    return bit, b,polar

def requestQbits(length):
    
    bits=[ secrets.choice([1,0]) for i in range(length) ]
    '''print("\n")'''
    print("                                 AT ALICE")
    '''print("\n")'''
    print("Bits taken by alice according to which it will polarise the photons:")
    print(bits)
    print("\n")
    polar=[secrets.choice(["+","X"]) for i in range(length)]
    print("Basises took by Alice to Polarise it's Photons are:")
    print(polar)
    '''polarf1=[i*45 for i in polar]'''
    k=0
    state=[]
    while k<length:
        if bits[k]==1 and polar[k]=="X":
            state.append("/")
            k+=1
        elif bits[k]==1 and polar[k]=="+":
            state.append("|")
            k+=1
        elif bits[k]==0 and polar[k]=="X":
            state.append("I")
            k+=1
        else:
            state.append("-")
            k+=1
                         
    print("\n")
    print("Polarised States obtained after polarising Alice's Photons are")
    print(state)
    print("\n")
    print("Sending Polarised States to BOB")
    '''print(list(zip(bits,polarf1)))'''
    print("\n")
    return bits,state, polar
def eve(ids,length):
    n=length
    bit=[]
    e=[]
    polar=[secrets.choice(["+","X"]) for i in range(length)]
    k=0
    bit=[]
    while k<length:
        if ids[k]=="/" and polar[k]=="X":
            bit.append(1)
            e.append("/")
            k+=1
        elif ids[k]=="/" and polar[k]=="+":
            bit.append(secrets.choice([0,1]))
            e.append(secrets.choice(["-","|"]))
            k+=1
        elif ids[k]=="I" and polar[k]=="X":
            bit.append(0)
            e.append("I")
            k+=1
        elif ids[k]=="I" and polar[k]=="+":
            bit.append(secrets.choice([0,1]))
            e.append(secrets.choice(["-","|"]))
            k+=1
        elif ids[k]=="-" and polar[k]=="+":
            bit.append(0)
            e.append("-")
            k+=1
        elif ids[k]=="-" and polar[k]=="X":
            bit.append(secrets.choice([0,1]))
            e.append(secrets.choice(["/","I"]))
            k+=1
        elif ids[k]=="|" and polar[k]=="+":
            bit.append(1)
            e.append("|")
            k+=1
        elif ids[k]=="|" and polar[k]=="X":
            bit.append(secrets.choice([0,1]))
            e.append(secrets.choice(["/","I"]))
            k+=1
    return e
    
diff = lambda a, b: [  i == j for i, j in zip(a, b) ]
discard = lambda sequence, diff: list(
    filter(
        lambda i:  i in [0, 1], 
        [ i if same else None for i, same in zip(sequence, diff) ]
    )
)
