import random
class Animal():
    """An Animal Class"""
    def __init__(self,food_need,weight,growth_rate,water_need):
        self._food_need = food_need
        self._weight = weight
        self._days_growing = 0
        self._growth = 0
        self._growth_rate = growth_rate
        self._water_need = water_need
        self._type = "Generic"
        self._status = "Baby"

    def needs(self):
        return{"Food need":self._food_need, "Water need":self._water_need}
    
    def report(self):
        return {"Type":self._type, "Status":self._status, "Growth":self._growth_rate, "Days Growing":self._days_growing, "Weight":self._weight}

    def update_status(self):
        if self._growth > 20:
            self._status = "Old"
        if self._growth > 15:
            self._status = "Mature"
        elif self._growth > 10:
            self._status = "Teen"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Toddler"
        elif self._growth == 0:
            self._status = "Baby"            

    def grow(self, food_need, water):
        if food >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()

def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - PLease enter a new value between 1 and 10")
        except ValueError:
            print("Value entered not valid - PLease enter a new value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a new value between 1 and 10")
        except ValueError:
            print("Value entered not valid - Please enter a new value between 1 and 10")
    animal.grow(food,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option fromt the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal, 20)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")

def main():
    new_animal = Animal(8,50,1,6)
    manage_animal(new_animal)


if __name__ == "__main__":
    main()
            
            
        
