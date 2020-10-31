# https://leetcode.com/discuss/interview-question/853053/
# REDO
from collections import deque

def turnstile(numCust, arrTime, directions):
  i = 0
  enterQ = deque()
  exitQ = deque()
  result = [-1] * numCust
  time = 0
  status = True # true = exit, false = enter

  while i < numCust or enterQ or exitQ:
    # load queues
    while i < numCust and arrTime[i] <= time:
      if directions[i] == 1:
        exitQ.append(i)
      else:
        enterQ.append(i)
      i+=1
    
    # if there are customers waiting to enter and exit
    if enterQ and exitQ:
      # previous second wasn't used, then existing customer goes first
      if (len(set(result)) == 0 and result[0] == -1) or max(result) != time-1:
        result[exitQ.popleft()] = time
        status = True
      # last customer left, then next customer will exit
      elif status == True:
        result[exitQ.popleft()] = time
        status = True
      # last customer entered, then next customer will enter
      elif status == False:
        result[enterQ.popleft()] = time
        status = False
    elif enterQ:
      result[enterQ.popleft()] = time
      status = False
    elif exitQ:
      result[exitQ.popleft()] = time
      status = True
    else:
      pass

    time += 1
  return result

test = turnstile(4,[0,0,1,5],[0,1,1,0])
print(test == [2,0,1,5])