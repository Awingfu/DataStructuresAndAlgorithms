# https://leetcode.com/problems/most-common-word/

def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    # store a hashmap of each word in lowercase and their occurence
    
    # keep track of highest occurence
    # keep track of result as empty string
    # loop through hashmap, if word not in banned, and value > highest occurance, update highest occurence and result
    
    wordCounts = {}
    cleanedParagraph = paragraph.replace(',',' ').replace('!',' ').replace('?',' ').replace('\'',' ').replace(';',' ').replace('.',' ')
    for word in cleanedParagraph.split(" "):
        word = word.lower()
        # print(word)
        if word.isalnum():
          if word in wordCounts:
              wordCounts[word] += 1
          else:
              wordCounts[word] = 1
    
    highestOccurence = 0
    result = ''
    for word in wordCounts.keys():
        if wordCounts[word] > highestOccurence and word not in banned:
            result = word
            highestOccurence = wordCounts[word]
    
    return result
    
test1 = mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
print(test1)