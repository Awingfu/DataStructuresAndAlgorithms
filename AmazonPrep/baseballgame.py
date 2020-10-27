# https://leetcode.com/problems/baseball-game/

def calPoints(ops):
  record = []
  for item in ops:
    if item == "D":
      record.append(record[-1] * 2)
    elif item == "C":
      record.pop()
    elif item == "+":
      record.append(record[-2] + record[-1])
    else: # number
      record.append(int(item))
  return sum(record)

test1 = calPoints(["5","2","C","D","+"])
test2 = calPoints(["5","-2","4","C","D","9","+","+"])
test3 = calPoints(["1"])

print(test1 == 30)
print(test2 == 27)
print(test3 == 1)
