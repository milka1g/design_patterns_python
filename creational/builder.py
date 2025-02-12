"""
Construct complex objects step by step. 
The pattern organizes object construction into a set of steps (buildWalls, buildDoor, etc.).
To create an object, you execute a series of these steps on a builder object.
The important part is that you don’t need to call all of the steps. You can call only those 
steps that are necessary for producing a particular configuration of an object.

The director class defines the order in which to execute the building steps, while the builder provides 
the implementation for those steps.Having a director class in your program isn’t strictly necessary. 
You can always call the building steps in a specific order directly from the client code. 

When and how to apply:
Say you have a constructor with ten optional parameters. Calling such a beast is very inconvenient; 
therefore, you overload the constructor and create several shorter versions with fewer parameters. 
These constructors still refer to the main one, passing some default values into any omitted parameters.
Use the Builder pattern when you want your code to be able to create different representations of some 
product (for example, stone and wooden houses).

1) Make sure that you can clearly define the common construction steps for building all available
product representations. Otherwise, you won’t be able to proceed with implementing the pattern.
2) Declare these steps in the base builder interface.
3) Create a concrete builder class for each of the product representations and 
implement their construction steps. Don’t forget about implementing a method for fetching the result 
of the construction. The reason why this method can’t be declared inside the builder interface is 
that various builders may construct products that don’t have a common interface. 
4) Think about creating a director class. It may encapsulate various ways to construct a product 
using the same builder object.
5) The client code creates both the builder and the director objects. Before construction starts, 
the client must pass a builder object to the director. Usually, the client does this only once, 
via parameters of the director’s class constructor. The director uses the builder object in 
all further construction.
6) The construction result can be obtained directly from the director only if all products follow the 
same interface. Otherwise, the client should fetch the result from the builder.
Unlike other creational patterns, Builder doesn’t require products to have a common interface. 
That makes it possible to produce different products using the same construction process.
"""

from abc import ABC, abstractmethod


class Builder(ABC):
    """
    Specify methods for creating different parts of the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product1:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")


class ConcreteBuilder1(Builder):
    """
    Provide specific implementations of the building steps.
    ConcreteBuilder2 could return Product2, and those Products
    do not need to follow the common interface.
    """

    def __init__(self) -> None:
        """
        Fresh builder contains a blank product object.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
