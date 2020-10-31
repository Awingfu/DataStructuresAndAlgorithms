# https://leetcode.com/discuss/interview-question/854110/
# REDO
import heapq

def fiveStarReviews(productRatings, ratingsThreshold):
  # make a min heap
  # always add to the minimum and increment counter, then readd product to heap
  # recalculate
  # if over threshold, return

  num_products = len(productRatings)
  result = 0

  ratings_array = [p[0]/p[1] for p in productRatings]
  curr_rating = sum(ratings_array) / num_products * 100
  
  heap = []
  for p in productRatings:
    heap.append([-diff(p)] + p) # negative because we want greatest change
  print(heap)
  heapq.heapify(heap)

  while curr_rating < ratingsThreshold:
    p_diff, p0, p1 = heapq.heappop(heap)
    curr_rating = curr_rating - (p_diff / num_products * 100) # add current diff
    p0 += 1
    p1 += 1
    heapq.heappush(heap, [-diff([p0,p1]), p0, p1])
    result += 1

  return result

def diff(p):
  return (p[0]+1)/(p[1]+1) - p[0]/p[1] # gain from adding 1 five star review 

productRatings = [[4, 4], [1, 2], [3, 6]]
ratingsThreshold = 77
output = 3
test = fiveStarReviews(productRatings, ratingsThreshold)
print(test == output)