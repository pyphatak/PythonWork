invited_guests=["Prashant", "ajanta", "Mukta", "siddharth", 'deepak', 'kaustubh']
#print(invited_guests)
#print(sorted(invited_guests))

#invited_guests.sort()
#invited_guests.sort(reverse=True)
#print(invited_guests)

print("Sorted list is " + str(sorted(invited_guests)))
print("Original list is " + str(invited_guests))

#print(invited_guests.reverse())
print("The first three items in the list are " + str(invited_guests[:3]))
print(str(len(invited_guests)))

#print("Three items from the middle of the list are " + str(invited_guests[len(invited_guests)/2:3]))

middle_of_the_list = int(len(invited_guests)/2)
print(middle_of_the_list)

print(invited_guests[middle_of_the_list:middle_of_the_list+3])
print("Three items from the middle of the list are " + str(invited_guests[middle_of_the_list:middle_of_the_list+3]))
print("The last three items in the list are " + str(invited_guests[-3:-1]))
print(invited_guests[-1])








