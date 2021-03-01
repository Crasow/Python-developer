class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_count(self, mass_for_m, thickness):
        return self._length * self._width * mass_for_m * thickness


road = Road(2, 2)
print(road.mass_count(4, 5))
