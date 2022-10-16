    #Python Project 
#Vigenere Cipher

#WORKS ONLY WITH LOWER CASE LETTERS
import string

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
        plaintxt = input("Please, Write encrypted text for decoding? :")

        while True:
            askKey = input("Do you know key for decrypting your message?Enter (Yes/No): ")
            if askKey != "Yes" and askKey != 'No':
                print("Please,Enter only Yes or No!")
                continue  
            elif askKey == 'Yes':
                k = input("Please,Enter known key:")
                KnownKey(plaintxt,k)
                break
            elif askKey == 'No':
                UnknownKey(plaintxt)
                break
        
        
def KnownKey(message,key):
    print("Decoding with known key...") 
    mint = generateNums(message)
    kint = generateNums(generateKey(message,key))
    newTuple = ()            
    for i in range(len(mint)):
        newTuple += ((mint[i] - kint[i])%26,)
        
    answer = hackCipher(newTuple)
    ans = ''
    for i in range(len(answer)):
        ans += answer[i]
    
    print("Encrypted data = ",message)
    print("Key = ",key)
    print("Decrypted data = ",ans)  
    


def UnknownKey(x):
    print("Decoding with unknown key...")
    
    
    
    
       
def hackCipher(tup):
    baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    finalres = ()
    for j in range(len(tup)):
        for z in range(len(baseAlphabet)):
            if tup[j] == z:
                finalres += (baseAlphabet[z],)
    return finalres
       
    
def generateNums(string):
    baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    messageTuple =()
    
    for i in range(len(string)):
        for j in range(len(baseAlphabet)):
            if (string[i] == baseAlphabet[j]):
                messageTuple += (j,)
    return messageTuple


        
        
def encode():
    #while True:
        plaintxt = input("Please, Write your Plain text for encoding? :")
        key = input("Enter a key: ")
        chooseMethod(plaintxt,key)
        '''
        if not plaintxt.isalpha() or not key.isalpha():
            print('Enter only letters for both inputs to encode your message')
            continue
        else:
            chooseMethod(plaintxt,key)
            break
        '''
    
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
    alp_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("Encoding with List function...")
    alphabet = {c: i for i, c in enumerate(string.ascii_letters)}
    a = message
    b = generateKey(message,key)
    k = ""

    lst_a = []
    lst_b = []
    
    for i in a:
        lst_a.append(alphabet.get(i))
    for i in b:
        lst_b.append(alphabet.get(i))

    zipped_lists = zip(lst_a, lst_b)
    sum_list = [(x + y)%26 for (x, y) in zipped_lists]

    cipher = []
    for index_list,item_list in enumerate(sum_list):
        for index, item in enumerate(alp_list):
            if (item_list == index):
                cipher.append(item)
            
    print(cipher)
                    
    
##########################  LIST method ENDS here ############################
    








##########################  TUPLE method STARTS here ############################
def encodeWithTuple(plainText,key):
    baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    keyTuple = ()
    keyLength = 0
    
    while keyLength < len(plainText):
        for char in key:
            if keyLength < len(plainText):
                ch = (str(char),)
                keyTuple += ch
                #keyTuple += ch
                keyLength += 1
                
    plainTextTuple = () 
    for i in range(len(plainText)):
        plainTextTuple += (plainText[i],)    

    cipherTupleInt_1 = ()
    cipherTupleInt_2 = ()
    
    for x in range(len(plainTextTuple)):
            for z in range(len(baseAlphabet)):
                if plainTextTuple[x] == baseAlphabet[z]:
                    cipherTupleInt_1 += (z,)

    
    for y in range(len(keyTuple)):
        for z in range(len(baseAlphabet)):
            if keyTuple[y] == baseAlphabet[z]:
                cipherTupleInt_2 += (z,)
    newTuple = ()            
    for i in range(len(cipherTupleInt_1)):
        newTuple += ((cipherTupleInt_1[i]+ cipherTupleInt_2[i])%26,)

    finalres = ()
    for j in range(len(newTuple)):
        for z in range(len(baseAlphabet)):
            if newTuple[j] == z:
                finalres += (baseAlphabet[z],)
    print("Encoding with Tuple function...")
    print("Message = ",plainTextTuple) 
    print("Genererated Key = ",keyTuple)
    print("Result = ",finalres)
    
        
    
##########################  TUPLE method ENDS here ############################



startingPoint()







