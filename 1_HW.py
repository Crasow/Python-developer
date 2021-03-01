from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for color in TrafficLight.__color:
            print(f'Цвет светофора сейчас {color}')
            if color == TrafficLight.__color[0]:
                sleep(7)
            elif color == TrafficLight.__color[1]:
                sleep(2)
            elif color == TrafficLight.__color[2]:
                sleep(4)


light = TrafficLight()
light.running()
