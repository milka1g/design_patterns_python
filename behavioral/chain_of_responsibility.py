"""
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, 
each handler decides either to process the request or to pass it to the next handler in the chain. Each check should be extracted to its own class with a 
single method that performs the check. Each linked handler has a field for storing a reference to the next handler in the chain. It’s crucial that all handler 
classes implement the same interface. Each concrete handler should only care about the following one having the execute method.
Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various ways, but the exact types of requests 
and their sequences are unknown beforehand.
Use the pattern when it’s essential to execute several handlers in a particular order.
Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.
How to:
1) Declare the handler interface and describe the signature of a method for handling requests.
2) To eliminate duplicate boilerplate code in concrete handlers, it might be worth creating an abstract base handler class, derived from the handler interface.
3) One by one create concrete handler subclasses and implement their handling methods. Each handler should make two decisions when receiving a request:
- Whether it’ll process the request.
- Whether it’ll pass the request along the chain.
4) The client may either assemble chains on its own or receive pre-built chains from other objects. 
5) The client may trigger any handler in the chain, not just the first one. The request will be passed along the chain until some handler refuses to pass it 
further or until it reaches the end of the chain.
6) Due to the dynamic nature of the chain, the client should be ready to handle the following scenarios:
- The chain may consist of a single link.
- Some requests may not reach the end of the chain.
- Others may reach the end of the chain unhandled.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
All Concrete handlers either handle a request or pass it to the next handler in chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
