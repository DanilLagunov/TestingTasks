class Person:
    def __init__(self, salary):
        '''Пример инкапсуляции: __age - закрытый атрибут'''
        Person.salary = salary
        self.__age = 33
    ''' Пример полиморфизма '''
    def work(self):
        self._work = 'Работает'
        return self._work


class Programmer(Person):  #Пример наследования

    def __init__(self, salary):
        Person.__init__(self, salary)
        Programmer.salary = Person.salary * 1.3
    def work(self):
        self._work = 'Программирует'
        return self._work
    def info(self):
        print('Должность: Программист\nРабота: {}\nЗароботная плата: {}$'.format(self.work(),self.salary))


class Junior_Programmer(Programmer):

    def __init__(self, salary):
        Programmer.__init__(self, salary)
        self.salary = Programmer.salary * 0.7

    def work(self):
        self._work = 'Программирует на начальном уровне'
        return self._work
    def info(self):
        print('Должность: Junior-программист\nРабота: {}\nЗароботная плата: {}$'.format(self.work(),self.salary))

p = Person(500)
pr = Programmer(Person.salary)
j = Junior_Programmer(Programmer.salary)
pr.info()
j.info()