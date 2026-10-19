import pandas as pd
import random
import string

def generate_password(length=10):
    # Берем все буквы (заглавные и строчные) и цифры
    characters = string.ascii_letters + string.digits
    # Случайно выбираем нужное количество символов и склеиваем в строку
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Список имен (в реальности мы бы взяли его из файла или базы данных)
names = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Елена"]

# Создаем пустой список, куда будем складывать словари с данными
users_data = []

for name in names:
    # Генерируем логин (имя маленькими буквами + _user)
    login = f"{name.capitalize()}_user"
    # Генерируем пароль через нашу функцию
    password = generate_password()
    
    # Создаем словарь для одного пользователя
    user = {
        "Имя": name,
        "Логин": login,
        "Пароль": password
    }
    users_data.append(user)

# Превращаем список словарей в DataFrame
df = pd.DataFrame(users_data)

print("--- Таблица новых сотрудников ---")
print(df)

# Сохраняем в CSV
df.to_csv("employees.csv", index=False)
print("\nФайл employees.csv сохранен!")