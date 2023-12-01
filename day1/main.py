def getArrayOfText():
  file = open("challenge.txt", 'r')
  content = file.read()
  listOfText = content.split('\n')
  file.close()
  return listOfText

def isDigitValid(digit, pointer, increment, word):
  digitsTuple = ('0','1','2','3','4','5','6','7','8','9')
  startingNumberLetters = ['o', 't', 'f', 's', 'e', 'n']
  numbersLength = {
    'o': 3,
    't': [3,5],
    'f': 4,
    's': [3,5],
    'e': 5,
    'n': 4
  }
  numsDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }
  
  if(digit in digitsTuple):
    return pointer, digit
  elif(increment == True):
    newPointer = pointer + 1
    return newPointer, None
  elif(increment == False):
    newPointer = pointer - 1
    return newPointer, None
    
    




def sumOfDigits(word):
  pointer1 = 0
  pointer2 = len(word) - 1
  digit1, digit2 = None, None
  while(digit1 == None or digit2 == None):
    pointer1, digit1 = isDigitValid(word[pointer1], pointer1, True, word)
    pointer2, digit2 = isDigitValid(word[pointer2], pointer2, False, word)
      
  return digit1 + digit2

textList = getArrayOfText()
totalSum = 0

for word in textList:
  totalSum += int(sumOfDigits(list(word)))

print(totalSum)
