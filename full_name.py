first_name = "stephen"
last_name = "curry"
full_name = f"{first_name} {last_name}" # place letter f before quotation marks to insert a variables value into a string. Put braces around each variable you want to insert inside the string.
print(full_name)

full_name = "{first_name} {last_name}" # if you omit f before the quotes, the output will show: {first_name} {last_name}
print(full_name)

# these string are called f-strings or format strings. Messages can also be composed with them.

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# you can also assign the entire message to a variable

message = f"Hello, {full_name.title()}!"
print (message)