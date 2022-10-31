from src.models import Contact, Email, Phone
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_, not_, select

engine = create_engine("sqlite:///mybase.db")
Session = sessionmaker(bind=engine)
session = Session()


def add_contact(*args):
    new_name = args[0]
    try:
        session.query(Contact).filter(Contact.name == new_name).one()
        return f'Contact with that name already exists!'
    except NoResultFound:
        contact = Contact(name=new_name)
        session.add(contact)
        session.commit()
        return f'Contact {new_name} added successfuly!'


def add_email(*args):
    name_, emails_ = args[0], args[1]
    contact = session.query(Contact).filter(Contact.name == name_).one()
    new_email = Email(contact_id=contact.id, mail=emails_)
    session.add(new_email)
    session.commit()
    return f'Added to contact {name_} new email {emails_}'


def add_number(*args):
    name_, phones_ = args[0], args[1]
    contact = session.query(Contact).filter(Contact.name == name_).one()
    new_phone = Phone(contact_id=contact.id, phone_number=phones_)
    session.add(new_phone)
    session.commit()
    return f'Added to contact {name_} new email {phones_}'


def view_contact(contact):
    id_ = contact.id
    name_ = contact.name
    phone_db = session.query(Phone).filter(Phone.contact_id == id_).order_by(Phone.phone_number).all()
    email_db = session.query(Email).filter(Email.contact_id == id_).order_by(Email.mail).all()


def show_all(*args):
    users = session.query(Contact).all()
    for u in users:
        print(f'Contact: {u.name}, phone: {u.phones}, email: {u.emails}')



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