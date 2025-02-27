"""
Facade is a structural design pattern that provides a simplified interface to a library, 
a framework, or any other complex set of classes.
Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.
Use the Facade when you want to structure a subsystem into layers.
How to:
1) Check whether it’s possible to provide a simpler interface than what an existing subsystem already provides. 
2) Declare and implement this interface in a new facade class. The facade should redirect the calls from the client code to appropriate objects of the subsystem. 
3) To get the full benefit from the pattern, make all the client code communicate with the subsystem only via the facade. 
4) If the facade becomes too big, consider extracting part of its behavior to a new, refined facade class.
"""

from __future__ import annotations

class Facade:
    """"
    Provides simple interface to complex logic of one or several subsystems.
    """

    def __init__(self, subststem1: SubSystem1, subststem2: SubSystem2) -> None:
        """
        Provide facade with existing subsystem or force it to create them.
        """
        self._subsystem1 = subsystem1 or SubSystem1()
        self._subsystem2 = subsystem2 or SubSystem2()

    def operation(self) -> str:
        """
        Facade's methods are convenient shortcuts to sophisticated functionality
        of subsystems.
        """
        results = []
        results.append("Facade init:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)
    

class SubSystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"

class SubSystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"


    def operation_z(self) -> str:
        return "Subsystem2: Fire!"
    
def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")

if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = SubSystem1()
    subsystem2 = SubSystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)

