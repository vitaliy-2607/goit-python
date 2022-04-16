articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_dict = []
    if letter_case:
        for val in articles_dict:
            for el in val.values():
                if key in str(el):
                    new_dict.append(val)

    else:
        for val in articles_dict:
            for el in val.values():
                if key.lower() in str(el).lower():
                    new_dict.append(val)

    return new_dict
