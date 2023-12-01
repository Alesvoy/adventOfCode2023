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
  
  if(digit in digitsTuple):
    return pointer, digit
  elif(increment == True):
    newPointer = pointer + 1
    return newPointer, None
  elif(increment == False):
    newPointer = pointer - 1
    return newPointer, None
    
    




def sumOfDigits(word):
  digitsTuple = ('0','1','2','3','4','5','6','7','8','9')
  startingNumberLetters = ['o', 't', 'f', 's', 'e', 'n']
  numbersAsWords = ['one','two','three','four','five','six','seven','eight','nine']
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
  myList = []
  for i in range(0,len(word)):
    if word[i] in digitsTuple:
      myList.append(word[i])
    elif(word[i] in startingNumberLetters):
      myStr = ''
      for j in range(i, len(word)):
        myStr += word[j]
        if(myStr in numbersAsWords):
          myList.append(numsDict[myStr])
          break
  return myList[0] + myList[len(myList) - 1]
    

textList = getArrayOfText()
totalSum = 0

for word in textList:
  totalSum += int(sumOfDigits(list(word)))

print(totalSum)