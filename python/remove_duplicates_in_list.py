# Remove duplicates from a list of numbers

list1 = eval(input("Enter a list of numbers"))
print(list1)

#Way-1
list2 = []
for each_value in list1:
    if each_value not in list2:
        list2.append(each_value)

print(list2)

#Way-2
s1 = set(list1)
print(s1)