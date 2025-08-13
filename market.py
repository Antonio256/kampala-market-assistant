#function to calculate total bill for a shopping list

produce = {
    "mango": {
        "price":2500,
        "stock": 15 
    },
    "orange": {
        "price": 2000,
        "stock": 20
    },
    "banana": {
        "price": 5000,
        "stock": 10
    },
    "onions": {
        "price": 2200,
        "stock": 20
    }
    
}

shopping_list = ["mango", "orange", "banana", "apple", "onions"]

total_cost = 0

for item in shopping_list:
    if item in produce:
        print(f"Adding {item} to the cart")
        
        total_cost += produce[item]["price"]
    else:
        print(f"We are out of stock for {item}")


print(f"Your total bill is UGX : {total_cost}")



# the re-usable function 
produce_items = {
    "mango": {
        "price":2500,
        "stock": 15 
    },
    "orange": {
        "price": 2000,
        "stock": 20
    },
    "banana": {
        "price": 5000,
        "stock": 10
    },
    "onions": {
        "price": 2200,
        "stock": 20
    },
    "melons": {
        "price": 2200,
        "stock": 0
    }
    
}

customer_list = ["mango", "orange", "banana", "apple", "onions", "mellons"]


def calculate_bill(produce_items, customer_list):
    total_cost = 0
    
    for item in customer_list:
        if item in produce_items:
            if produce_items[item]["stock"] > 0: #Checking for stock availability
                print(f"Adding {item} to the cart")
        
                total_cost += produce_items[item]["price"]
                produce_items[item]["stock"] -= 1 #reduce stock
        else:
            print(f"Sorry. {item} is currently out of stock")
    return total_cost

fina_bill = calculate_bill(produce_items, customer_list)
print(f"The final bill is UGX: {fina_bill}")
