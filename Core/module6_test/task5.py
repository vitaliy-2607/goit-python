def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as file:
        dictionary = []
        for line in file:
            dictionary.append(dict(zip(['id', 'name', 'age'], line.strip().split(','))))
        return dictionary
