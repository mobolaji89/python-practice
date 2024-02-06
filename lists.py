bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0]) # to access any value in a list, type the name of the list followed by the index of the item in square brackets.
print(bicycles[1])
print(bicycles[2])

print(bicycles[-1]) # index -1 always returns the last item in a list

message = f"My first bicycle was a {bicycles[0].title()}"
print (message)

# Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ['miguel', 'ricky', 'marcus', 'louis']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Greetings: Start with the list you used, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

print(f"Hello, {names[0].title()}")
print(f"Hello, {names[1].title()}")
print(f"Hello, {names[2].title()}")
print(f"Hello, {names[3].title()}")

# Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transportation = ['scooter', 'bicycle', 'motorcycle', 'car', 'truck']
print(f"I would like to own a Razor {transportation[0].title()}")
print(f"I own a blue Schwinn {transportation[1].title()}")
print(f"I don't want to crash the {transportation[2].title()}")
print(f"I drive a fast {transportation[3].title()}")
print(f"I need to move some furniture using the {transportation[4].title()}")


# Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guests = ['Barack Obama','Michael Jordan','Joe Montana','Snoop Dogg','Stephen Curry']
print(f"I would like to invite you to dinner {guests[0].title()}")
print(f"I would like to invite you to dinner {guests[1].title()}")
print(f"I would like to invite you to dinner {guests[2].title()}")
print(f"I would like to invite you to dinner {guests[3].title()}")
print(f"I would like to invite you to dinner {guests[4].title()}")

# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print(f"Unfortunately, {guests[1].title()} cannot attend my dinner.")

guests[1] = "Scottie Pippen"

print(f"I would like to invite you to dinner {guests[0].title()}")
print(f"I would like to invite you to dinner {guests[1].title()}")
print(f"I would like to invite you to dinner {guests[2].title()}")
print(f"I would like to invite you to dinner {guests[3].title()}")
print(f"I would like to invite you to dinner {guests[4].title()}")

