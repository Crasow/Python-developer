class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn_right(self):
        print(f'Машина {self.name} повернула на право')

    def turn_left(self):
        print(f'Машина {self.name} повернула на лево')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')

        if self.speed > 60:
            print(f'Сбавь скорость до 60 км/ч!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed} км/ч')

        if self.speed > 40:
            print(f'Сбавь скорость до 40 км/ч!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


toyota = SportCar(99, 'Red', 'Toyota', False)
daewoo = TownCar(43, 'Blue', 'Daewoo', False)
lada = WorkCar(89, 'White', 'Lada', False)
nissan = PoliceCar(200, 'Purple', 'Nissan', True)
lada.turn_left()
nissan.go()
nissan.show_speed()
daewoo.stop()
lada.show_speed()
