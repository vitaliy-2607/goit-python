user_dictionary = {

}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name is not found in contacts, try another name!'
        except IndexError:
            return 'Contact list is empty! Add at least one contact!'
    return inner


def hello():
    return 'How can I help you?'


def help():
    return 'hello, отвечает в консоль "How can I help you?"\n"add ...". По этой команде бот сохраняет в памяти(в словаре например) новый контакт. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.\n"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.\n"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта. Вместо ... пользователь вводит имя контакта, чей номер нужно показать.\n"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.\n"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".'


@input_error
def add(*args):
    user_dictionary.update({args[0].title(): args[1]})
    return 'New contact saved successfully!'


@input_error
def change(*args):
    for k, v in user_dictionary.items():
        if args[0].title() == k:
            user_dictionary[k] = args[1]
            return 'Number successfully changed!'
        else:
            raise KeyError


@input_error
def phone(*args):
    return user_dictionary[args[0].title()]


@input_error
def show_all(*args):
    if len(user_dictionary) == 0:
        raise IndexError
    else:
        return "\n".join([f"{k}: {v} " for k, v in user_dictionary.items()])


def exit():
    return "Good bye!"


COMMANDS = {exit: ["exit", ".", "good bye", 'close', 'бувай'], add: [
    "add", "добавь", "додай"], show_all: ["show all", "show"], change: ['change', 'змінити', 'поменять'],
    hello: ['hello', 'привіт', 'здравствуйте'], phone: ['phone', 'телефон', 'телефон'],
    help: ['help', 'допомога', 'помощь']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split()


def main():
    while True:
        user_input = input('Enter command: ')
        result, data = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break


if __name__ == "__main__":
    main()
