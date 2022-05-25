user_dictionary = {

}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name is not found in contacts, try another name!'
    return inner


def hello():
    return 'How can I help you?'


@input_error
def add(name, phone_user):
    user_dictionary.update({name.title(): phone_user})
    return 'New contact saved successfully!'


@input_error
def change(name, phone_user):
    for k, v in user_dictionary.items():
        if name.title() == k:
            user_dictionary[k] = phone_user
            return 'Number successfully changed!'
        else:
            return 'Contact with this name is not in the contact list!'


@input_error
def phone(name):
    return user_dictionary[name.title()]


def show_all(user_dictionary):
    if len(user_dictionary) == 0:
        return 'Contact list is empty! Add at least one contact!'
    else:
        return "\n".join([f"{k}: {v} " for k, v in user_dictionary.items()])


def exit():
    return "Good bye!"


def parser(user_input, command):
    name = ''
    phone_user = ''
    if command == 'hello':
        print(hello())
    elif command == 'show':
        print(show_all(user_dictionary))
    elif command == 'phone':
        name = ''.join(user_input[1])
        print(phone(name))
    elif command == 'change':
        name = ''.join(user_input[1])
        phone_user = ''.join(user_input[2])
        print(change(name, phone_user))
    elif command == 'add':
        name = ''.join(user_input[1])
        phone_user = ''.join(user_input[2])
        print(add(name, phone_user))


def main():
    while True:
        user_input = input('Enter command: ').lower().split()
        command = ''.join(user_input[0])
        if command in ['exit', 'close', 'good bye']:
            print(exit())
            break
        parser_command = parser(user_input, command)


if __name__ == "__main__":
    main()
