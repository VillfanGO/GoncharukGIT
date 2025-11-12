print("=== ПРОСТОЙ КАЛЬКУЛЯТОР ===")
print("Доступные операции:")
print("+ - сложение")
print("- - вычитание")
print("* - умножение")
print("/ - деление")
print("% - остаток от деления")
print("** - возведение в степень")
print()

try:
    # Ввод первого числа
    num1 = float(input("Введите первое число: "))
    
    # Ввод операции
    operation = input("Введите операцию (+, -, *, /, %, **): ")
    
    # Ввод второго числа
    num2 = float(input("Введите второе число: "))
    
    # Выполнение операции
    if operation == '+':
        result = num1 + num2
        print(f"\nРезультат: {num1} + {num2} = {result}")
        
    elif operation == '-':
        result = num1 - num2
        print(f"\nРезультат: {num1} - {num2} = {result}")
        
    elif operation == '*':
        result = num1 * num2
        print(f"\nРезультат: {num1} * {num2} = {result}")
        
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
        else:
            result = num1 / num2
            print(f"\nРезультат: {num1} / {num2} = {result}")
            
    elif operation == '%':
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
        else:
            result = num1 % num2
            print(f"\nРезультат: {num1} % {num2} = {result}")
            
    elif operation == '**':
        result = num1 ** num2
        print(f"\nРезультат: {num1} ** {num2} = {result}")
        
    else:
        print("Ошибка: Неизвестная операция!")
        
except ValueError:
    print("Ошибка: Пожалуйста, вводите только числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")