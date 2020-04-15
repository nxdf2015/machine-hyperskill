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



def verify_validity(coffee,state):
    for ingredient in ["water","milk","bean"]:
        if state[ingredient] < recipes[coffee][ingredient]:
            print(f"Sorry, not enough {ingredient}!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

def buyCoffee():
    try:
        choice=int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        return coffees[choice - 1]
    except:
        return "back"





def render_state(state):

    print(f'''The coffee machine has:
{state["water"]} of water
{state["milk"]} of milk
{state["bean"]} of coffee beans
{state["cup"]} of disposable cups
${state["money"]} of money''')

class Machine:

    def __init__(self,state):
        """
        state={water,cup,milk,money}
        """
        self.state=state

    def start(self):
         while True:
             action=input("Write action (buy, fill, take, remaining, exit)")
             print()
             if action=="exit":
                 break
             self.actions(action)
             print()

    def actions(self,action):
        if action=="remaining":
            render_state(self.state)

        elif action=="buy":
            coffeeSelected=buyCoffee()
            if  coffeeSelected in coffees and verify_validity(coffeeSelected,self.state):
                self.state=self.updateState("buy",coffeeSelected)

        elif action=="fill":
            amountIngredients=fill_machine()
            self.state=self.updateState("fill",amountIngredients)

        elif action=="take":
           # amount=self.state["money"]
            self.state=self.updateState("take")

    def updateState(self,action,selected=""):
        """
        :param action: fill buy take
        :param state:  { water , milk , bean, cup , money }
        :param selected:
        :return: state updated
        """
        if action == "buy":
            for type in ["water","milk","bean"]:
                self.state[type] -= recipes[selected][type]
            self.state["money"]+=recipes[selected]["price"]
            self.state["cup"]-=1

        elif action == "fill":
            for type in ["water","milk","bean","cup"]:
                self.state[type]+=selected[type]
        else:
            self.state["money"]=0

        return state



if __name__=="__main__":
    #initial state coffee machine
    state={
        "water":400,"milk":540,"bean":120,"money":550,"cup":9
    }
    machine=Machine(state)
    machine.start()


