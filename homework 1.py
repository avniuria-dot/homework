list = (3, 5, 7, 20, 11, 13,)
max_number = list[0]
for i in range(len(list)-1):
    if list[i+1] > max_number:
        max_number = list[i+1]

print(max_number)