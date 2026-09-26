import pandas as pd
apartments = [
    {"rooms": 2, "area": 65, "price": 42000000, "district": "Bostandyk"},
    {"rooms": 1, "area": 38, "price": 25000000, "district": "Almaly"},
    {"rooms": 3, "area": 90, "price": 68000000, "district": "Bostandyk"},
    {"rooms": 2, "area": 55, "price": 31000000, "district": "Auezov"},
    {"rooms": 4, "area": 120, "price": 95000000, "district": "Bostandyk"}
]
df = pd.DataFrame(apartments)
avg=df['area'].mean()
low_400=df[df['price']<40000000] 
print(f'Средняя площадь квартир: {avg}')
print(f'Файл low_400.xlsx успешно создан вашей папке.') 
skok=df['district'].value_counts()
print(f'times', skok)
skok.to_excel('skok.xlsx', index=False)
print(f'Файл skok.xlsx успешно создан вашей папке.')
print(f'Файл avg.xlsx успешно создан вашей папке.')

