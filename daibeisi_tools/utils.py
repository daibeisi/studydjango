from threading import Lock
import logging

# Default logger
log = logging.getLogger()


def logger():
    return log


class SingletonMeta:
    """
    This is a thread-safe implementation of Singleton.

    Changes to the value of the `__init__` argument affect the returned instance.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance


# class SingletonMeta(type):
#     """
#     This is a thread-safe implementation of Singleton.
#
#     Possible changes to the value of the `__init__` argument do not affect the returned instance.
#     """
#
#     _instances = {}
#
#     _lock: Lock = Lock()
#
#     def __call__(cls, *args, **kwargs):
#         with cls._lock:
#             if cls not in cls._instances:
#                 instance = super().__call__(*args, **kwargs)
#                 cls._instances[cls] = instance
#         return cls._instances[cls]

# class Singleton(type):
#     """
#     An metaclass for singleton purpose. Every singleton class should inherit from this class by 'metaclass=Singleton'.
#     """
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         key = (args, tuple(sorted(kwargs.items())))
#         if cls not in cls._instances:
#             cls._instances[cls] = {}
#         if key not in cls._instances[cls]:
#             cls._instances[cls][key] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls][key]


if __name__ == '__main__':
    class A(SingletonMeta):
        def __init__(self, code):
            self.code = code
    a = A("1212")
    b = A("2313")
    print(1)
