def count_vowels(string):
  count = 0
  for i in range(len(string)):
    if string[i] in "aeiouAEIOU":
      count += 1
  return count

string = "jahsdfbvjlsHBVCjlBVzderg"
print(count_vowels(string))