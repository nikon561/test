list = '5 2 4 9 12 1 8 21 17 15 27 31 '
at = [int(x) for x in list.split()]

try:
    user = int(input("Введите целое число от 1 до 30: "))
    if user % 1 == 0:
        at.append(user)
        print("Список до сортировки: ", at)
        at.sort()
        print("Список после сортировки по возрастанию: ", at)
    else:
        print("введите корректное число")
except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")

def binary_search(at, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if at[middle] == user:
            return middle
        elif user < at[middle]:
            return binary_search(at, user, left, middle - 1)
        else:
            return binary_search(at, user, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


print("Индекс введенного числа в списке: ", binary_search(at, user, 0, len(at) - 1))


