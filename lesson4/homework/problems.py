import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["Windows", "macOS", "Linux"]

last_index = len(operating_systems) - 1
print(operating_systems[last_index])

operating_systems.reverse()
print(operating_systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
schoolSubjects = ["english", "computer science", "science", "math"]
print (schoolSubjects[1])
schoolSubjects.sort()
print (schoolSubjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
errorCodes = ["IndexError", "TypeError", "ValueError", "KeyError", "NameError"]
print (len (errorCodes))

for errorCodes in errorCodes:
  print (errorCodes)

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programmingLanguages = ["Python", "JavaScript"]
print (random.choice(programmingLanguages))

# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = [12376, 78392, 88594, 78372, 78323, 78932]

passwords.remove(12376)

for password in passwords:
  print(password)










