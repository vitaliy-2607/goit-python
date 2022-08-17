from abc import ABC, abstractmethod


class ABC_Abook(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def delete_contact(self, contact_name):
        pass

    @abstractmethod
    def change(self, phone1, phone2):
        pass

    @abstractmethod
    def delete(self, phone):
        pass

    @abstractmethod
    def add_number(self, phone):
        pass

    @abstractmethod
    def days_to_birthday(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ABC_Nbook(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def add_tag(self):
        pass
