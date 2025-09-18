def calculator():
    # Запрос двух значений у пользователя
    a = input("Введите первое значение: ")
    b = input("Введите второе значение: ")

    # Запрос типа операции
    print("Выберите тип операции:")
    print("1 - Арифметические (+, -, *, /, //, %, **)")
    print("2 - Операторы сравнения (==, !=, >, <, >=, <=)")
    print("3 - Логические операторы (and, or, not)")
    print("4 - Побитовые операторы (&, |, ^, ~, <<, >>)")
    print("5 - Операторы принадлежности (in, not in)")
    print("6 - Операторы тождественности (is, is not)")

    op_type = input("Введите номер типа операции: ")

    try:
        if op_type == '1':  # Арифметические операции
            op = input("Введите арифметический оператор (+, -, *, /, //, %, **): ")
            num1 = float(a)
            num2 = float(b)
            if op == '+':
                print("Результат:", num1 + num2)
            elif op == '-':
                print("Результат:", num1 - num2)
            elif op == '*':
                print("Результат:", num1 * num2)
            elif op == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print("Результат:", num1 / num2)
            elif op == '//':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print("Результат:", num1 // num2)
            elif op == '%':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print("Результат:", num1 % num2)
            elif op == '**':
                print("Результат:", num1 ** num2)
            else:
                print("Неверный оператор")

        elif op_type == '2':  # Операторы сравнения
            op = input("Введите оператор сравнения (==, !=, >, <, >=, <=): ")
            val1 = float(a)
            val2 = float(b)
            if op == '==':
                print(val1 == val2)
            elif op == '!=':
                print(val1 != val2)
            elif op == '>':
                print(val1 > val2)
            elif op == '<':
                print(val1 < val2)
            elif op == '>=':
                print(val1 >= val2)
            elif op == '<=':
                print(val1 <= val2)
            else:
                print("Неверный оператор")

        elif op_type == '3':  # Логические операторы
            bool_a = bool(a)
            bool_b = bool(b)
            op = input("Введите логический оператор (and, or, not): ")
            if op == 'and':
                print(bool_a and bool_b)
            elif op == 'or':
                print(bool_a or bool_b)
            elif op == 'not':
                print(not bool_a)
            else:
                print("Неверный оператор")

        elif op_type == '4':  # Побитовые операторы
            op = input("Введите побитовый оператор (&, |, ^, ~, <<, >>): ")
            int_a = int(float(a))
            int_b = int(float(b))
            if op == '&':
                print(int_a & int_b)
            elif op == '|':
                print(int_a | int_b)
            elif op == '^':
                print(int_a ^ int_b)
            elif op == '~':
                print(~int_a)
            elif op == '<<':
                print(int_a << int_b)
            elif op == '>>':
                print(int_a >> int_b)
            else:
                print("Неверный оператор")

        elif op_type == '5':  # Операторы принадлежности
            op = input("Введите оператор принадлежности (in, not in): ")
            if op == 'in':
                print(a in b)
            elif op == 'not in':
                print(a not in b)
            else:
                print("Неверный оператор")

        elif op_type == '6':  # Операторы тождественности
            op = input("Введите оператор тождественности (is, is not): ")
            if op == 'is':
                print(a is b)
            elif op == 'is not':
                print(a is not b)
            else:
                print("Неверный оператор")

        else:
            print("Неверный тип операции")

    except ValueError:
        print("Ошибка: некорректный ввод чисел")
    except Exception as e:
        print("Произошла ошибка:", e)


if __name__ == "__main__":
    calculator()
