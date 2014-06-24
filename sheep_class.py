from animal_class import *
class Sheep(Animal):
    """A Sheep Class"""

    def __init__(self):
        super().__init__(9,250,1,8)
        self._type = "Sheep"

    def grow(self,food_need,water_need):
        if food_need >= self._food_need and water_need >= self._water_need:
            if self._status == "Baby" and water_need > self._water_need:
                self._weight += self._growth_rate * 2
            elif self._status == "Toddler" and water_need > self._water_need:
                self._weight += self._growth_rate * 1.5
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self.update_status()

def main():
    sheep_animal = Cow()
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
