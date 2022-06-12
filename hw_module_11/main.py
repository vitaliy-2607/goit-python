from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.startswith('+380') and len(value) == 13:
            self.__value = value
        else:
            raise ValueError


class Birthday(Field):
    def __str__(self):
        if self.value is None:
            return 'Birthday not specified!'
        else:
            return f'{self.value:%d.%m.%Y}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value is None:
            self.__value = None
        else:
            try:
                self.__value = datetime.strptime(
                    value, '%d.%m.%Y').date()
            except:
                print('Enter the date of birth in the format dd.mm.yyyy!')


class Record:
    def __init__(self, name: Name, telephone=[], birthday: Birthday = None):
        self.name = name
        self.telephone_list = telephone
        self.birthday = birthday

    def add(self, phone):
        self.telephone_list.append(phone)

    def delete(self, phone):
        self.telephone_list.remove(phone)

    def edit(self, old_phone, new_phone):
        self.telephone_list[self.telephone_list.index(old_phone)] = new_phone

    def days_to_birthday(self, birthday: Birthday):
        if birthday.value is None:
            return 'Impossible to count! Set a birthday!'
        b_day = datetime.strptime(str(self.birthday), '%d.%m.%Y')
        day_now = date.today()
        day_end = date(year=day_now.year, month=b_day.month, day=b_day.day)
        if day_end < day_now:
            day_end = date(year=day_now.year + 1,
                           month=b_day.month, day=b_day.day)
        return (day_end - day_now).days

    def __repr__(self) -> str:
        return f'{self.name.value}: {self.telephone_list}, {self.birthday}'


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec

    def iterator(self, num: int = 2):
        page = 1
        counter = 0
        result = '\n'
        for i in self.data:
            result += f'{self.data[i]}\n'
            counter += 1
            if counter >= num:
                yield result
                result = ' ' * 40 + 'page ' + str(page) + '\n'
                counter = 0
                page += 1
        yield result


def input_error(func):
    def inner(address_book, *args):
        try:
            return func(address_book, *args)
        except KeyError:
            return 'This name is not found in contacts, try another name!'
        except IndexError:
            return 'Contact list is empty! Add at least one contact!'
        except ValueError:
            return 'Enter the phone number in the format +380000000000'
        except TypeError:
            return 'This number does not belong to any contact!'

    return inner


def hello(*args):
    return 'How can I help you?'


def help(*args):
    return 'hello, отвечает в консоль "How can I help you?"\n"add ...".По этой команде бот сохраняет в памяти(в словаре например) новый контакт. Вместо ... пользователь вводит имя и номер телефона и день рождения, обязательно через пробел.\n"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... пользователь вводит имя, старый номер и новый номер телефона, обязательно через пробел.\n"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.Вместо ... пользователь вводит имя контакта, чей номер нужно показать.\n"name ..." По этой команде бот выводит в консоль имя контакта для указанного номера.Вместо ... пользователь вводит номер телефона, чье имя нужно показать.\n"help" По этой команде бот выводит список всех команд.\n"del ..." По этой команде бот удаляет номер телефона контакта.Вместо ... пользователь вводит имя и телефон который нужно удалить.\n"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.\n"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того,как выведет в консоль "Good bye!"\n"bday... По этой комманду бот выводит, сколько дней до дн роджения пользователяю Вместо ... пользователь вводть имя, бот покажет количество дней до дня рождения"\n"+bday..." По этой комманде бот сохраняет день рождения пользователю. Вместо ... пользователь вводит имя и день рождения.'


@input_error
def add_new_contact(address_book, *args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.value in address_book:
        address_book[name.value].add(phone.value)
        return f'Another phone has been added to the contact: {name.value}'
    else:
        if len(args) > 2:
            birthday = Birthday(args[2])
        else:
            birthday = Birthday(None)
        address_book[name.value] = Record(name, [phone.value], birthday)
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
    if len(rec.telephone_list) == 0:
        address_book.pop(args[0])
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
        for key in address_book.iterator():
            users += f'{key}\n'
        return users.replace('[', '').replace(']', '')


@input_error
def birthday(address_book, *args):
    name = args[0]
    if address_book[name].birthday.value is None:
        return 'None'
    return f'There are {address_book[name].days_to_birthday(address_book[name].birthday)} days left until the {name} birthday'


@input_error
def add_bday(address_book, *args):
    name = args[0]
    address_book[name].birthday = Birthday(args[1])
    return f'The birthday has been successfully added to the {name}'


def command_not_found(*args):
    return 'Command not found! Try help or another command!'


def exit(*args):
    return "Good bye!"


COMMANDS = {exit: ["exit", ".", "good bye", 'close', 'бувай'], add_new_contact: [
    "add", "добавь", "додай"], show_all: ["show all", "show"], change: ['change', 'змінити', 'поменять'],
    hello: ['hello', 'привіт', 'здравствуйте'], search_phone: ['phone', 'телефон', 'телефон'],
    help: ['help', 'допомога', 'помощь'], del_phone: ['del', 'видалити', 'удалить'],
    search_name: ['name', 'імя', 'имья'], birthday: ['bday', 'день рождения', 'день народження'], add_bday: ['+bday']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split()
    else:
        return command_not_found


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
