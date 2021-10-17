print("__VIGENERE CIPHER__")

def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("". join(key)) 
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26 
    encrypt_text.append(chr(x+65)) 
  return("" . join(encrypt_text)) 

def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    orig_text.append(chr(x+65)) 
  return("" . join(orig_text)) 


while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption \n 3.Exit \n Enter your choice : "))
    if choice==1:
        string = input("Enter the Plain txt: ")
        string = string.replace(" ", "")
        string = string.upper()
        keyword = input("Enter the Key: ")
        keyword = keyword.replace(" ", "")
        keyword = keyword.upper()
        key = generateKey(string, keyword) 
        encrypt_text = encryption(string,key) 
        print("Encrypted Txt:", encrypt_text) 
        
    elif choice==2:
        string = input("Enter the Encrypted txt: ")
        string = string.replace(" ", "")
        string = string.upper()
        keyword = input("Enter the Key: ")
        keyword = keyword.replace(" ", "")
        keyword = keyword.upper()
        key = generateKey(string, keyword) 
        decryp_text = decryption(string,key) 
        print("Decrypted Txt:", decryp_text) 
    
    elif choice==3:
        break
    
    else:
        print("Choose correct choice")