"""
Ensure that a class has just a single instance. Why would anyone want to control how many instances
a class has? The most common reason for this is to control access to some shared 
resource—for example, a database or a file.
Provide a global access point to that instance. Just like a global variable, the 
Singleton pattern lets you access some object from anywhere in the program.
However, it also protects that instance from being overwritten by other code.
Make the default constructor private, to prevent other objects from using the new operator
with the Singleton class.
Create a static creation method that acts as a constructor. Under the hood, this method calls
the private constructor to create an object and saves it in a static field. 
All following calls to this method return the cached object.

1) Add a private static field to the class for storing the singleton instance.
2) Declare a public static creation method for getting the singleton instance.
3) Implement “lazy initialization” inside the static method. It should create a new object on its
first call and put it into the static field. The method should always return that instance on all subsequent calls.
4) Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects.
"""


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        When __call__ is defined in a metaclass (SingletonMeta), it controls what happens when a class instance is created
        (i.e., when Singleton() is called).
        Since SingletonMeta is a metaclass, __call__ is triggered when a class using that metaclass is instantiated.
        For a metaclass, super() refers to type, the default metaclass.
        type.__call__() is the built-in way Python creates instances.
        type.__call__() internally does:
        Calls __new__()
        Calls __init__()
        Returns the instance
        When s1 = Singleton() is executed it triggers SingletonMeta.__call__ and super().__call__(*args, **kwargs) is executed
        which calls Singleton.__new__() and __init__() and returns an instance
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


# # Simpler approach
# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# # Usage
# # s1 = Singleton()
# # s2 = Singleton()

# # print(s1 is s2)  # True

# def singleton(cls):
#     instances = {}

#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]

#     return get_instance


# @singleton
# class Singleton:
#     pass


# # # Usage
# # s1 = Singleton()
# # s2 = Singleton()

# # print(s1 is s2)  # True
