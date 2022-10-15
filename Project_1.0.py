    #Python Project 
#Vigenere Cipher

print("This is Vingere cipher")

alp = 'abcdefghijklmnopqrstuvwxyz'



def startingPoint():
    ans = input("Do you want encode or decode? Choose: (en/de)")
    if ans == 'en':
        encode()
    elif ans == 'de':
        decode()
    else:
        print("Please,choose correctly!")
        startingPoint()


def decode():
    while True:
        plaintxt = input("Please, Write encrypted text for decoding? :")
        
        if not plaintxt.isalpha():
            print('Enter only letters to decode your message')
            continue
        else:
            print(plaintxt)
            #decoding function()
            break        
        
        
def encode():
    while True:
        plaintxt = input("Please, Write your Plain text for encoding? :")
        key = input("Enter a key: ")
        if not plaintxt.isalpha() or not key.isalpha():
            print('Enter only letters for both inputs to encode your message')
            continue
        else:
            chooseMethod(plaintxt,key)
            break
    
def chooseMethod(message,key):
    method = input("Choose method to encode your data: String, List, Tuple.(1/2/3)")

    met = int(method)

    if met == 1:
        encodeWithString(message,key)
        
    elif met == 2:
        encodeWithList(message,key)
        
    elif met == 3:
        encodeWithTuple(message,key)
        
    else:
        print("Enter only one and right method.(1 or 2 or 3)")
        chooseMethod()


##########################  STRING method STARTS here ############################

def encodeWithString(message,key):
    print("Encoding with String function and with '{}' Key...".format(key))
    
    newkey = generateKey(message,key)
    print("Result: " + MainStringCipher(message,newkey))
    
    
def generateKey(value,key):
    add2key = len(value) - len(key)
    counter = 0
    for i in range(add2key):
        key += key[counter]
        counter += 1
        if counter == 3:
            counter = 0 
    return key  

                
def MainStringCipher(val,k):
    ans = ''
    tempVal = 0
    tempKey = 0
    tempValIndex = 0
    tempKeyIndex = 0
    for j in range(len(val)):
        for i in range(len(alp)):
            
            if val[j] == alp[i]:
                tempVal += 1
                tempValIndex = i
                
            if (k[j]) == alp[i]:
                tempKey += 1
                tempKeyIndex = i
        if tempVal == tempKey and tempVal != 0:
            for i in range(len(alp)):
                if (tempValIndex + tempKeyIndex)%26 == i:
                    ans += alp[i]
    return ans

##########################  STRING method ENDS here ############################
    


##########################  LIST method STARTS here ############################
def encodeWithList(message,key):
    print("encoding with List function...")
##########################  LIST method ENDS here ############################
    








##########################  TUPLE method STARTS here ############################
def encodeWithTuple(message,key):
    print("encoding with Tuple function...")
##########################  TUPLE method STARTS here ############################



startingPoint()







