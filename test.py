#Rania Aziz Farooqi
#Storing the menu indicating different categories of food.
Burgers=[{
    "id": 0, #ID Number
    "name": "Chicken Burger", 
    'price': 10,
    'stock':12
    },
{
    "id": 1,
    "name": "Beef Burger",
    'price': 13,
    'stock':2
    },
{
    "id":2,
    "name": "Zinger Burger",
    'price': 18,
    'stock':4
    },
{
    "id": 3,
    "name": "Cheeseburger",
    'price': 9,
    'stock':6
    },]
Drinks=[{
    "id": 4,
    "name": "Original Hot Coffee",
    'price': 10,
    'stock':10
    },
{
    "id": 5,
    "name": "Iced Latte",
    'price': 20,
    'stock':7
    },
{
    "id": 6,
    "name": "Pepsi",
    'price': 4,
    'stock':1
    },
{
    "id": 7,
    "name": "Water",
    'price': 2,
    'stock':20
    },]
Add_Ons=[{
    "id": 8,
    "name": "Extra Fries",
    'price': 10,
    'stock':15
    },
{
    "id": 9,
    "name": "Cheeseballs",
    'price': 8,
    'stock':19
    },
{
    "id": 10,
    "name": "Chicken Nuggets",
    'price': 14,
    'stock':5
    },
{
    "id": 11,
    "name": "Cookie",
    'price': 5,
    'stock':16
    }
]

Menu =[Burgers,Drinks,Add_Ons]
def Conversion_of_dict_to_list(dict):
    list(dict.keys())[list(dict.values()).index(val)]


quit = False
full_order = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

print("Welcome to Burgermania!\nHere is what we have to ofFer:")
print("\n1 - Burgers")
for i in Burgers:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
print("2 - Drinks")
for i in Drinks:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
print("3 - Add Ons")
for i in Add_Ons:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")

def machine(quit,full_order):
    while quit == False:

        order = int(input("Enter the ID of the item you want to order: "))
        if (order <3 or order ==3):
            full_order.append(Burgers[order])
            if full_order['stock']==0:
                print("Sorry this item is out of stock!")
            else: 
                full_order['stock'] -= 1
        elif (order <7 or order ==7):
            full_order.append(Drinks[order-4])
        elif order <11 or order ==11:
            full_order.append(Add_Ons[order-8])       
        else:
            print('\nThis code is invalid.')

        
        print("\nYour order till now: ")  
        for i in full_order:
            print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")    

        more_items = str(input("Enter to add more items or press q to quit.. "))
        if more_items == "q":
            quit=True
        
    print("\nHere is the total:",sum(full_order),"AED")
    balance= int(input("Please enter the cash amount."))
    if balance>sum(full_order):
        change=balance-sum(full_order)
        print("\nYour order has been dispensed.\nHere is your change:",change,"AED.","\n\nHere is your receipt! ")
    print(create_reciept(full_order, reciept))

def sum(full_order):
    sum = 0

    for i in full_order:
        sum += i["price"]

    return sum

def create_reciept(full_order, reciept):

    for i in full_order:
        reciept += f"""
        \t{i["name"]} -- {i['price']}
        """

    reciept += f"""
        \tTotal --- {sum(full_order)}
        
        
        """
    return reciept

if __name__ == "__main__":
    machine(quit,full_order) 