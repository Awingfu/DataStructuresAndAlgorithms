# https://leetcode.com/discuss/interview-question/542597/

import heapq

def getTopKeywords(k, keywords, reviews):
  # store counts in a hashmap of keywords: review counts
  # loop through keywords, load dictionary with values 0

  # for each review,
  # for each word, 
  # init set of indexes per keyword
  # for each keyword by index
  # if keyword == word and index not in set, increment dictionary[keyword] value and add index to set
  
  # for each key in dict
  # generate array with values of [-value, keyword]
  # convert array to min heap
  # 
  # for each k, heappop heap, and store keyword into result array
  # return result array  

  keyword_counts = {}  # space O(keywords)
  for word in keywords:
    keyword_counts[word] = 0
  
  for review in reviews: # O(reviews) * O(max_words in review) * O(keywords)
    for word in review.split(' '): # space O(keywords)
      alreadySeen = set()
      for keyword in keywords:
        if word == keyword and keyword not in alreadySeen:
          keyword_counts[keyword] += 1
          alreadySeen.add(keyword)
  
  heap = []
  for key in keyword_counts.keys(): # O(keywords)
    heap.append([-keyword_counts[key], key])
  
  heapq.heapify(heap) # O(keywords)
  print(heap)
  result = []
  for _ in range(k):
    result.append(heapq.heappop(heap)[1]) #O(log(keywords))

  return result

test1 = getTopKeywords(2,["anacell", "cetracular", "betacellular"], [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
])

print(test1 == ["anacell", "betacellular"])