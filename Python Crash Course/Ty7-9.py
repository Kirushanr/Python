sandwich_orders  = ['bacon', 'cheese', 'chicken', 'crisp', 'egg', 'pastrami']
finished_sandwiches =[]

print("Deli has run out of pastrami")

# remove all orders of pastrami

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


# iterate throught the sandwich orders

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your "+ order  + " sandwich")

    finished_sandwiches.append(order)

for sandwich in finished_sandwiches:
    print(sandwich)
