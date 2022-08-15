# Given a S3 API to suppport 3 functiosn
load tested 

class S3api:
  def __init__(self):
    self.cache = {}
    self.indexer = {}
    self.counter = 0
    self.random = []

  def getKey(self, key):
    try:
      if key in self.cache:
        return key
      else:
        return None
    except:
      print()
      return None
get(key)
add(key)
delete(key)
getRandomKey() # gets random key

  def getRandomKey(self):
    keys = list(self.cache.keys())
    randomIndex = math.randomRange(0,self.counter)
    return keys[randomIndex]