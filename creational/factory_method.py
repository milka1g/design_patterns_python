"""
Factory Method is a creational design pattern that provides an interface
for creating objects in a superclass, but allows subclasses to alter the
type of objects that will be created.
"""

from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        """
        Here can be some default implementation.
        """
        pass

    def some_operation(self):
        """
        Creator can define some logic as well.
        """
        product = self.factory_method()
        result = f"Creator: Same creator code worked with: {product.operation()}"
        return result


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Product 1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Product 2"


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    Client works with an instance of concrete creator through its base interface.
    """
    print(f"Client: I am not aware of creator's class, but it works.")
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    client_code(ConcreteCreator1())
    print("\n")
    client_code(ConcreteCreator2())
