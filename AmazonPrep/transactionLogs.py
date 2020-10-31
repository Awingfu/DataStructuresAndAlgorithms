# https://leetcode.com/discuss/interview-question/862600/

def transactionLogs(logs, threshold):
  # 1 hashmap of userID: transaction
  seenUsers = {}
  for transaction in logs: # O(logs)
    user1 = transaction[0]
    user2 = transaction[1]
    if user1 in seenUsers:
      seenUsers[user1] += 1
    else:
      seenUsers[user1] = 1
    if user2 != user1:
      if user2 in seenUsers:
        seenUsers[user2] += 1
      else:
        seenUsers[user2] = 1
  result = []
  for user in seenUsers.keys(): # O(logs)
    if seenUsers[user] >= threshold:
      result.append(user)
  result.sort() # worst case, every user unique and meets thresh O(logs*log(logs))
  print(result)
  return result

test1 = transactionLogs([
['345366', '89921', '45'],
['029323', '38239', '23'],
['38239', '345366', '15'],
['029323', '38239', '77'],
['345366', '38239', '23'],
['029323', '345366', '13'],
['38239', '38239', '23']], 3)

print(test1 == ['029323', '345366', '38239'])