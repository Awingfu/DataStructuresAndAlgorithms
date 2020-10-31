# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq

def kClosest(points, K):
  # create a min heap where [dist, point]
  heap = []
  for point in points:
    distance = point[0] ** 2 + point[1] ** 2
    heapq.heappush(heap, [distance, point])
  
  result = []
  for _ in range(K):
    result.append(heapq.heappop(heap)[1])

  return result


test1 = kClosest( [[3,3],[5,-1],[-2,4]], 2)
print(test1 == [[3,3],[-2,4]])