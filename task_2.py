# 2. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Пример:
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

num_rows = int(input('Введите количество строк: '))
num_columns = int(input('Введите количество столбцов: '))


def print_operation_table(operation, num_rows, num_columns):
    table = []
    for i in range(1, num_columns+1):
        table.append([])
        for j in range(1, num_rows+1):
            table[i-1].append(operation(i,j))
            print(f'{operation(i,j):2d}', end=' ')
        print()
    return table

print_operation_table(lambda x, y: x*y, num_rows, num_columns)
