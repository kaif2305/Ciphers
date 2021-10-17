print("__Playfair Cipher__")

key = input("Enter the key : ")
key = key.replace(" ","")
key = key.upper()

result=[]

for i in key:
    if i not in result:
        if i=='J':
            result.append('I')
        else:
            result.append(i)

for j in range(65,91):
    if chr(j) not in result:
        if j==74 and chr(73) in result:
            pass
        else:
            result.append(chr(j))       


matrix=[]
k=0
for i in range(5):
    a=[]
    for j in range (5):
        a.append(result[k])
        k+=1
    matrix.append(a)
for i in range(5):
    for j in range(5):
        print(matrix[i][j], end = " ")
    print()

def locindex(c):
    loc=[]
    if c=='J':
        c='I'
    for i ,j in enumerate(matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():
    msg = input("Enter the Plain Txt : ")
    msg = msg.upper()
    msg = msg.replace(" ", "")
    for s in range(0,len(msg),2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg = msg[:s+1]+'X'+msg[s+1:]
    if (msg[len(msg)-1]==msg[len(msg)-2]):
            msg = msg[:]+'X'    
    print("After Split : ", msg)
    print("Cipher Txt :",end='')
    
    for i in range(0,len(msg),2):
        loc1=[]
        loc1=locindex(msg[i])
        loc2=[]
        loc2=locindex(msg[i+1])
        if loc1[1]==loc2[1]:
            print( matrix[(loc1[0]+1)%5][loc1[1]]+matrix[(loc2[0]+1)%5][loc2[1]], end='')
        elif loc1[0]==loc2[0]:
            print( matrix[(loc1[1]+1)%5][loc1[0]]+matrix[(loc2[1]+1)%5][loc2[0]], end ='')
        else:
            print( matrix[loc1[0]][loc2[1]]+matrix[loc2[0]][loc1[1]], end ='')
    
def decrypt():
    msg = input("Enter the Cipher Txt : ")
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("Plain Txt :",end='')
    
    for i in range(0,len(msg),2):
        loc1=[]
        loc1=locindex(msg[i])
        loc2=[]
        loc2=locindex(msg[i+1])
        if loc1[1]==loc2[1]:
            print( matrix[(loc1[0]-1)%5][loc1[1]]+matrix[(loc2[0]-1)%5][loc2[1]], end='')
        elif loc1[0]==loc2[0]:
            print( matrix[(loc1[1]-1)%5][loc1[0]]+matrix[(loc2[1]-1)%5][loc2[0]], end ='')
        else:
            print( matrix[loc1[0]][loc2[1]]+matrix[loc2[0]][loc1[1]], end ='')

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption \n 3.Exit \n Enter your choice : "))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        break
    else:
        print("Choose correct choice")