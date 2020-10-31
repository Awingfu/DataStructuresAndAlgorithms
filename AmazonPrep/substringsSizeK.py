# https://leetcode.com/discuss/interview-question/877624/

def substringsOfSizeK(inputString, num):
  # use sliding window and 2 sets
  # result initialized to a set
  # if inputString size < num, return []
  # for string len num in inputString
  # if len(string) == len(set(string.split(''))) + 1
  # add string to result
  # return list(result)
  result = set()

  for i in range(len(inputString) - num + 1):
    substr = inputString[i:i+num]
    if len(substr) == len(set(list(substr))) + 1:
      result.add(substr)

  # print(list(result)
  return list(result)

test1 = substringsOfSizeK('awaglk',4)
print(test1 == ['awag'])

test2 = substringsOfSizeK('democracy',5)
# print(test2)
print(test2 == ['ocrac', 'cracy']) # order doesnt matter, but close enough
