print("__Vernam Cipher__")

def encrypt(plaintxt,key):
    add=[]
    for i in range(len(key)):
        if len(key)==len(plaintxt):
            k= (ord(key[i])+ord(plaintxt[i]))%65
            add.append(k)
        else:
            print("Error- The length of Plain Txt and Key must be same")

    sub=''
    for i in range(len(add)):
        if add[i]>26:
            sub += chr(add[i]-26+65)
        else:
            sub +=chr(add[i]+65)
    
    print("Encrypted Cipher txt : ",sub)

def decrypt(encryptxt,key):
    sub=[]
    for i in range(len(key)):
        if len(key)==len(encryptxt):
            k= ord(encryptxt[i])-ord(key[i])
            sub.append(k)
        else:
            print("Error- The length of Encrypted Txt and Key must be same")
   
    add=''
    for i in range(len(sub)):
        if sub[i]<0:
            add += chr(sub[i]+26+65)
        else:
            add +=chr(sub[i]+65)
    
    print("Original Txt : ",add)
    

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption \n 3.Exit \n Enter your choice : "))
    if choice==1:
        plaintxt = input("Enter the Plain txt: ")
        plaintxt = plaintxt.replace(" ", "")
        plaintxt = plaintxt.upper()
        key = input("Enter the Key: ")
        key = key.replace(" ", "")
        key = key.upper()
        encrypt(plaintxt,key) 
        
        
    elif choice==2:
        encryptxt = input("Enter the Encrypted txt: ")
        encryptxt = encryptxt.replace(" ", "")
        encryptxt = encryptxt.upper()
        key = input("Enter the Key: ")
        key = key.replace(" ", "")
        key = key.upper()
        decrypt(encryptxt,key) 
       
    
    elif choice==3:
        break
    
    else:
        print("Choose correct choice")