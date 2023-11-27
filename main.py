class MobileOperator:
    def __init__(self, name, cost_per_minute, coverage_area):
        self.name = name
        self.cost_per_minute = cost_per_minute
        self.coverage_area = coverage_area

    def quality(self):
        return 100 * self.coverage_area / self.cost_per_minute

    def object_info(self):
        return f"Название оператора: {self.name}\nСтоимость 1 минуты разговора: {self.cost_per_minute}\nПлощадь покрытия: {self.coverage_area}\n"

class SubMobileOperator(MobileOperator):
    def __init__(self, name, cost_per_minute, coverage_area, P):
        super().__init__(name, cost_per_minute, coverage_area)
        self.P = P

    def quality(self):
        Q = super().quality()
        if self.P:
            return 0.7 * Q
        else:
            return 1.5 * Q

    def object_info(self):
        return f"{super().object_info()}Дополнительная плата за соединение: {self.P}\n"

# Создание объектов класса MobileOperator и SubMobileOperator с вводом данных
def create_mobile_operator():
    name = input("Введите название оператора: ")
    cost_per_minute = float(input("Введите стоимость 1 минуты разговора: "))
    coverage_area = float(input("Введите площадь покрытия: "))
    return MobileOperator(name, cost_per_minute, coverage_area)

def create_sub_mobile_operator():
    name = input("Введите название оператора: ")
    cost_per_minute = float(input("Введите стоимость 1 минуты разговора: "))
    coverage_area = float(input("Введите площадь покрытия: "))
    P = bool(input("Наличие платы за соединение (True/False): "))
    return SubMobileOperator(name, cost_per_minute, coverage_area, P)

# Вывод информации о объектах
def print_operator_info(operator):
    print(operator.object_info())

# Создание объектов и вывод информации
operator1 = create_mobile_operator()
print_operator_info(operator1)

operator2 = create_sub_mobile_operator()
print_operator_info(operator2)

# Вывод качества объектов
print(f"Качество оператора 1-го уровня: {operator1.quality()}")
print(f"Качество оператора 2-го уровня: {operator2.quality()}")
