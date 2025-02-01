# FileNotFoundError
# with open("a_file.txt", "r") as file:
#     file.read()

try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message: # Get hold of the error message
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

# finally:
#     raise TypeError("Error!")

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

