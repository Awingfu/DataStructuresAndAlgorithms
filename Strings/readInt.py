# software bug
# alexas text to speech
# one thousand three hundred twenty five -> 1325
# given integer input, translate number to fully worded
# upper bound < 100000
# lower bound >= 0


# 0-20, 30, 40 ... 90
# number_word_map = {0: 'zero', 1: 'one': 2: 'two' ... 90: 'ninety'}

# read thousands
# 123,456 -> read_hundred(123) + thousand + read_hundred(456)
# 3,456 -> read_hundred(3) + thousand + read_hundred(456)
# read hundred takes in a numebr < 1000
# 123 -> <hundred place> hundred + read_tens(23)
# read tens
# 23 -> split to 20 and 3 -> get the map for those keys

# 72,419
# 24,000,123

# def read_number(input):
#     prefix = "" 
#     if input < 0:
#         return "negative " + read_number(-input)
#     if input == 0: 
#         return "zero"
#     elif input >= 1000:
#         return read_thousands(input)
#     elif input >= 100:
#         return read_hundred(input)
#     else: 
#         return read_tens(input)

# def read_thousands(input):
#     thousands = input // 1000
#     hundreds = input % 1000
#     if thousands == 0:
#         return read_hundred(input)
#     else:
#         return read_hundred(thousands) + " thousand " + read_hundred(hundreds) # seventy two + thousand + four hundred nineteen
    
# def read_hundreds(input):
#     hundreds_place = input // 100 
#     tens = input % 100 
#     if hundreds_place == 0:
#         return read_tens(tens)
#     else:
#         return number_word_map[hundreds] + " hundred " + read_tens(tens) # four hundred + nineteen
    
# def read_tens(input):
#     tens_place = input // 10
#     ones_place = input % 10 
#     if input == 0:
#         return ""
#     elif tens_place > 1:
#         tens = tens_place * 10 
#         return number_word_map[tens] + " " + number_word_map[ones_place]
#     else: # < 20
#         return number_word_map[ones_place]

under_20_map = {
  0: "zero",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen"
}
tens_factors_map = {
  20: 'twenty',
  30: 'thirty',
  40: 'fourty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
}

def read_number(num):
  if num == 0:
    return "zero"

  if num < 0:
    return "negative " + read_number(num * -1)

  places = ["", "thousand", "million", "billion"]

  groups = [] # groups of 3 numbers in reverse so 123,456,789 -> [789,456,123]
  while num > 0:
    groups.append(num % 1000)
    num = num // 1000 

  #  [789,456,123] -> ["seven hundred eighty nine", "four hundred fifty six thousand", etc]
  result = [] 
  for i in range(len(groups)):
    words = read_hundreds(groups[i]) # 123 -> one hundred twenty three
    if words == "": # so [123, 000, 123] would skip thousands
      continue
    result.append(read_hundreds(groups[i]) + " " + places[i]) # add places
  return " ".join(result[::-1]) # reverse list then join with space in between

def read_hundreds(num):
  if num == 0:
    return ""

  hundreds_place = num // 100
  if hundreds_place >= 1:
    return under_20_map[hundreds_place] + " hundred " + read_tens(num % 100)

  return read_tens(num % 100)

def read_tens(num):
  if num == 0:
    return ""
  
  if num < 20:
    return under_20_map[num]

  tens = (num // 10) * 10 # floor to nearest tens
  ones = num % 10
  if ones == 0:
    return tens_factors_map[tens]
  
  return tens_factors_map[tens] + " " + under_20_map[ones]


print(read_number(15))
print(read_number(500))
print(read_number(720))
print(read_number(123456))
print(read_number(1000000000))
print(read_number(-1000000000))
print(read_number(999555444333))