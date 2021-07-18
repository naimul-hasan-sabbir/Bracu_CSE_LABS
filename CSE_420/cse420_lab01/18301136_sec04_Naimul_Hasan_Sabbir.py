#openning input.txt file
with open('input.txt','r')as f:
#creating arrays of matching strings
    keywords=["int","float","double","if","else"]
    mathOperators=["+","-","*","/","="]
    logicalOperators=[">","<"]
    otherOperators=[",",";","{","}","(",")"]
    numericOperators=["0","1","2","3","4","5","6","7","8","9","."]

    keys=[]
    math=[]
    logical=[]
    others=[]
    numeric=[]
    identifier=[]

    def checkMatching(m):
        if m in keywords:
            keys.append(m)
            #print("keywords :",end=" ")
            #print(*keys,sep=",")
        elif m in mathOperators:
            math.append(m)
        elif m in logicalOperators:
            logical.append(m)
        elif m in otherOperators:
            others.append(m)
        #else:
            #try:
              #m=int(m)
        elif m in numericOperators:
            numeric.append(str(m))
            #except valueError:
        elif "." in m:
            if "." in numericOperators:
               numeric.append(str(m))
        else:
          identifier.append(m)


    for line in f:
        stringSplit=line.split()
        for m in stringSplit:
            checkMatching(m)

#removes duplicate items from list
math=list(dict.fromkeys(math))
keys=list(dict.fromkeys(keys))
logical=list(dict.fromkeys(logical))
others=list(dict.fromkeys(others))
identifier=list(dict.fromkeys(identifier))
#printng out
print("keywords :",end=" ")
print(*keys,sep=",")

print("Math operators :",end=" ")
print(*math,sep=",")

print("Logical Operators :",end=" ")
print(*logical,sep=",")

print("Others :",end=" ")
print(*others,sep=" ")

print("Numeric Values :",end=" ")
print(*numeric,sep=",")

print("identifiers :",end =" ")
print(*identifier,sep=",")
