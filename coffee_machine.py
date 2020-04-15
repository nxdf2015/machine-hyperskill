# Write your code her

recipes={
            "espresso":{
                "water":250,
                "milk":0,
                "bean":16,
                "price":4
            },
             "latte":{
                "water":350,
                "milk":75,
                "bean":20,
                "price":7
            },
             "cappuccino":{
                "water":200,
                "milk":100,
                "bean":12,
                "price":6
            },
        }

#list coffee available
coffees="espresso latte cappuccino".split(" ")


def getQuantity(msg):
    return int(input(msg))


def fill_machine():
   return  {"water" : getQuantity("Write how many ml of water the coffee machine has:"),
     "milk": getQuantity("Write how many ml of milk the coffee machine has:"),
     "bean": getQuantity("Write how many grams of coffee beans do you want to add:"),
     "cup":getQuantity("Write how many cups of coffee do you want to add:")
     }


def verify(n,ingredients):
    """
    verify if it is possble to make n cups with ingredients available
    """

    m= min(ingredients["water"]//200 , ingredients["milk"]//50 , ingredients["bean"]//15)
    if m < n:
        print(f"No, I can make only {m} cups of coffee")
    elif m == n:
        print("Yes, I can make that amount of coffee")
    else:
        print(f"Yes, I can make that amount of coffee (and even {m-n} more than that")


def verify_validity(coffee,state):
    for ingredient in ["water","milk","bean"]:
        if state[ingredient] < recipes[coffee][ingredient]:
            print(f"Sorry, not enough {ingredient}!")
            return False
        print("I have enough resources, making you a coffee!")
        return True


def coffeeMachine():
    ingredients=fill_machine()
    n = int(input("write how many cups of coffee you will need:"))
    verify(n,ingredients)

def buyCoffee():
    try:
        choice=int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        return coffees[choice - 1]
    except:
        return "back"




def updateState(action,state,selected=""):
    """
    :param action: fill buy take
    :param state:  { water , milk , bean, cup , money }
    :param selected:
    :return: state updated
    """
    if action == "buy":
        for type in ["water","milk","bean"]:
            state[type] -= recipes[selected][type]
        state["money"]+=recipes[selected]["price"]
        state["cup"]-=1

    elif action == "fill":
        for type in ["water","milk","bean","cup"]:
            state[type]+=selected[type]
    else:
        state["money"]=0

    return state


def actions(state,action):

    if action=="remaining":
        render_state(state)

    elif action=="buy":
        coffeeSelected=buyCoffee()

        if  coffeeSelected in coffees and verify_validity(coffeeSelected,state):
            state=updateState("buy",state,coffeeSelected)

    elif action=="fill":
        amountIngredients=fill_machine()
        state=updateState("fill",state,amountIngredients)

    elif action=="take":
        amount=state["money"]
        state=updateState("take",state)
    return state


def render_state(state):

    print(f'''The coffee machine has:
{state["water"]} of water
{state["milk"]} of milk
{state["bean"]} of coffee beans
{state["cup"]} of disposable cups
${state["money"]} of money''')

def coffee_machine(state):
     # render_state(state)
     # print()
     while True:

         action=input("Write action (buy, fill, take, remaining, exit)")
         print()
         if action=="exit":
             break
         state=actions(state,action)
         print()
         #render_state(state)




if __name__=="__main__":
    #initial state coffee machine
    state={
        "water":400,"milk":540,"bean":120,"money":550,"cup":9
    }
    coffee_machine(state)


