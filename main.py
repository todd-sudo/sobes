from abc import ABC, ABCMeta, abstractmethod
from calendar import c


class User(ABC):

    @abstractmethod
    def create():
        pass
    
    @abstractmethod
    def update():
        pass
    
    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def get():
        pass


class CustomUser(User):
    
    def create():
        pass

    def update():
        pass

    def get():
        pass

    def delete():
        pass


class OneMeta(ABCMeta):
    """Абстрактный Мета класс"""
    pass


class Meta(type):
    """Мета класс"""
    def __new__(cls, name, bases, attrs):
        attrs["my_field"] = "Value"
        return super().__new__(cls, name, bases, attrs)


class User(metaclass=Meta):
    def __init__(self) -> None:
        print("Конструктор")
        super().__init__()



u = User()
print(u.my_field)


