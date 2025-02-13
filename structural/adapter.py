"""
Allows objects with incompatible interfaces to collaborate.
e.g. your app downloads data in XML, you find a 3rd-party lib that uses JSON and
you need to create adapter that converts interface of one object to that of another one.
1) The adapter gets an interface, compatible with one of the existing objects.
2) Using this interface, the existing object can safely call the adapter’s methods.
3) Upon receiving a call, the adapter passes the request to the second object, 
but in a format and order that the second object expects.
Use the Adapter class when you want to use some existing class, but its interface
isn’t compatible with the rest of your code.
Use the pattern when you want to reuse several existing subclasses that lack some common
functionality that can’t be added to the superclass.
1) Make sure that you have at least two classes with incompatible interfaces:
- A useful service class
- One or several client classes that want to use service
2) Declare the client interface and describe how clients communicate with the service.
3) Create the adapter class and make it follow the client interface.
4) Add a field to the adapter class to store a reference to the service object. Or pass service to adapter.
5) Clients should use the adapter via the client interface.
"""


class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: default target's behavior."


class Adaptee:
    """
    Contains some useful behavior but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation
    before the client code can use it. This is a 3rd-party service.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """
    print(target.request())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print(
        "Client: The Adaptee class has a weird interface. "
        "See, I don't understand it:"
    )
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
