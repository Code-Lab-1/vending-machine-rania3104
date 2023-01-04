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
full_order = []

reciept = """
\t\tITEM -- PRICE
\n"""

total = 0

print("Welcome to Burgermania!\nHere is what we have to ofFer:")
print("\n1 - Burgers")
for i in Burgers:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
print("\n2 - Drinks")
for i in Drinks:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
print("\n3 - Add Ons")
for i in Add_Ons:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")

def machine(quit,full_order):
    def ordering(quit,full_order):
        while quit == False:
            order = int(input("Enter the ID of the item you want to order: "))
            if (order <3 or order ==3):
                full_order.append(Burgers[order])
            elif (order <7 or order ==7):
                full_order.append(Drinks[order-4])
            elif (order <11 or order ==11):
                full_order.append(Add_Ons[order-8])         
            else:
                print('\nThis code is invalid.')
        
            print("\nYour order till now: ")  
            for i in full_order:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")  
            more_items = str(input("\nEnter to add more items or press q to quit.. "))
            if more_items == "q":
                quit=True

    def suggestions(full_order):
        print("\nYou may also like:")
        if Burgers in full_order:
            for i in Drinks and Add_Ons:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
        elif Drinks in full_order:
            for i in Burgers and Add_Ons:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
        else:
            for i in Add_Ons:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
    
    ordering(quit,full_order)
    suggestions(full_order)
    more_items = str(input("\nEnter if you still want to buy more or press q to quit.. "))
    if more_items == "q":
        quit=True
    else: 
        ordering(quit,full_order)
    
    def sum(full_order):
        total= 0

        for i in full_order:
            total += i["price"]

        return total
    
    def create_reciept(full_order, reciept):

        for i in full_order:
            reciept += f"""
            \t{i["name"]} -- {i['price']} AED
            
            """

        reciept += f"""
            \tTotal --- {sum(full_order)} AED
            """
        reciept += f"""
            \tAmount Paid --- {amount_paid} AED
            """
        reciept += f"""
            \tBalance --- {change} AED
            """
        return reciept

    print("\nHere is the total:",sum(full_order),"AED")
    amount_paid= int(input("Please enter the cash amount."))
    if amount_paid>sum(full_order):
        change=amount_paid-sum(full_order)
        print("\nYour order has been dispensed.\nHere is your change:",change,"AED.","\n\nHere is your receipt! ")
    print(create_reciept(full_order, reciept))


if __name__ == "__main__":
    machine(quit,full_order) 