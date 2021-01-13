# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
def getSongPairCount(songs):
  if songs is None or len(songs) == 1:
    return 0

  # loop through songs with indexers i and j O(n^2)
  # if i and j form a pair, append those values to already used set, increment counter by 1
  # ask if 0 length counts
  counter = 0

  for i in range(len(songs) - 1):
    for j in range(i+1, len(songs)):
      if (songs[i] + songs[j]) % 60 == 0:
        print('found pair', songs[i], songs[j])
        counter += 1
  
  # make a dict

  # for each song, 
  # make a 'simplified' song = song % 60
  # pair = 60 - simplified song
  # if pair in dict: increment counter by dict[pair]
  # if simplified_song == 0; simplified-song = 60
  # increment dict[simplied_song] += 1


  return counter

print(getSongPairCount([37, 23, 60]) == 1)
print(getSongPairCount([10, 50, 90, 30]) == 2)
print(getSongPairCount([30, 20, 150, 100, 40]) == 3)
print(getSongPairCount([60, 60, 60]) == 3)