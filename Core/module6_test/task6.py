def get_recipe(path, search_id):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            lst = line.strip().split(',')
            if search_id == lst[0]:
                return {'id': lst[0],
                        'name': lst[1],
                        'ingredients': lst[2:]}
    return None
