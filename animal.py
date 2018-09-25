class Animals:
    def __init__(self,growth_rate,water_need,food_need):
        self._growthrate = growth_rate
        self._water_need = water_need
        self._food_need = food_need
        self._stage = "birth"
        self._growth = 0
        self._age = 0
    def need(self):
        return {'water-need':self._water_need,'food-need':self._food_need}
    def report(self):
        report = {'stage':self._stage,'growth':self._growth,'age':self._age}
        return report['stage']
    def _update_stage(self):
        if self._growth > 10:
            self._stage ='old'
        elif self._growth > 5:
            self._stage ="aduldhood"
        elif self._growth > 0:
            self._stage= 'adolescence'
        elif self._growth == 0:
            self._stage = "birth"
    def Grow(self,food,water):
        if food >=self._food_need and water >= self._water_need:
            self._growth  += self._growthrate
            self._age += 1
            self._update_stage()
        
def main():
    print("COW :")
    print()
    cow = Animals(1,3,4)
    print(cow.need())
    print(cow.report())
    cow.Grow(4,4)
    print(cow.report())
    print('SHEEP')
    print()
    Sheep = Animals(1,2,3)
    print(Sheep.need())
    print(Sheep.report())
    Sheep.Grow(10,10)
    print(Sheep.report())

    
if __name__ == "__main__":
    main()
    




            