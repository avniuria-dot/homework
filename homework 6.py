def find_longest_word(string_list):
  longest_length = 0
  longest_words = []
  for word in string_list:
    if len(word) > longest_length:
      longest_length = len(word)
      longest_words = [word]
    elif len(word) == longest_length:
      longest_words.append(word)

  return longest_words


string_list = ["apple", "banana", "cherry", "date"]
print(find_longest_word(string_list))