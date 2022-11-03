from mongoengine import Q

from models import EmbeddedDocument, StringField, Person
import connect


def add_contact(*args):
    new_name = args[0]
    Person(name=new_name).save()
    return f'Contact {new_name} added successfuly!'



def add_email(*args):
    name_, emails_ = args[0], args[1]
    contact = Person.objects(Q(name=name_))
    contact.update(email=emails_)
    return f'Added to contact {name_} new email {emails_}'


def add_number(*args):
    name_, phones_ = args[0], args[1]
    contact = Person.objects(Q(name=name_))
    contact.update(phone=phones_)
    return f'Added to contact {name_} new phone {phones_}'



def show_all(*args):
    num_users = Person.objects.count()
    for c in Person.objects:
        print(
            f'Name: {c.name} \n'
            f'Email: {c.email} \n'
            f'Phone: {c.phone} \n')




def exit(*args):
    return f'Good bye!'


COMMANDS = {

    add_contact: ["add "],
    add_number: ["number "],
    add_email: ["email "],
    show_all: ["show all"],
    exit: ["good bye", "close", "exit", "."],
}


def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    return 'Unknown command', user_input


def main():
    while True:
        user_input = input("Please, enter command: ")
        result, data = parse_command(user_input)
        if result == 'Unknown command':
            print(f'{result}: {data}.\nType help to see list of commands.')
            continue
        print(result(*data))
        if result is exit:
            break



if __name__ == "__main__":
    main()