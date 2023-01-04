#Rania Aziz Farooqi
#Storing the menu indicating different categories of food.
Burgers=[{#list containing dictionaries of items according to the category 
    "id": 0, #ID Number
    "name": "Chicken Burger", #name of the item
    'price': 10, #price
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
Drinks=[{#second category
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
Add_Ons=[{#third category
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

Menu =[Burgers,Drinks,Add_Ons] #complete menu is a list
def Conversion_of_dict_to_list(dict):
    list(dict.keys())[list(dict.values()).index(val)] #conversion of the above dictionaries to lists for easy use ahead


quit = False #assigning the variable quit to False
full_order = [] #creating an empty list to add the future orders in

receipt = """
\t\tITEM -- PRICE
\n""" #creating the variable for the reciept at the end of the program

total = 0 #assigning the total amount of money to 0

print("\nWelcome to Burgermania!\nHere is what we have to ofFer:") #opening message letting the user know the menu ahead
print("\n1 - Burgers")
for i in Burgers:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED") #loop to print the corresponding menu according to the category
print("\n2 - Drinks")
for i in Drinks:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
print("\n3 - Add Ons")
for i in Add_Ons:
    print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")

def machine(quit,full_order): #creating the main function of the machine
    def ordering(quit,full_order): #function that includes all the codes to order according to the menu
        while quit == False: #referring to the variable created above in a while loop to make sure the loop breaks when quit=True
            order = int(input("Enter the ID of the item you want to order: ")) #way of user to input their order using the Item id in the dictionary
            if (order <3 or order ==3):
                full_order.append(Burgers[order]) #adding the corresponding order to the empty list created above
            elif (order <7 or order ==7):
                full_order.append(Drinks[order-4])
            elif (order <11 or order ==11):
                full_order.append(Add_Ons[order-8])         
            else:
                print('\nThis code is invalid.') #message to let the user know that the code they entered is not part of the menu
        
            print("\nYour order till now: ")  #message that lets the user know their order with reference to the list full_order
            for i in full_order:
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")  #iterates the list full_order and prints it
            more_items = str(input("\nEnter to add more items or press q to quit: ")) #message to ask the user if they want to add anything else to their order
            if more_items == "q": #if the user typed 'q' in the previous command, the function's loop will break and the code will move forward
                quit=True

    def suggestions(full_order): #function to give suggestions to the user to buy anything else they may like
        print("\nYou may also like:")
        if Burgers in full_order:
            for i in Drinks and Add_Ons: #if the user ordered a burger, they will be suggested drinks and add ons
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
        elif Drinks in full_order:
            for i in Burgers and Add_Ons: #if the user ordered a drink, they will be suggested burgers and add ons
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
        else:
            for i in Drinks and Burgers: 
                print(f"Item ID: {i['id']} - Item Name: {i['name']} - Price: {i['price']} AED")
    
    ordering(quit,full_order) #calling the main function of ordering
    suggestions(full_order) #after the ordering function breaks , suggestions function is called
    more_items = str(input("\nEnter if you still want to buy more or press q to quit: ")) #asks the user if they want to buy from suggestions or not
    if more_items == "q": #if the user inputs 'q' the function will break and the code will move forward
        quit=True
    else: #else the code will go back to the ordering function
        ordering(quit,full_order)
    
    def sum(full_order): #function for the total amount owed
        total= 0

        for i in full_order:
            total += i["price"] #adds all the prices in the list full_order

        return total
    
    def create_receipt(full_order, receipt): #function to create the receipt

        for i in full_order: #for loop that iterates throught the list full_ order and prints it all
            receipt += f"""
            \t{i["name"]} -- {i['price']} AED
            
            """

        receipt += f"""
            \tTotal --- {sum(full_order)} AED
            """#prints the total
        receipt += f"""
            \tAmount Paid --- {amount_paid} AED
            """#prints the amount of money paid
        receipt += f"""
            \tBalance --- {change} AED
            """#prints the balance owed
        return receipt

    

    print("\nHere is the total:",sum(full_order),"AED") #prints the total
    amount_paid= int(input("Please enter the cash amount: ")) #asks the user to input their desired amount of money
    if amount_paid<sum(full_order): 
        #if the user enters less money than stated in their full_order a message will display to add more
        extra_amount=int(input("Insufficient money, please add more: ")) 
        amount_paid+=extra_amount #the amount entered by the user will be store in the same variable until it reaches the exact amount or more

        #when the variable amount_paid is more than or equal to the total of the order the code will move forward
        if amount_paid==sum(full_order) or amount_paid>sum(full_order): 
            change=amount_paid-sum(full_order) #calculation of the change
            #message telling the user their order is despensed and giving them their change and receipt
            print("\nYour order has been dispensed.\nHere is your change:",change,"AED.","\n\nHere is your receipt! ")
            print(create_receipt(full_order, receipt)) #calling the function of creating receipt from above


if __name__ == "__main__": #code that runs the program when the main function machine is called
    machine(quit,full_order) 