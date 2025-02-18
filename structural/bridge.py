"""
Bridge is a structural design pattern that lets you split a large class or a
set of closely related classes into two separate hierarchies—abstraction and
implementation—which can be developed independently of each other.
Problem: say you have a Shape class and two subclasses Circle and Square.
You want to add color, and you would have BlueCircle, RedSquare, ... total of 4. 
To add new shapes and colors it grows exponentially.
This is because of inheritance, Bridge solves this by using object composition.
Original classes will reference an object of the new hierarchy, instead of having
all of its state and behaviors within one class. That reference will act as a bridge
between e.g. the Shape and Color classes.
Use the Bridge pattern when you want to divide and organize a monolithic 
class that has several variants of some functionality (for example, if the 
class can work with various database servers).
Use the Bridge if you need to be able to switch implementations at runtime.
How to: 
1) Identify the orthogonal dimensions in your classes. These independent concepts could be: 
abstraction/platform, domain/infrastructure, front-end/back-end, or interface/implementation.
2) See what operations the client needs and define them in the base abstraction class.
3) Determine the operations available on all platforms. Declare the ones that the abstraction
needs in the general implementation interface.
4) For all platforms in your domain create concrete implementation classes, but make sure they 
all follow the implementation interface.
5) Inside the abstraction class, add a reference field for the implementation type.
The client code should pass an implementation object to the abstraction’s constructor to associate 
one with the other. 
"""

from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    """
    You can extend Abstraction without changing the Implementation classes
    """

    def operation(self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """
    print(abstraction.operation())


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
