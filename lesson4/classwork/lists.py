colors = ["red", "green", "blue", "yellow"]

print (colors)

print ("first color:", colors [0])
print ("second color:", colors [1])
print ("third color:", colors [2])
print ("fourth color:", colors [3])
#error: out of range
#print (colors [10]

colors [0] = 'maroon'

print ("after edit:", colors)

colors.append("orange")
print ("after append:", colors)

colors.insert(2, "purple")
print("After insert at index 2:", colors)

colors.remove("green")
print ("after removing 'green':", colors

popped_color = colors.pop
print ("after pop:", colors)

popped_color_at_index = colors.pop (1)
print ("popped color:", colors)

index_of_blue = colors.index("blue")
print("index of 'blue':", index_of_blue)

# error: finding index of color not in list
# colors.index("pink")

colors.append ("blue")
blue_count = colors.count ("blue")
print ("count of blue:", blue_count)

colors.sort()
print ("after sort:" colors)

colors.reverse
print ("after reverse:", colors)









