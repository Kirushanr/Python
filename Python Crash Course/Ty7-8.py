sandwich_orders  = ['bacon', 'cheese', 'chicken', 'crisp', 'egg']
finished_sandwiches =[]

# iterate throught the sandwich orders

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your "+ order  + " sandwich")

    finished_sandwiches.append(order)

for sandwich in finished_sandwiches:
    print(sandwich)
