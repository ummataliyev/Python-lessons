def car_info(company, model, color, box, year, cost=None):
    car = {'company': company,
            'model': model,
            'color': color,
            'box': box,
            'year': year,
            'cost': cost}
    return car

def car_enter():
    """A function that allows the user to put information about several cars in one list using the car_info function"""
    cars = []
    while True:
        print("\nEnter the following information", end='')
        company = input("Manufacturer: ")
        model = input("Model: ")
        color = input("Color: ")
        box = input("Box: ")
        year = input("Date of manufacture: ")
        cost = input("Cost: ")


        cars.append(car_info(company, model, color, box, year, cost))
        answer = input("Do you want to add another information? (yes/no): ")
        if answer == 'no':
            break
        return

def info_print(car_info):
    """A function that consults a dictionary that stores information about cars"""
    print(f"{car_info['color'].title()}, "
          f"{car_info['company'].upper()}, "
          f"{car_info['model'].upper()}, "
          f"box type is {car_info['box'].lower()}, "
          f"year of manufacture: {car_info['year']},  cost: ${car_info['cost']}")

