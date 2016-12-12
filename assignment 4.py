#Gianluca Bonanno, Assignment 4, 1 + 2

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#Takes in a single character and returns an index based on its location in
#the alphabet. (The index in the ALPHABET string)
#ch - character being converted
def letterToIndex(ch):
  #print(ch) (Debug)
  chLower = ch.lower()  #Converts the character to a lowercase letter.  
  idx = ALPHABET.find(chLower)
  if idx < 0:
      print ("error: letter not in the alphabet", ch)
  #print(idx) (Debug)
  return idx

#Takes in a number and returns the corresponding letter in the ALPHABET string
#Returns an error message if the index is not within the indexes of the string
# idx - index being converted
def indexToLetter(idx):
  #print(idx) (Debug)
  if idx > 26:
    print ('error: ', idx, ' is too large')
    letter = ''
  elif idx < 0:
    print ('error: ', idx, ' is less  than 0')
    letter = ''
  else:
    letter = ALPHABET[idx]
  #print(letter) (Debug)
  return letter

#Takes in a key and a message in plaintext and converts it to a ciphertext
#message
#encrypyKey - key being used
#plainText - Message being encrypted
def encryptVignere(encryptKey,plainText):
  #print(encryptKey) (Debug)
  #print(plainText) (Debug)
  cipherText = ""
  keyLen = len(encryptKey)
  charNum = 0
  for i in range(len(plainText)):
    ch = plainText[i]
    if ch == ' ':
      cipherText = cipherText + ch
    else:
      cipherText = cipherText + vignereIndex(encryptKey[i%keyLen],ch)
  #print(cipherText) (Debug)
  return cipherText

#Takes a letter from the key and a plaintext letter from the message and
#returns a corresponding encrypted letter by using the indexToLetter
#function.
#keyLetter - letter in the key being used
#plainTextLetter - letter in the message that is being converted
#keyIndex - index of the letter in the key
#ptIndex - index of the plaintext letter in the message
#newIdx - index for the ciphertext letter
def vignereIndex(keyLetter,plainTextLetter):
    #print(keyLetter) (Debug)
    #print(plainTextLetter) (Debug)
    keyIndex = letterToIndex(keyLetter) #Creates a variable for the index of the key letter
    ptIndex = letterToIndex(plainTextLetter) #Creates a variable for the index of the plaintext letter
    newIdx = (ptIndex + keyIndex) % 26 #Finds the index of the ciphertext letter in the Vignere square
    #print(indexToLetter(newIdx)) (Debug)
    return indexToLetter(newIdx) #Converts the index into the ciphertext letter and returns said letter

#Takes in a letter from the key and a ciphertext letter and returns a
#plaintext letter by using the indexToLetter function.
#keyLetter - letter in the key being used
#ctLetter - ciphertext letter being converted
#keyIndex - index of the letter in the key
#ptIndex - index of the plaintext letter in the message
#newIdx - index for the ciphertext letter
def undoVig(keyLetter, ctLetter):
    #print(keyLetter) (Debug)
    #print(ctLetter) (Debug)
    keyIndex = letterToIndex(keyLetter) #Creates a variable for the index of the key letter
    ptIndex = letterToIndex(ctLetter) #Creates a variable for the index of the plaintext letter
    newIdx = (ptIndex - keyIndex) % 26 #Finds the index of the plaintext letter using the Vignere square
    #print(indexToLetter(newIdx) (Debug)
    return indexToLetter(newIdx) #Converts the index to the plaintext letter and returns said letter

#Takes a key and the ciphertext message and returns the plaintext message
#encrypyKey - key being used
#cipherText - ciphertext message being decrypted
def decryptVignere(encryptKey, cipherText):
    #print(encrypyKey) (Debug)
    #print(cipherText) (Debug)
    plainText = ""
    keyLen = len(encryptKey)
    charNum = 0
    for i in range(len(cipherText)):
        ch = cipherText[i]
        if ch == ' ':
            plainText = plainText + ch
        else:
            plainText = plainText + undoVig(encryptKey[i%keyLen],ch)
    #print(plainText) (Debug)
    return plainText

#Tests the program by asking the user for a key and message to encrypt. It encrypts
#the message and prints the encrypted message. Then it takes that same encrypted
#message and decrypts it and prints the result of that. (It should be the original
#user inputted message)
def main():
  key = input("Enter an alphabetic key for encrypting a message" +\
              "\nor press <Enter> to quit:  ")
  while(key):
    message = input("Enter a message to encrypt with the current key"  +\
                    "\nor press <Enter> to get another key:  ")
    while(message):
      cipherTextMessage = encryptVignere(key, message)
      print(cipherTextMessage)
      plainTextMessage = decryptVignere(key, cipherTextMessage)
      print(plainTextMessage) 
      message = input("Enter another message to encrypt with the current key"  +\
                    "\nor press <Enter> to get another key:  ")

    key = input("Enter a new alphabetic key for encrypting a message" +\
              "\nor press <Enter> to quit:  ")
      
main()
