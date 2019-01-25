# -*- coding:utf-8 -*-


class Animal(object):

    def __init__(self, _name, _weight):
        self.__name = _name
        self.__weight = _weight
        self.__satiety = 0

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isalpha():
            self.__name = value
        else:
            print("Bad name!")

    @property
    def satiety(self):
        return self.__satiety

    def give_voice(self):
        raise Exception("NotImplementedException")

    def give_food(self, food):
        self.__satiety += food

    def __str__(self):
        return """
                            Экземпляр класса {0}.
                            Имя экземпляра  "{1}".
                            Вес экземпляра  {2} кг.
                            Сытость экземпляра: {3}.
""".format(self.__class__.__name__, self.__name, self.__weight, self.__satiety)


class MilkAnimals(object):
    def __init__(self):
        self.__milk_amount = 0

    @property
    def milk_amount(self):
        return self.__milk_amount

    def get_milk(self, name, liters):
        print("Начинаем доить животное...")
        self.__milk_amount += liters
        print(""" "{0}" подоили. Получили {1} литров молока.\n
        """.format(name, self.__milk_amount))


class OviparousAnimals(object):
    def __init__(self):
        self.__eggs_amount = 0

    @property
    def eggs_amount(self):
        return self.__eggs_amount

    def gather_eggs(self, name, eggs):
        print("Начинаем собирать яйца...")
        self.__eggs_amount += eggs
        print("\"{0}\" снесла {1} яиц!\n".format(name, self.eggs_amount))


class WoolAnimals(object):
    def __init__(self):
        self.__wool_amount = 0

    @property
    def wool_amount(self):
        return self.__wool_amount

    def gather_wool(self, name, wool):
        print("Начинаем стричь шерсть...")
        self.__wool_amount += wool
        print("C \"{0}\" состригли {1} кг шерсти.\n".format(name, self.wool_amount))


class GooseFemale(Animal, OviparousAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        OviparousAnimals.__init__(self)

    def give_voice(self):
        print("Га га га!")


class GooseMale(Animal):
    def __init__(self, _name, _weight):
        super().__init__(_name, _weight)

    def give_voice(self):
        print("Га га га!")

    def defend_family(self):
        print("{0} защищает территорию!".format(self.name))
        self.give_voice()
        print("Моя территория! Не приближаться!\n")


class CowFemale(Animal, MilkAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        MilkAnimals.__init__(self)

    def give_voice(self):
        print("Мууууууу!")


class Sheep(Animal, WoolAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        WoolAnimals.__init__(self)

    def give_voice(self):
        print("Бееееее!")


class ChickenFemale(Animal, OviparousAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        OviparousAnimals.__init__(self)

    def give_voice(self):
        print("Ко ко ко!")


class ChickenMale(Animal):
    def __init__(self, _name, _weight):
        super().__init__(_name, _weight)

    def give_voice(self):
        print("Ку-ка-ре-ку!")

    def defend_family(self):
        print("\"{0}\" защищает территорию!".format(self.name))
        self.give_voice()
        print("Моя территория! Не приближаться!\n")


class GoatFemale(Animal, MilkAnimals, WoolAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        MilkAnimals.__init__(self)
        WoolAnimals.__init__(self)

    def give_voice(self):
        print("Меееее!")


class DuckFemale(Animal, OviparousAnimals):
    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        OviparousAnimals.__init__(self)

    def give_voice(self):
        print("Кря кря кря!")


def get_common_weight(*args):
    common_weight = 0

    for arg in args:
        common_weight += arg

    return common_weight


def get_the_heaviest_animal(**animals):

    maximim_weight = 0
    result = ""

    for (animal_name, animal_weight) in animals.items():

        if animal_weight > maximim_weight:
            maximim_weight = animal_weight
            result = animal_name

    return result


if __name__ == "__main__":

    male_goose = GooseMale("Серый", 3.5)
    male_goose.give_food(34)
    male_goose.defend_family()

    female_goose = GooseFemale("Белая", 4)
    female_goose.give_food(25)
    female_goose.gather_eggs(female_goose.name, 5)

    female_cow = CowFemale("Манька", 350)
    female_cow.get_milk(female_cow.name, 15)

    sheep_1 = Sheep("Барашек", 10)
    sheep_1.gather_wool(sheep_1.name, 1.5)

    sheep_2 = Sheep("Кудрявый", 10)
    sheep_2.gather_wool(sheep_2.name, 1.3)

    female_goat_roga = GoatFemale("Рога", 20)
    female_goat_roga.get_milk(female_goat_roga.name, 7)
    female_goat_roga.gather_wool(female_goat_roga.name, 2)

    female_goat_kopyta = GoatFemale("Копыта", 18)
    female_goat_kopyta.get_milk(female_goat_kopyta.name, 5)
    female_goat_kopyta.gather_wool(female_goat_kopyta.name, 1.5)

    female_chicken = ChickenFemale("Ко-Ко", 2)
    female_chicken.gather_eggs(female_chicken.name, 5)

    male_chicken = ChickenMale("Кукареку", 4)
    male_chicken.defend_family()

    female_duck = DuckFemale("Кряква", 6)
    female_duck.gather_eggs(female_duck.name, 6)

    all_obj = [
                    male_goose, female_goose, female_cow, female_goat_roga,
                    female_goat_kopyta, female_chicken, male_chicken, female_duck,
                    sheep_1, sheep_2]

    for obj in all_obj:
        print(obj)
        print("\"{0}\" издает звуки....".format(obj.name))
        obj.give_voice()

    obj_attr = {obj.name: obj.weight for obj in all_obj}

    total = get_common_weight(*obj_attr.values())

    max_weight = get_the_heaviest_animal(**obj_attr)

    print("Общий вес всех животных равен {0} кг.".format(total))
    print("Самое тяжелое животное -  {0}.".format(max_weight))
