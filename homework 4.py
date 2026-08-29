def reverse_text(string):
   for i in range(len(string)):
       string[i] = string[len(string)-1-i]
   return string

string = "hello"
print(reverse_text(string))