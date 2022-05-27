'''
Создайте класс Dog, родительским классом которого является класс Animal.
В классе Dog выполните переопределение метода say, чтобы он возвращал строку "Woof"
для экземпляров класса Dog.
В конструкторе класса Dog введите новое свойство breed — порода, при этом должны остаться все свойства,
наследуемые от класса Animal.
Создайте в коде следующий экземпляр класса Dog.
'''


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return f'Woof'


dog = Dog("Barbos", 23, "labrador")
