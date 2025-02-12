"""
Abstract Factory defines an interface for creating all distinct products
but leaves the actual product creation to concrete factory classes.
Each factory type corresponds to a certain product variety.

Use the Abstract Factory when your code needs to work with various families of related
products, but you don’t want it to depend on the concrete classes of those products—they
might be unknown beforehand or you simply want to allow for future extensibility.

Consider implementing the Abstract Factory when you have a class with a set of Factory Methods
that blur its primary responsibility.

1) Map out a matrix of distinct product types versus variants of these products.
2) Declare abstract product interfaces for all product types. Then make all concrete product classes
implement these interfaces.
3) Declare the abstract factory interface with a set of creation methods for all abstract products.
4) Implement a set of concrete factory classes, one for each product variant.
5) Create factory initialization code somewhere in the app. It should instantiate one of the 
concrete factory classes, depending on the application configuration or the current environment. 
Pass this factory object to all classes that construct products.
6) Scan through the code and find all direct calls to product constructors. Replace them with calls 
to the appropriate creation method on the factory object.
"""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA):
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Result of product A1"


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Result of product A2"


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "Result of product B1"

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "Result of product B2"

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of B2 collaborating with the ({result})"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")


if __name__ == "__main__":
    print("Testing with Factory type 1")
    client_code(ConcreteFactory1())

    print("Testing with Factory type 2")
    client_code(ConcreteFactory2())
