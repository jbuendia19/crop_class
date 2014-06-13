class Crop:
    """A generic food crop"""
    #constructor
    def __init__(self,growth_rate, light_need,water_need):
        #set the attributes with an initial value
        #_ = atrributes private
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #return a dictionary containing the light and water needs
        return {"light need": self._light_need, "water need":self._water_need}
    #method to report tje provide information about the current state of crop
    def report(self):
        #return a dictionary conatianing the type, stauts, growth and days growing
        return {"type":self._type, "status":self._status, "growth":self._growth, "days growing":self._days_growing}

def main():
    #instantiate the class
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())


if __name__ == "__main__":
    main()
