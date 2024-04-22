import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num >= max_num or quantity > (max_num - min_num + 1):
        print("Неправильно вказаний формат чисел.")
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
