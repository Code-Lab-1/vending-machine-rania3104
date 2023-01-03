#Rania Aziz Farooqi
#Storing the menu indicating different categories of food.
Burgers=[{
    "id": 0, #ID Number
    "name": "Chicken Burger", 
    'price': 10,
    },
{
    "id": 1,
    "name": "Beef Burger",
    'price': 13,
    },
{
    "id":2,
    "name": "Zinger Burger",
    'price': 18,
    },
{
    "id": 3,
    "name": "Cheeseburger",
    'price': 9,
    },]
Drinks=[{
    "id": 4,
    "name": "Original Hot Coffee",
    'price': 10,
    },
{
    "id": 5,
    "name": "Iced Latte",
    'price': 20,
    },
{
    "id": 6,
    "name": "Pepsi",
    'price': 4,
    },
{
    "id": 7,
    "name": "Water",
    'price': 2,
    },]
Add_Ons=[{
    "id": 8,
    "name": "Extra Fries",
    'price': 10,
    },
{
    "id": 9,
    "name": "Cheeseballs",
    'price': 8,
    },
{
    "id": 10,
    "name": "Chicken Nuggets",
    'price': 14,
    },
{
    "id": 11,
    "name": "Cookie",
    'price': 5,
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

def machine(quit,the_item):
    while quit == False:

        order = int(input("Enter the ID of the item you want to order: "))
        if (order <3 or order ==3):
            the_item.append(Burgers[order])
        elif (order <7 or order ==7):
            the_item.append(Drinks[order-4])
        elif order <11 or order ==11:
            the_item.append(Add_Ons[order-8])         
        else:
            print('This code is invalid.')
        
        print("Your order till now: ")  
        for i in the_item:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']}")    

        more_items = str(input("Enter to add more items or press q to quit.. "))
        if more_items == "q":
            quit=True
        
    print("Here is the total: ",sum(the_item))
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
    machine(quit,the_item) 