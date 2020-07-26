
#def display_inventory(inventory):





#my_dictionary = {'red': 34,'green': 30,'brown': 31,'yellow': 29}
my_dictionary ={}

length_of_my_dictionary = len(my_dictionary)
list_of_keys_of_my_dictionary = list(my_dictionary.keys())
list_of_values_of_my_dictionary = list(my_dictionary.values())


print(f'Length of my dyctionary {length_of_my_dictionary}')
print(f'list of keys {list_of_keys_of_my_dictionary}')
print(f'list of values {list_of_values_of_my_dictionary}')

for items in range(length_of_my_dictionary):
    if length_of_my_dictionary != 0:
        print(f'{list_of_keys_of_my_dictionary[items]}: {list_of_values_of_my_dictionary[items]}')
    



