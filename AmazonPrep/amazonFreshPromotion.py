# https://leetcode.com/discuss/interview-question/762546/
def isCustomerWinner(codeList, shoppingCart):
  if codeList == []:
    return 1
  if shoppingCart == []:
    return 0
  anything = None
  # for each pattern in codeList, 
  # find a case where it's true, if so, continue, if ends return false
  for i in range(len(codeList)):
    pattern = codeList[i]
    patternLen = len(pattern)
    matchPattern = False
    for j in range(len(shoppingCart)-patternLen + 1):
      potentialPattern = shoppingCart[j:j+patternLen]
      print(pattern, potentialPattern)
      match = True
      for k in range(patternLen):
        if pattern[k] == 'anything':
          if anything is None:
            anything = potentialPattern[k]
          if potentialPattern[k] != anything:
            match = False
            break
        elif pattern[k] != potentialPattern[k]:
          match = False
          break
      if match == True:
        matchPattern = True
        print("Matched")
        print(pattern, potentialPattern)
        break
    if matchPattern == False:
      return 0
  return 1
        
  # i = 0 # for each pattern
  # j = 0 # starting index for shoppingcart
  # while i < len(codeList) and j+len(codeList[i]) <= len(shoppingCart):
  #   match = True
  #   pattern = codeList[i]
  #   for k in range(len(pattern)):
  #     if pattern[k] == 'anything':
  #       if anything is None:
  #         anything = shoppingCart[j+k]
  #       if shoppingCart[j+k] != anything:
  #         match = False
  #         break
  #     if pattern[k] != 'anything' and pattern[k] != shoppingCart[j+k]:
  #       match = False
  #       break
  #   if match:
  #     j+= len(pattern)
  #     i+=1
  #   else:
  #     j+=1
  # return 1 if i == len(codeList) else 0



# print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
# print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['banana', 'orange', 'banana', 'apple', 'apple']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']))
print(isCustomerWinner([['apple', 'banana','apple', 'banana', 'coconut']], ['apple', 'banana', 'apple', 'banana', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'orange'], ['orange', 'banana', 'orange']], ['apple', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'grape']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'banana']], ['apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([["anything", "apple" ], ["banana", "anything", "banana"]], ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]))
print(isCustomerWinner([['anything']], ['apple', 'apple', 'apple', 'banana']))