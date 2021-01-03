# cook your dish here
def binaryToDecimal(b):
    return int(b,2)
def EncodedString():
    mapping={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p'}
    try:
        T=int(input())
        while(T):
            n=int(input())
            s=input()
            res=''
            for i in range(0,len(s),4):
                btd=binaryToDecimal(s[i:i+4])
                res=res+mapping[btd]
            print(res)
            T-=1
    except:
        pass
EncodedString()
        