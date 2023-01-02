#Rania Aziz Farooqi
#Storing the menu indicating different categories of food.
Burgers=[{
    "id": 101, #ID Number
    "name": "Chicken Burger", 
    'price': 10,
    "stock": 29
    }, #The amount that is is in stock
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
    "stock": 13
    },
{
    "id": 104,
    "name": "Cheeseburger",
    'price': 9,
    "stock": 4,
    },]
Drinks=[{
    "id": 105,
    "name": "Original Hot Coffee",
    'price': 10,
    "stock": 48,
    },
{
    "id": 106,
    "name": "Iced Latte",
    'price': 20,
    "stock": 22,
    },
{
    "id": 107,
    "name": "Pepsi",
    'price': 4,
    "stock": 80,
    },
{
    "id": 108,
    "name": "Water",
    'price': 2,
    "stock": 0,
    },]
Add_Ons=[{
    "id": 109,
    "name": "Extra Fries",
    'price': 10,
    "stock": 8,
    },
{
    "id": 110,
    "name": "Cheeseballs",
    'price': 8,
    "stock": 12,
    },
{
    "id": 111,
    "name": "Chicken Nuggets",
    'price': 14,
    "stock": 19,
    },
{
    "id": 112,
    "name": "Cookie",
    'price': 5,
    "stock": 57,
    }
]

Menu =[Burgers,Drinks,Add_Ons]
def Conversion_of_dict_to_list(dict):
    list(dict.keys())[list(dict.values()).index(val)]


quit = False
the_item = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

def machine(Menu,quit,the_item):
    while quit == False:
        print("Welcome to Burgermania!\nHere is what we have to ofFer:")
        
        print("1 - Burgers")
        for i in Burgers:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")
        print("2 - Drinks")
        for i in Drinks:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")
        print("3 - Add Ons")
        for i in Add_Ons:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")
        
        order = int(input("Enter the ID of the item you want to order: "))

        def your_order(category):
            if order in category:
                the_item.append(category.values(order))
                category['stock'] -= 1
                if category['stock']==0:
                    print("Sorry the item you requested for is currently out of stock.")
            else:
                print('This code is invalid.')
        question = input("To quit the machine enter q and to continue buying enter anything: ")
        
        your_order(Menu)

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