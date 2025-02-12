"""
Factory Method is a creational design pattern that provides an interface
for creating objects in a superclass, but allows subclasses to alter the
type of objects that will be created.

Use the Factory Method when you don’t know beforehand the exact types and
dependencies of the objects your code should work with.

1) Make all products follow the same interface. This interface should declare methods
that make sense in every product.
2) Add an empty factory method inside the creator class. The return type of the method
should match the common product interface.
3) In the creator’s code find all references to product constructors. 
One by one, replace them with calls to the factory method, while extracting
the product creation code into the factory method.
4) Now, create a set of creator subclasses for each type of product 
listed in the factory method. Override the factory method in the subclasses 
and extract the appropriate bits of construction code from the base method.
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
