from animal_class import *
class Cow(Animal):
    """A Cow Class"""

    def __init__(self):
        super().__init__(9,250,1,8)
        self._type = "Cow"

    def grow(self,food_need,water_need):
        if food_need >= self._food_need and water_need >= self._water_need:
            if self._status == "Baby" and water_need > self._water_need:
                self._growth += self._growth_rate * 2
            elif self._status == "Toddler" and water_need > self._water_need:
                self._growth += self._growth_rate * 1.5
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()

def main():
    cow_animal = Cow()
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
