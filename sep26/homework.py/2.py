import pandas as pd
employees = [
    {"name": "Arman", "age": 23, "salary": 140000},
    {"name": "Elena", "age": 34, "salary": 280000},
    {"name": "Timur", "age": 21, "salary": 90000},
    {"name": "Aigerim", "age": 29, "salary": 310000}
]
df = pd.DataFrame(employees)
avg=df['salary'].mean()
print(f"avg salary: {avg}")
avg_voz=df[df['age']<25]
avg_voz.to_excel('avg_voz.xlsx', index=False)
print('Файл avg_voz.xlsx успешно создан вашей папке.')


