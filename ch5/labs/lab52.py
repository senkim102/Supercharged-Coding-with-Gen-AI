# from dataclasses import dataclass
# from unittest import TestCase, main


# class Singleton(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls.__name__] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls.__name__]


# @dataclass
# class Environment(metaclass=Singleton):
#     name: str = 'Production' # This is the default environment
#     version: int = 1


# if __name__ == "__main__":
#     main()
from dataclasses import dataclass
from unittest import TestCase, main


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls.__name__] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls.__name__]


@dataclass
class Environment(metaclass=Singleton):
    name: str = 'Production'
    version: int = 1


class TestEnvironment(TestCase):

    def test_singleton_instance(self):
        env1 = Environment()
        env2 = Environment()

        self.assertEqual(env1, env2)


if __name__ == "__main__":
    main()