bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0]) # to access any value in a list, type the name of the list followed by the index of the item in square brackets.
print(bicycles[1])
print(bicycles[2])

print(bicycles[-1]) # index -1 always returns the last item in a list

message = f"My first bicycle was a {bicycles[0].title()}"
print (message)