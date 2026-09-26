#client={
   # "name": "sanches",
    #"age": 28,
   # "income":120000,
   # "has credit": False
#}
#print(client["income"])

clients = [{ "name": "ivan", "age": 25, "income":45000,},
           { "name": "sanches", "age": 28, "income":120000, },
           { "name": "maria", "age": 35, "income":200000,}]
for client in clients:
    if client["income"]>=50000:
        print(client["name"])