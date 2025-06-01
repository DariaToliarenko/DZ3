def calculator():
    print("Простой калькулятор")
    print("Введите два числа и операцию (+, -, *, /).")

    while True:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ошибка: Деление на ноль.")
                continue
        else:
            print("Ошибка: Неверная операция.")
            continue

        print(f"Результат: {result}")
        
        again = input("Хотите выполнить еще один расчет? (да/нет): ")
        if again.lower() != 'да':
            break

if __name__ == "__main__":
    calculator()
    