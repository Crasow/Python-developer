income_dict = {"wage": 5000, "bonus": 1500}


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return total_income


a = Position('Ilya', 'Getter', 'manager', 5000, 1500)
print(a.get_full_name())
print(a.get_total_income())
