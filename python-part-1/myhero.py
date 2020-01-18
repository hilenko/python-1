class myhero():
    """ Class to creater hero for my first game """
    def __init__(self, name, age, level, rank):
        """ Initial our hero """
        self.name = name
        self.age = age
        self.level = level
        self.rank = rank
        self.health = 100

    def show_myhero(self):
        """ Print all parametr myHERO """
        description = (self.name + ' Level is: ' + str(self.level) + ' Age is: ' + str(
            self.age) + ' Rank is: ' + self.rank + ' health is: ' + str(self.health)).title()
        print(description)

    def upgrage_level(self):
        """ Upgrade level of MYHero """
        print('level is upgraded on one point')
        self.level += 1

    def move(self):
        """ Start moving hero """
        print('Hero ' + self.name + 'start moving ...')

    def set_health(self, new_health):
        self.health = new_health

class SuperHero(myhero):
    """ Class creater super hero """
    def __init__(self, name, age, level, rank, magiclevel):
        """ Init out super hero """
        super().__init__(name, age, level, rank)
        self.magiclevel = magiclevel
        self.__magic = 100

    def makemagic(self):
        """ Use magic """
        self.__magic -= 10

    def show_myhero(self):
        """ Print all parametr myHERO """
        description = (self.name + ' Level is: ' + str(self.level) + ' Age is: ' + str(
            self.age) + ' Rank is: ' + self.rank + ' health is: ' + str(self.health) + ' magic is: ' + str(self.__magic)).title()
        print(description)