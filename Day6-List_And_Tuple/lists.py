# Create a list
# list1 = [10, 20, 30, 40, "A", "Welcome"]
# print(list1)
#
# list2 = list()
# print(list2)

# Accessing elements from the list

# list1 = [10, 20, 30, 40, "A", "Welcome"]
# print(list1[4])
# print(list1[-2])
# print(list[-3])

# Range of indexes


# Change item list
#
# list1 = [10, 20, 30, 40, "A", "Welcome"]
# list1[0] = "orange"
# print(list1)

# read list items using for loop
# list1 = [10, 20, 30, 40, "A", "Welcome"]
# for ele in list1:
#     print(ele)

# Check item in List

# list1 = [10, 20, 30, 40, "A", "Welcome"]
#
# if 10 in list1:
#     print("element is present")
# else:
#     print("element is not present")

# count elements in ist

list1 = [10, 20, 30, 40, "A", "Welcome"]

print(len(list1))

# Add element to list -- inset() and append()
list1 = [10, 20, 30, 40, "A", "Welcome", "orange"]
print(list1)

# copy elements from list
list1 = [10, 20, 30, 40, "A", "Welcome" ]
# list2 = []
list2 = list1.copy()
print(list2)

# combine or join list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list1 + list2)

list3 = list1 + list2

print(list3)

for i in list2:
    list1.append(i)

print(list1)


# comparison of lists
list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1 == list2)












