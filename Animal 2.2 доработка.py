# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class AbstractAnimal(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, _weight):
        self.__name = name
        self.__weight = _weight
        self.__satiety = 0
        self.__gathered_items = 0

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

    @property
    def gathered_items(self):
        return self.__gathered_items

    @gathered_items.setter
    def gathered_items(self, value):
        try:
            if value >= 0:
                self.__gathered_items = value
        except TypeError:
            print("Недопустимые входные данные!")

    @abstractmethod
    def give_voice(self):
        raise NotImplementedError

    @abstractmethod
    def gather_items(self, item_amount):
        raise NotImplementedError

    def give_food(self, food):
        self.__satiety += food
        print("""Животное "{0}" съело {1} кг корма.""".format(self.name, food))

    def __str__(self):
        return """
                            Экземпляр класса {0}.
                            Имя экземпляра  "{1}".
                            Вес экземпляра  {2} кг.
                            Сытость экземпляра {3}.
                            Собрано продукции {4}.
        """.format(
                            self.__class__.__name__,
                            self.name,
                            self.weight,
                            self.satiety,
                            self.gathered_items)


class Cow(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Муууу!")

    def gather_items(self, litters):
        print("Начинаем доить животное...")
        self.gathered_items += litters
        print(""" Животное "{0}" подоили. Получили {1} литров молока.\n
        """.format(self.name, self.gathered_items))


class Bull(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Муууу!")
    
    def gather_items(self, horns):
        print("Начинаем собирать рога...")
        self.gathered_items += horns
        print(""" Собрали рога у "{0}" . Получили {1} кг.\n
        """.format(self.name, self.gathered_items))


class Goose(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Га-га-га!!")

    def gather_items(self, eggs):
        print("Начинаем собирать яйца...")
        self.gathered_items += eggs
        print(""" У \"{0}\" собрали яйца. Собрали {1} шт.\n
        """.format(self.name, self.gathered_items))


class GooseMale(AbstractAnimal):
    def __init__(self, name, _weight):
        super().__init__(name, _weight)

    def give_voice(self):
        print("Га-га-га!!")
    
    def defend_family(self):
        print("{0} защищает территорию!".format(self.name))
        self.give_voice()
        print("Моя территория! Не приближаться!\n")

    def gather_items(self, nap):
        print("Начинаем собирать пух...")
        self.gathered_items += nap
        print(""" У {0} собрали пух. Собрано {1} гр.\n
        """.format(self.name, self.gathered_items))


class Sheep(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Бееееее!")

    def gather_items(self, wool):
        print("Начинаем стричь животное...")
        self.gathered_items += wool
        print(""" Животное "{0}" подстригли. Получили {1} кг шерсти.\n
        """.format(self.name, self.gathered_items))


class Chicken(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Ко ко ко!")

    def gather_items(self, eggs):
        print("Начинаем собирать яйца...")
        self.gathered_items += eggs
        print(""" У {0} собрали яйца. Собрали {1} шт.\n
        """.format(self.name, self.gathered_items))


class Cock(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        
    def give_voice(self):
        print("Ку-ка-ре-ку!")

    def defend_family(self):
        print("{0} защищает территорию!".format(self.name))
        self.give_voice()
        print("Моя территория! Не приближаться!\n")

    def gather_items(self, pen):
        print("Начинаем собирать перья...")
        self.gathered_items += pen
        print(""" У {0} собрали пух. Собрано {1} гр. перьев.\n
        """.format(self.name, self.gathered_items))


class GoatFemale(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Меееее!")
        
    def gather_items(self, litters):
        print("Начинаем доить животное...")
        self.gathered_items += litters
        print(""" Животное "{0}" подоили. Получили {1} литров молока.\n
        """.format(self.name, self.gathered_items))


class Duck(AbstractAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def give_voice(self):
        print("Кря кря кря!")
        
    def gather_items(self, eggs):
        print("Начинаем собирать яйца...")
        self.gathered_items += eggs
        print(""" У {0} собрали яйца. Собрали {1} шт.\n
        """.format(self.name, self.gathered_items))


def get_common_weight(*args):
    common_weight = 0

    for arg in args:
        common_weight += arg

    return common_weight


def get_the_heaviest_animal(**animals):

    maximum_weight = 0
    result = ""

    for (name, weight) in animals.items():

        if weight > maximum_weight:
            maximum_weight = weight
            result = name

    return result


if __name__ == "__main__":

    goose_m = GooseMale("Серый", 3.5)
    goose_m.defend_family()

    goose_f = Goose("Белая", 4)

    cow = Cow("Манька", 350)
    bull = Bull("Вася", 450)

    sheep_1 = Sheep("Барашек", 10)
    sheep_2 = Sheep("Кудрявый", 10)

    goat_1 = GoatFemale("Рога", 20)

    goat_2 = GoatFemale("Копыта", 18)

    chicken = Chicken("Ко-Ко", 2)

    cock = Cock("Кукареку", 4)
    cock.defend_family()

    duck = Duck("Кряква", 6)

    animals = [
                    goose_f, goose_m,
                    cow, bull,
                    sheep_1, sheep_2,
                    goat_1, goat_2,
                    chicken, cock,
                    duck, ]

    for animal in animals:
        animal.give_voice()
        animal.give_food(5)
        animal.gather_items(3)
        print(animal)

    animal_attr = {animal.name: animal.weight for animal in animals}

    total_weight = get_common_weight(*animal_attr.values())

    max_weight = get_the_heaviest_animal(**animal_attr)

    print("Общий вес всех животных равен {0} кг.".format(total_weight))
    print("Самое тяжелое животное -  {0}.".format(max_weight))
