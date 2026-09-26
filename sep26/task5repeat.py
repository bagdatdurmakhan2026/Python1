drivers = [
    {"name": "ali", "age": 19, "city": "Almaty"},
    {"name": "dmitry", "age": 30, "city": "Astana"},
    {"name": "sergey", "age": 22, "city": "Shymkent"},
    {"name": "anna", "age": 45, "city": "Almaty"}
]
def find_young_drivers(drivers_list):
    young_drivers = []
    for young in drivers_list:
        if young['age'] < 25:
            young_drivers.append(young['name'])
    return young_drivers
final_result = find_young_drivers(drivers)
print(final_result)