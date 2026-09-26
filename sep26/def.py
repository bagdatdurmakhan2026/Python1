clients = [ {"name": "ivan", "age": 25, "income": 45000}, {"name": "sanches", "age": 28, "income": 120000}, {"name": "maria", "age": 35, "income": 200000} ]
def filter_vip_clients(clients_list):
    vip_clients=[]
    for client in clients_list:
        if client['income'] >= 100000:
            vip_clients.append(client['name'])
    return vip_clients 
final_result = filter_vip_clients(clients) 
print(final_result) 