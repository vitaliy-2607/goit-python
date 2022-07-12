import re
from collections import UserDict
from datetime import datetime
import shelve


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}
        self.listdata = []

    def show_all(self):
        counter = 0
        for k, v in self.data.items():
            counter += 1
            print(v)
        return f'Database has {counter} profile(s)'

    def add_record(self, record):
        self.data[record.name.value] = record
        self.listdata.append(record)
        # book.append({record.name.value: record})

    def load(self, filename):
        with shelve.open(filename) as db:
            phone_book.listdata = db['PhoneBook'].listdata
            phone_book.data = db['PhoneBook'].data

    def save_close(self, filename):
        with shelve.open(filename) as db:
            db['PhoneBook'] = phone_book

    def search_common(self, searched_text):
        searched_profiles = []
        for k, v in self.data.items():
            if searched_text.lower() in v.name.value.lower():
                searched_profiles.append(v.name.value)
            for i in v.phones:
                if searched_text in i.value:
                    searched_profiles.append(v.name.value)
        if len(searched_profiles) == 0:
            return f'Anything common haven`t been found in database.'
        if len(searched_profiles) == 1:
            return f'{searched_profiles[0]} has something in common with your search.'
        else:
            return f'{", ".join(searched_profiles)} have something in common with your search.'

    def iterator(self, num):
        counter = 0
        start_counter = counter
        while True:
            temp_list = []
            try:
                while counter < start_counter + num:
                    temp_list.append(self.listdata[counter])
                    counter += 1
            except IndexError:
                yield temp_list
                break
            yield temp_list
            start_counter = counter
            temp_list.clear


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        if not phone:
            self.phones.append(phone)

    def change(self, phone1, phone2):
        for i in self.phones:
            if i.value == phone1:
                i.value = phone2
                return f'Number {phone1} from {self.name}`s list changed to {phone2}'
        return f'Number {phone1} is not exist in {self.name} list'

    def delete(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                return f'Number {phone} deleted from {self.name}`s number list'
        return f'Number {phone} is not exist in {self.name} list'

    def add_number(self, phone):
        for i in self.phones:
            if i.value == phone.value:
                return f'This number is already in database'
        self.phones.append(phone)

    def days_to_birthday(self):
        if self.birthday == None:
            return f'{self.name.value}`s birth date is not exist in this database.'
        else:
            d_now = datetime.now()
            if datetime(day=d_now.day, month=d_now.month, year=d_now.year) < datetime(day=self.birthday.value.day, month=self.birthday.value.month, year=d_now.year):
                diff = (datetime(day=self.birthday.value.day, month=self.birthday.value.month,
                        year=d_now.year) - datetime(day=d_now.day, month=d_now.month, year=d_now.year)).days
                return f'{diff} days to {self.name.value}`s birthday'
            elif datetime(day=d_now.day, month=d_now.month, year=d_now.year) > datetime(day=self.birthday.value.day, month=self.birthday.value.month, year=d_now.year):
                diff = (datetime(day=self.birthday.value.day, month=self.birthday.value.month,
                        year=d_now.year+1) - datetime(day=d_now.day, month=d_now.month, year=d_now.year)).days
                return f'{diff} days to {self.name.value}`s birthday'
            elif datetime(day=d_now.day, month=d_now.month, year=d_now.year) == datetime(day=self.birthday.value.day, month=self.birthday.value.month, year=d_now.year):
                return f'Today is {self.name.value}`s birthday'

    def __str__(self) -> str:
        self.phones_show = None
        if len(self.phones) == 0:
            self.phones_show = 'not exist in this database'
        elif len(self.phones) == 1:
            self.phones_show = str(self.phones[0])
        elif len(self.phones) > 1:
            self.phones2 = [*self.phones]
            self.phones_show = [*self.phones2]
        if self.birthday == None:
            return f'{self.name.value} phone(s) is {self.phones_show}.'
        else:
            return f'{self.name.value} phone(s) is {self.phones_show}, his/here birth date is {self.birthday}.'

    def __repr__(self) -> str:
        if self.birthday == None:
            return f'{self.name.value}, {self.phones}'
        else:
            return f'{self.name.value}, {self.phones}, {self.birthday.value}'


class Field:
    pass


class Name(Field):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'


class Phone(Field):
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if is_number_valid(value):
            self.__value = value
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f'{self.value}'


class Birthday(Field):
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if is_birthday_valid(value):
            d, m, y = value.split('.')
            new_value = datetime(day=int(d), month=int(m), year=int(y))
            self.__value = new_value
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f'{self.value.strftime("%d %B %Y")}'


def is_birthday_valid(value):
    searcher = re.findall('\d{2}\.\d{2}\.\d{4}', value)
    if value == searcher[0]:
        d, m, y = value.split('.')
        try:
            new_value = datetime(day=int(d), month=int(m), year=int(y))
            return True
        except ValueError:
            return False
    else:
        return False


def is_number_valid(value):
    searcher = re.findall('\d{10}', str(value))
    if value == searcher[0]:
        return True
    else:
        return False


phone_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except TypeError:
            return 'TypeError! Try to type command again.'
        except IndexError:
            return 'IndexError! Try to type command again.'
        except KeyError:
            return 'KeyError! Try to type command again.'
        except ValueError:
            return 'ValueError! Try to type command again.'
    return wrapper


def exit(*args):
    return "Good bye!"


@input_error
def add_contact(*args):  # Для add_contact потрібно ввести Ім'я, також можна відразу додати Новий номер і День народження
    # print(phone_book, 'before')
    for k, v in phone_book.items():
        if k == args[0]:
            return f'{args[0]} is already in list'
    name = Name(args[0])
    if len(args) == 2:
        phone = Phone(args[1])
    if len(args) == 3:
        phone = Phone(args[1])
        birthday = Birthday(args[2])
    if len(args) == 1:
        rec = Record(name)
    elif len(args) == 2:
        rec = Record(name, phone)
    else:
        rec = Record(name, phone, birthday)

    phone_book.add_record(rec)
    # print(phone_book, 'after')
    return f'Contact {name.value} added successfuly'


@input_error
def add_number(*args):  # Для add_number потрібно ввести Ім'я і Новий номер, який ви хочете додати
    rec = phone_book[args[0]]
    # print(rec)
    new_number = Phone(args[1])
    # print(rec.phones)
    if rec.add_number(new_number) == None:
        return f'Number {new_number.value} added to {rec.name}`s list of numbers successfuly'
    else:
        return rec.add_number(new_number)


@input_error
def add_birthday(*args):
    rec = phone_book[args[0]]
    rec.birthday = Birthday(args[1])
    return f'Birthday is updated to {rec.birthday.value.strftime("%d %B %Y")}'


@input_error
def change(*args):  # Для change потрібно ввести Ім'я, Старий номер і Новий номер
    # print(phone_book, 'before')
    for k, v in phone_book.items():
        if k == args[0]:
            rec = phone_book[args[0]]
            return rec.change(args[1], args[2])
    return f'{args[0]} isn`t exist in list of names'


@input_error  # Тут можна додати опцію видалити всі контакти
def delete(*args):  # Для delete потрібно ввести Ім'я та Номер який хочете видалити
    for k, v in phone_book.items():
        if k == args[0]:
            rec = phone_book[args[0]]
            return rec.delete(args[1])
    return f'{args[0]} isn`t exist in list of names'


@input_error
def phone(*args):
    rec = phone_book[args[0]]
    return rec


@input_error
def show_all(*args):
    return phone_book.show_all()


@input_error
def days_to_birthday(*args):
    for k, v in phone_book.items():
        if k == args[0]:
            rec = phone_book[args[0]]
            return rec.days_to_birthday()
    return f'{args[0]} isn`t exist in list of names'


@input_error
def show_num(*args):
    iter = phone_book.iterator(int(args[0]))
    for i in iter:
        a = i
        for i2 in a:
            print(i2)
    return f'{len(phone_book.listdata)} profile(s) showed'


@input_error
def search_common(*args):
    result = AddressBook.search_common(*args)
    return result


COMMANDS = {
    search_common: ["search", "search common"],
    exit: ["good bye", "close", "exit", "."],
    add_contact: ["add contact", "add c"],
    add_number: ["add number", "add n"],
    show_all: ["show all"],
    phone: ["phone"],
    change: ["change", "change phone"],
    delete: ["delete"],
    add_birthday: ["add birthday", "add b"],
    days_to_birthday: ["days to birthday", "d t b"],
    show_num: ["show num"],
    help: ["help"]
}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    return 'Unknown command', user_input


def main():
    filename = 'database/some_db'
    phone_book.load(filename)
    while True:
        user_input = input(">>>")
        result, data = parse_command(user_input)
        if result == 'Unknown command':
            print(f'{result}: {data}')
            continue
        print(result(*data))
        if result is exit:
            break
    phone_book.save_close(filename)


if __name__ == "__main__":
    main()
