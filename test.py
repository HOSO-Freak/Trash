import pandas as pd

df = pd.read_csv("data.csv")

print("--- первые 3 строки---")
print(df.head(3))

print("\n--- Статистика по таблице---")
print(df.describe())

average_salary = df["Зарплата"].mean()
print(f"\nСредняя зарплата: {average_salary} руб.")

df["Налог"] = df["Зарплата"] *  0.13
df["На руки"] = df["Зарплата"] - df["Налог"]
df_sorted = df.sort_values(by="Возраст", ascending=False)

print("\n--- Сортировка по возрасту (убывание)")
print(df_sorted[["Имя", "Возраст", "Зарплата", "На руки"]])

df_sorted.to_csv("data_final.csv", index=False)
print("\nФайл data_final.csv успешно сохранен")