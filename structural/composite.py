"""
Using the Composite pattern makes sense only when the core model of your
app can be represented as a tree.
Use the Composite pattern when you have to implement a tree-like object structure.
Use the pattern when you want the client code to treat both simple and complex elements uniformly.
How to: 
1) Make sure that the core model of your app can be represented as a tree structure. 
Try to break it down into simple elements and containers. 
Remember that containers must be able to contain both simple elements and other containers.
2) Declare the component interface with a list of methods that make sense for both simple 
and complex components.
3) Create a leaf class to represent simple elements. 
A program may have multiple different leaf classes.
4) Create a container class to represent complex elements. In this class, provide an array 
field for storing references to sub-elements. The array must be able to store both leaves and 
containers, so make sure it’s declared with the component interface type.
5) Finally, define the methods for adding and removal of child elements in the container.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """
        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Does the actual work, whereas Composite objects only delegate to their sub-components.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    Complex components that may have children.
    Usually, the Composite objects delegate the actual work to their children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        Traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print(
        "Client: I don't need to check the components classes even when managing the tree:"
    )
    client_code2(tree, simple)
