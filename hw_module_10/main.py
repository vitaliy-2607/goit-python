from collections import UserDict


class Field():
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    def __init__(self, *args: str):
        super().__init__(*args)


class Phone(Field):
    def __init__(self, *args: str):
        super().__init__(*args)


class Record:
    def __init__(self, name: Name, telephone=[]):
        self.name = name
        self.telephone_list = telephone

    def add(self, phone):
        self.telephone_list.append(phone)

    def delete(self, phone):
        self.telephone_list.remove(phone)

    def edit(self, old_phone, new_phone):
        self.telephone_list[self.telephone_list.index(old_phone)] = new_phone

    def __repr__(self) -> str:
        return f'{self.name.value}: {self.telephone_list}'


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec


def input_error(func):
    def inner(address_book, *args):
        try:
            return func(address_book, *args)
        except KeyError:
            return 'This name is not found in contacts, try another name!'
        except IndexError:
            return 'Contact list is empty! Add at least one contact!'
        except ValueError:
            return 'This number does not belong to any contact!'
    return inner


def hello(*args):
    return 'How can I help you?'


def help(*args):
    return 'hello, отвечает в консоль "How can I help you?"\n"add ...". По этой команде бот сохраняет в памяти(в словаре например) новый контакт. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.\n"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.\n"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта. Вместо ... пользователь вводит имя контакта, чей номер нужно показать.\n"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.\n"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".'


@input_error
def add_new_contact(address_book, *args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, [phone.value])
    if name.value in address_book:
        address_book[name.value].add(phone.value)
        return f'Another phone has been added to the contact: {name.value}'
    else:
        address_book[name.value] = rec
    return 'New contact saved successfully!'


@input_error
def change(address_book, *args):
    old_phone, new_phone = args[1], args[2]
    rec = address_book[args[0]]
    rec.edit(old_phone, new_phone)
    return f'The contact {args[0]} successfully replaced the old phone {old_phone} with the new phone {new_phone}'


@input_error
def del_phone(address_book, *args):
    phone = args[1]
    rec = address_book[args[0]]
    rec.delete(phone)
    return f'The contact {args[0]} successfully delete the phone {phone}!'


@input_error
def search_phone(address_book, *args):
    name = args[0]
    phone = str(address_book[name].telephone_list)
    return f'{name}: {phone.replace("[", "").replace("]", "")}'


@input_error
def search_name(address_book, *args):
    phone = args[0]
    for k, v in address_book.items():
        if phone in v.telephone_list:
            return f'This number {phone} belongs to the contact {k}'
        raise ValueError


@input_error
def show_all(address_book, *args):
    if len(address_book) == 0:
        raise IndexError
    else:
        users = ''
        for key in address_book:
            users += f'{address_book[key]}\n'
        return users.replace('[', '').replace(']', '')


def exit(*args):
    return "Good bye!"


COMMANDS = {exit: ["exit", ".", "good bye", 'close', 'бувай'], add_new_contact: [
    "add", "добавь", "додай"], show_all: ["show all", "show"], change: ['change', 'змінити', 'поменять'],
    hello: ['hello', 'привіт', 'здравствуйте'], search_phone: ['phone', 'телефон', 'телефон'],
    help: ['help', 'допомога', 'помощь'], del_phone: ['del', 'видалити', 'удалить'],
    search_name: ['name', 'імя', 'имья']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split()


def main():
    address_book = AddressBook()
    while True:
        user_input = input('Enter command: ')
        result, data = parse_command(user_input)
        print(result(address_book, *data))
        if result is exit:
            break


if __name__ == "__main__":
    main()
