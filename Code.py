#Rania Aziz Farooqi

#Storing the menu indicating different categories of food.
Menu=["Burgers","Combo_Meals","Drinks","Add_Ons"]
Burgers = [
    {
        "id": 101,
        "name": "Chicken Burger",
        'price': "10 AED",
        "stock": 29,
    },
    {
        "id": 102,
        "name": "Beef Burger",
        'price': "13 AED",
        "stock": 32,
    },
    {
        "id": 103,
        "name": "Zinger Burger",
        'price': "18 AED",
        "stock": 13,
    },
    {
        "id": 104,
        "name": "Cheeseburger",
        'price': "9 AED",
        "stock": 4,
    },
    {
        "id": 105,
        "name": "Veg Burger",
        'price': "8 AED",
        "stock": 21,
    },
]
Combo_Meals = [
    {
        "id": 106,
        "name": "Chicken Burger Combo",
        'price': "15 AED",
        "stock": 18,
    },
    {
        "id": 107,
        "name": "Beef Burger Combo",
        'price': "20 AED",
        "stock": 2,
    },
    {
        "id": 108,
        "name": "Zinger Burger Combo",
        'price': "22 AED",
        "stock": 1,
    },
]
Drinks = [
    {
        "id": 109,
        "name": "Original Hot Coffee",
        'price': "10 AED",
        "stock": 48,
    },
    {
        "id": 110,
        "name": "Iced Latte",
        'price': "20 AED",
        "stock": 22,
    },
    {
        "id": 111,
        "name": "Pepsi",
        'price': "4 AED",
        "stock": 80,
    },
    {
        "id": 112,
        "name": "Water",
        'price': "2 AED",
        "stock": 113,
    },
]
Add_Ons = [
    {
        "id": 113,
        "name": "Extra Fries",
        'price': "10 AED",
        "stock": 8,
    },
    {
        "id": 114,
        "name": "Cheeseballs",
        'price': "8 AED",
        "stock": 12,
    },
    {
        "id": 115,
        "name": "Chicken Nuggets",
        'price': "14 AED",
        "stock": 19,
    },
    {
        "id": 116,
        "name": "Cookie",
        'price': "5 AED",
        "stock": 57,
    },
]

quit = False
item = ''

while quit == False:
    print("Welcome to Burgermania!\nHere is what we have to ofFer:")
    print("1 - Burgers\n2 - Combo Meals\n3 - Drinks\n4 - Add Ons")
    order_pt1=int(input("Enter the number associated with each category to browse its menu."))

    def Menu(list):
        for i in list:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")

    if order_pt1>4 or order_pt1<1:
        print("This number is invalid")
    elif order_pt1==1:
        print("Burgers:")
        Menu(Burgers)
    elif order_pt1==2:
        print("Combo Meals:")
        Menu(Combo_Meals)
    elif order_pt1==3:
        print("Drinks:")
        Menu(Drinks)
    else:
        print("Add Ons:")
        Menu(Add_Ons)

    order = int(input("Enter the ID of the item you want to order: "))
    for i in (Burgers or Combo_Meals or Drinks or Add_Ons) :
        if order == i['id']:
            item = i
    if item == '':
        print('This code is invalid.')
        order = input("To quit the machine enter q and to continue buying enter anything: ")

def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["price"]

    return sum

def create_reciept(the_item, reciept):

    for i in the_item:
        reciept += f"""
        \t{i["name"]} -- {i['price']}
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
