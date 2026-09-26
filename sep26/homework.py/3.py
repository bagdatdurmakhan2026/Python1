import pandas as pd
orders = [
    {"id": 1, "item": "Laptop", "price": 450000, "status": "delivered"},
    {"id": 2, "item": "Mouse", "price": 12000, "status": "canceled"},
    {"id": 3, "item": "Monitor", "price": 150000, "status": "delivered"},
    {"id": 4, "item": "Keyboard", "price": 25000, "status": "delivered"},
    {"id": 5, "item": "Headphones", "price": 45000, "status": "canceled"}
]
def cal_r(orders_list):
    total_revenue = 0
    for order in orders_list:
        if order['status']== "delivered":
            total_revenue += order['price']
    return total_revenue
##print(f"Total revenue from delivered orders: {cal_r(orders)}")
fin= cal_r(orders)
print(fin)