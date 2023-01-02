#Rania Aziz Farooqi
#Storing the menu indicating different categories of food.
Menu=["Burgers","Combo_Meals","Drinks","Add_Ons"]
Burgers = [ #Types of Burgers
    {
        "id": 101, #ID Number
        "name": "Chicken Burger", 
        'price': 10,
        "stock": 29, #The amount that is is in stock
    },
    {
        "id": 102,
        "name": "Beef Burger",
        'price': 13,
        "stock": 32,
    },
    {
        "id": 103,
        "name": "Zinger Burger",
        'price': 18,
        "stock": 13,
    },
    {
        "id": 104,
        "name": "Cheeseburger",
        'price': 9,
        "stock": 4,
    },
    {
        "id": 105,
        "name": "Veg Burger",
        'price': 8,
        "stock": 21,
    },
]
Combo_Meals = [
    {
        "id": 106,
        "name": "Chicken Burger Combo",
        'price': 15,
        "stock": 18,
    },
    {
        "id": 107,
        "name": "Beef Burger Combo",
        'price': 20,
        "stock": 2,
    },
    {
        "id": 108,
        "name": "Zinger Burger Combo",
        'price': 22,
        "stock": 1,
    },
]
Drinks = [
    {
        "id": 109,
        "name": "Original Hot Coffee",
        'price': 10,
        "stock": 48,
    },
    {
        "id": 110,
        "name": "Iced Latte",
        'price': 20,
        "stock": 22,
    },
    {
        "id": 111,
        "name": "Pepsi",
        'price': 4,
        "stock": 80,
    },
    {
        "id": 112,
        "name": "Water",
        'price': 2,
        "stock": 113,
    },
]
Add_Ons = [
    {
        "id": 113,
        "name": "Extra Fries",
        'price': 10,
        "stock": 8,
    },
    {
        "id": 114,
        "name": "Cheeseballs",
        'price': 8,
        "stock": 12,
    },
    {
        "id": 115,
        "name": "Chicken Nuggets",
        'price': 14,
        "stock": 19,
    },
    {
        "id": 116,
        "name": "Cookie",
        'price': 5,
        "stock": 57,
    },
]

quit = False
the_item = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

def machine(Menu,quit,the_item):
    while quit == False:
        print("Welcome to Burgermania!\nHere is what we have to ofFer:")
        print("1 - Burgers\n2 - Combo Meals\n3 - Drinks\n4 - Add Ons")
        order_pt1=int(input("Enter the number associated with each category to browse its menu."))

        def your_order(category):
            order = int(input("Enter the ID of the item you want to order: "))
            if order in category:
                the_item.append(category[order])
                category['stock'] -= 1
            
            else:
                print('This code is invalid.')
            order = input("To quit the machine enter q and to continue buying enter anything: ")

        def Menu(list):
            for i in list:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")
        
        if order_pt1>4 or order_pt1<1:
            print("This number is invalid")
        elif order_pt1==1:
            print("Burgers:")
            Menu(Burgers)
            your_order(Burgers)
        elif order_pt1==2:
            print("Combo Meals:")
            Menu(Combo_Meals)
            your_order(Combo_Meals)
        elif order_pt1==3:
            print("Drinks:")
            Menu(Drinks)
            your_order(Drinks)
        else:
            print("Add Ons:")
            Menu(Add_Ons)
            your_order(Add_Ons)
        
        while more_items!="q":
            more_items = str(input("press any key to add more items and press q to quit.. "))
        if more_items == "q":
            quit=True
        
        print(sum(the_item))
        print(create_reciept(the_item, reciept))

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
    return reciept

if __name__ == "__main__":
    machine(Menu,quit,the_item) 