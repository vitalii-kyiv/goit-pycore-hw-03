import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not (1 <= min <= max <= 1000):
        raise ValueError("Мінімальне або максимальне значення діапазону не відповідає умовам min>=0 та max<=1000.")
    if quantity > (max - min + 1) or quantity < 1:
        raise ValueError("Кількість чисел перевищує доступний діапазон.")
    numbers_list = random.sample(range(min, max), quantity)
    numbers_list.sort() 
    print(type(numbers_list))
    return numbers_list

ticket = get_numbers_ticket(1, 100, 6)
print("Ваш лотерейний білет:", ticket)