def get_full_name(name, surname, father = ''):
    if father:
        return f"{name} {father} {surname}".title()
    else:
        return f"{name} {surname}".title()

