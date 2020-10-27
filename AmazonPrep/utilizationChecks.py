# https://leetcode.com/discuss/interview-question/895097/Amazon-or-OA-2020-or-Utilization-Checks
def finalInstances(instances, averageUtil):
  counter = 0
  while counter < len(averageUtil):
    if averageUtil[counter] > 60:
      doubled = instances * 2
      if doubled <= 2 * (10 ** 8):
        instances = doubled
        counter += 10
    elif averageUtil[counter] < 25 and instances > 1:
      instances = int((instances / 2) + (0 if instances % 2 == 0 else 1))
      counter += 10
    
    counter += 1
  return instances

test = finalInstances(2, [25,23,1,2,3,4,5,6,7,8,9,10,76,80])
print(test)