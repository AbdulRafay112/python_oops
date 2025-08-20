# C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

my_list = ["rafay" , "Ali" , "python"] 
try:
    value = input("Enter Value ")
    index = int(input("Enter index you want to push "))
    my_list[index] = value 
except IndexError:
    print("Don't try buffer overflow attacks in python")

print(my_list)    