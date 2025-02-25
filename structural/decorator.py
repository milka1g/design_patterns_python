"""
Decorator is a structural design pattern that lets you attach new behaviors to objects 
by placing these objects inside special wrapper objects that contain the behaviors.
“Wrapper” is the alternative nickname for this pattern. The wrapper contains the same set of methods as the target and 
delegates to it all requests it receives. When does a simple wrapper become the real decorator? As I 
mentioned, the wrapper implements the same interface as the wrapped object. That’s why from the 
client’s perspective these objects are identical. Make the wrapper’s reference field accept any 
object that follows that interface. This will let you cover an object in multiple wrappers, 
adding the combined behavior of all the wrappers to it. Since all decorators implement the same 
interface as the base notifier, the rest of the client code won’t care whether it works with the 
“pure” notifier object or the decorated one.
Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime without breaking 
the code that uses these objects.
Use the pattern when it’s awkward or not possible to extend an object’s behavior using inheritance.
How to:
1) Figure out what methods are common to both the primary component and the optional layers. 
Create a component interface and declare those methods there.
2) Create a concrete component class and define the base behavior in it.
3) Create a base decorator class. It should have a field for storing a reference to a wrapped object. 
The field should be declared with the component interface type to allow linking to concrete components 
as well as decorators. The base decorator must delegate all work to the wrapped object.
4) Make sure all classes implement the component interface.
5) Create concrete decorators by extending them from the base decorator. A concrete decorator must execute
its behavior before or after the call to the parent method (which always delegates to the wrapped object).
6) The client code must be responsible for creating decorators and composing them in the way the client needs.
"""

class Component():
    """
    Base component interface defines ops that can be altered by decorators.
    """
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    def operation(self) -> str:
        return "Concrete Component"
    
class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"
    
class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}")


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)