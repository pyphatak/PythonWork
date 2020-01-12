list_of_my_pizzas = ['Cheese', 'Veggie', 'Grandma']
for pizza in list_of_my_pizzas:
	print("I like " + pizza + " pizza")

list_of_friends_pizzas = list_of_my_pizzas[:]
print(list_of_my_pizzas)
print(list_of_friends_pizzas)
list_of_my_pizzas.append('thin crust')
list_of_friends_pizzas.append('jalapeno')

print(list_of_my_pizzas)
print(list_of_friends_pizzas)




