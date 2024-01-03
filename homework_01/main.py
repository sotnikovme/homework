"""
Домашнее задание №1
Функции и структуры данных
"""
# a = (1, 2, 5, 7)


def power_numbers(*sp):
    # for a in s:
        a = map(lambda num_sq: num_sq**2, sp)
        return list(a)
    # print(a)
    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """
# print(power_numbers(1, 2, 5, 7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

# def f_odd(num_1):
#     # print(num_1)
#     f = filter(lambda q: q % 2 == 0, num_1)

#     return list(f)



# def f_even(num_2):
#     # f = filter(lambda q: q % 2 == 1, num_2)
#     return list(f)


def is_prime(num_3):
    m = []
    
    for number in num_3:
       
        if number > 1:
            simple = True 
            for i in range(2, number):
            
                if(number % i) == 0: 
                    simple = False
              
            if simple == True:
                    m.append(number)
    return list(m)

            


def filter_numbers(x, y):
    if y == ODD:
          return list(filter(lambda q: q % 2 == 1, x))
        # return f_odd(x)
    if y ==EVEN:
          return list(filter(lambda q: q % 2 == 0, x))
        # return f_even(x)
    if y==PRIME:
        return is_prime(x)

# print(filter_numbers([2, 3, 4, 5, 9, 7, 11, 6], ODD))
# print(filter_numbers([2, 3, 4, 5, 9, 7, 11, 6], EVEN))
# print(filter_numbers([2, 3, 4, 5, 9, 7, 11, 6], PRIME))
# print(filter_numbers([2, 1, 3, 5, 4], EVEN))


    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)

    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """
