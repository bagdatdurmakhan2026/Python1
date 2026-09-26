import pandas as pd
drivers = [
    {"name": "ali", "age": 19, "city": "Almaty"},
    {"name": "dmitry", "age": 30, "city": "Astana"},
    {"name": "sergey", "age": 22, "city": "Shymkent"},
    {"name": "anna", "age": 45, "city": "Almaty"}
]
df = pd.DataFrame(drivers)
young_age = df['age'].mean()
print(f'Средний возраст водителей: {young_age}')
young_drivers_df = df[df['age'] < 25]
young_drivers_df.to_excel('young_drivers.xlsx', index=False)
print('Файл young_drivers.xlsx успешно создан вашей папке.')