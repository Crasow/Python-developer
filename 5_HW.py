class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашем')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')


obj1 = Stationery('персонаж')
obj2 = Handle('персонаж')
obj3 = Pencil('машина')
obj4 = Pen('машина')
obj1.draw()
obj2.draw()
obj3.draw()
obj4.draw()
