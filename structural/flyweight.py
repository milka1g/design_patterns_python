"""
Flyweight is a structural design pattern that lets you fit more objects into the available amount
of RAM by sharing common parts of state between multiple objects instead of keeping all of the data
in each object.
Constant data of an object is usually called the intrinsic state. It lives within the object; other 
objects can only read it, not change it. The rest of the object’s state, often altered “from the outside” 
by other objects, is called the extrinsic state. The Flyweight pattern suggests that you stop storing 
the extrinsic state inside the object. An object that only stores the intrinsic state is called a flyweight.
How to:
1) Divide fields of a class that will become a flyweight into two parts: intrinsic and extrinsic state
2) Leave the fields that represent the intrinsic state in the class, but make sure they’re immutable. 
They should take their initial values only inside the constructor.
3) Go over methods that use fields of the extrinsic state. For each field used in the method, introduce 
a new parameter and use it instead of the field.
4) Optionally, create a factory class to manage the pool of flyweights. Clients must only request flyweights through it.
5) The client must store or calculate values of the extrinsic state (context) to be able to call methods of flyweight objects. 
 The Flyweight pattern has a single purpose: minimizing memory intake
"""

import json

from typing import Dict


class Flyweight:
    """
    Stores intrinsic state - common portion of the state
    that belongs to multiple entities. The Flyweight
    accepts the rest of the state (extrinsic state, unique for each entity) via
    its method parameters.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Returns a Flyweight's string hash for a given state.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Returns an existing Flyweight with a given state or creates a new one.
        """

        key = self.get_key(shared_state)

        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory(
        [
            ["Chevrolet", "Camaro2018", "pink"],
            ["Mercedes Benz", "C300", "black"],
            ["Mercedes Benz", "C500", "red"],
            ["BMW", "M5", "red"],
            ["BMW", "X6", "white"],
        ]
    )

    factory.list_flyweights()

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
