incomes = [30000, 120000, 45000, 200000, 15000, 85000, 300000]
good_incomes = [income for income in incomes if 50000 <= income <= 150000]
print(good_incomes)