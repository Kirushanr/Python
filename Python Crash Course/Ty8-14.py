def make_car(manufacturer, model, **arguments):
    """ Returns a dictionary containing information of A car """
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in arguments.items():
        car[key] = value
    return car


car_detail = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_detail)
