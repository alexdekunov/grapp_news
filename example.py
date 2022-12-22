# пример для проверки работы mypy

def calc_price(unit_price: float, quantity: int) -> float:
    return unit_price * quantity


def ruok(one: int, two: int) -> int:
    return one + two

if __name__ == "__main__":
    print(calc_price(73.2, 2))
    print(calc_price(73, 4))
    print(calc_price(73.2, 5))

    print(ruok(2, 3))
