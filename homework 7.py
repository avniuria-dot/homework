def find_palindromes(string_list):
  palindromes = []
  for word in string_list:
    if word == word[::-1]:
      palindromes.append(word)
  return palindromes  