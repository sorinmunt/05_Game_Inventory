
def display_inventory(inventory):

    length_of_inventory = len(inventory)
    list_of_keys_of_inventory = list(inventory.keys())
    list_of_values_of_inventory = list(inventory.values())


    for items in range(length_of_inventory):
        if length_of_inventory != 0:
            print(f'{list_of_keys_of_inventory[items]}: {list_of_values_of_inventory[items]}')



def add_to_inventory(inventory, added_items):

    list_of_keys_of_inventory = list(inventory.keys())
    list_of_values_of_inventory = list(inventory.values())
    length_of_inventory = len(inventory)


    list_of_keys_of_my_added = list(added_items.keys())
    length_of_my_added = len(added_items)


    for items_of_inventory in range(length_of_inventory):
        for items_of_my_added in range(length_of_my_added):
            if list_of_keys_of_inventory[items_of_inventory] == list_of_keys_of_my_added[items_of_my_added]:
                inventory[list_of_keys_of_inventory[items_of_inventory]] +=1
        



    for items_of_my_added in range(length_of_my_added):
        if list_of_keys_of_my_added[items_of_my_added] not in inventory:
            inventory.update({list_of_keys_of_my_added[items_of_my_added]: 1})
    

def remove_from_inventory(inventory, removed_items):

    list_of_keys_of_inventory = list(inventory.keys())
    list_of_values_of_inventory = list(inventory.values())
    length_of_inventory = len(inventory)

    list_of_keys_of_removed_items = list(removed_items.keys())
    length_of_removed_items = len(removed_items)


    for items_of_inventory in range(length_of_inventory):
        for items_of_removed in range(length_of_removed_items):
            if list_of_keys_of_inventory[items_of_inventory] == list_of_keys_of_removed_items[items_of_removed]:
                inventory[list_of_keys_of_inventory[items_of_inventory]] -=1
                if inventory[list_of_keys_of_inventory[items_of_inventory]] <= 0:
                    inventory.pop(list_of_keys_of_inventory[items_of_inventory])




def print_table(inventory, order):


    inventory_sorted = sorted(inventory.items(), key=lambda x: x[1], reverse=order)

    print(f'--------------------------')
    print(f'{"colour name":<15}{"|":<1}{"count":>10}')
    print(f'--------------------------')


    for i in inventory_sorted:
        print(f'{i[0]:<15}{"|":<1}{i[1]:>10}')


    print(f'--------------------------')



def print_table1(inventory):

    length_of_inventory = len(inventory)
    list_of_keys_of_inventory = list(inventory.keys())
    list_of_values_of_inventory = list(inventory.values())


    print(f'--------------------------')
    print(f'{"colour name":<15}{"|":<1}{"count":>10}')
    print(f'--------------------------')

    for items in range(length_of_inventory):
        if length_of_inventory != 0:
            print(f'{list_of_keys_of_inventory[items]:<15}{"|":<1}{list_of_values_of_inventory[items]:>10}')

        #print(f'{i[0]:<15}{"|":<1}{i[1]:>10}')


    print(f'--------------------------')


def import_inventory(inventory, filename):

    import csv

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            imported_inventory = row

    print(f'inventory = {inventory}')
    print(f'imported_inventory = {imported_inventory}')

    add_to_inventory(my_inventory, imported_inventory)

    print(f'inventory = {inventory}')


def export_inventory(inventory, filename):

    import csv

    with open(filename, mode='w') as csv_file:

        #ieldnames = ['emp_name', 'dept', 'birth month']
        list_of_keys_of_inventory = list(inventory.keys())

        writer = csv.DictWriter(csv_file, fieldnames=list_of_keys_of_inventory)

        writer.writeheader()
        writer.writerow(inventory)




#----------------------------------------------------------------------------------------------------------------

# MAIN *** MAIN *** MAIN


my_inventory = {'red': 34,'green': 30,'brown': 31,'yellow': 29}

print(my_inventory)

my_added_items = {'red': 1, 'brown': 1, 'mangenta': 1, 'super_yellow': 1}

my_removed_items = {'red': 1, 'yellow': 1, 'mangenta': 1, 'super_mangenta': 25}




display_inventory(my_inventory)
add_to_inventory(my_inventory, my_added_items)
display_inventory(my_inventory)

print(my_inventory)

remove_from_inventory(my_inventory, my_removed_items)

print(my_inventory)


my_order = True  # sorting descending
#my_order = False # sorting ascending

print_table(my_inventory, my_order)
print_table1(my_inventory)


import_inventory(my_inventory,"/home/sorin/Desktop/projects/05_Game_Inventory/names_import.csv")

export_inventory(my_inventory,"/home/sorin/Desktop/projects/05_Game_Inventory/names_export.csv")


exit()

#-----------------------------------------------------------------------------------------------------------------------


