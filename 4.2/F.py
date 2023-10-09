def order(*wishes):
    global in_stock
    recipes = {
        'Эспрессо': {'coffee': 1},
        'Капучино': {'coffee': 1, 'milk': 3},
        'Макиато': {'coffee': 2, 'milk': 1},
        'Кофе по-венски': {'coffee': 1, 'cream': 2},
        'Латте Макиато': {'coffee': 1, 'cream': 1, 'milk': 2},
        'Кон Панна': {'coffee': 1, 'cream': 1},
    }
    for wish in wishes:
        temp = in_stock.copy()
        for ingredient, amount in recipes[wish].items():
            if temp[ingredient] - amount < 0:
                break
            temp[ingredient] -= amount
        else:
            in_stock = temp.copy()
            return wish
    else:
        return 'К сожалению, не можем предложить Вам напиток'

