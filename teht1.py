

tuple = (1, 8, 3) 
list = [9, 5, 0] 
set = {8, 4, 8} 
dictionary = {"john":5119222, "tom":1415096, "mike":45312387}

print(tuple[1])
print(list[1])

iter = 0
for i in set:
    if iter == int(len(set)/2):
        print(i)
    iter += 1


iter = 0
for i in dictionary:
    if iter == int(len(dictionary)/2):
        print(i, dictionary[i])
    iter += 1











