def withdraw(balance):
    amount = int(input("Сколько снять? "))
    if amount > balance:
        print("Недостаточно средств!")
        return balance
    else:
        print("Выдано")
        return balance - amount

def deposit(balance):
    amount = int(input("Сколько пополнить? "))
    print("Счет пополнен")
    return balance + amount

def show_menu():
    print("1. Снять деньги")
    print("2. Пополнить балик")
    print("3. Выход")


balance = 1000
print("Welcome")

while True:
    print(f"Ваш баланс: {balance} Руб")
    show_menu()

    choise = input("Выберите действие (1, 2, 3): ")
    if choise == "1":
        balance = withdraw(balance)
    elif choise == "2":
        balance = deposit(balance)
        pass
    elif choise == "3":
        print("Adios")
        break
    else:
        print("Неверная команда")