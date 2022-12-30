items = [
    {
        "item_id": 0,
        "item_name": "C",
        'item_price': 60,
    },
    {
        "item_id": 1,
        "item_name": "Fanta",
        'item_price': 90,
    },
    {
        "item_id": 2,
        "item_name": "Kurkure",
        'item_price': 25,
    },
    {
        "item_id": 3,
        "item_name": "Thumbs Up",
        'item_price': 90,
    },
    {
        "item_id": 4,
        "item_name": "Wai-Wai",
        'item_price': 20,
    },
]

quit = False
item = ''

while quit == False:
    print("Welcome to Burgermania!\nHere is what we have to ofFer:")
    for i in items:
        print(f"Item Name: {i['item_name']} - Price: {i['item_price']} - code: {i['item_id']}")

    order = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if order == i['item_id']:
            item = i
    if item == '':
        print('This code is invalid.')
    else:
        print(f"Great, {item['item_name']} will cost you {item['item_price']} dollars")

        price = int(input(f"Enter {item['item_price']} dollars to purchase: "))
        if price == item['item_price']:
            print(f"Thank you for buying here is your {item['item_name']}")
        else:
            print(f"Please enter only {item['item_price']} dollars")

    order = input("To quit the machine enter q and to continue buying enter anything: ")

def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["item_price"]

    return sum

def create_reciept(the_item, reciept):

    for i in the_item:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """

    reciept += f"""
        \tTotal --- {sum(the_item)}
        
        
        """
    return r

if order == 'c':
    quit = False
else:
    quit = True
print('')
