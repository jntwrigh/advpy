class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            return cls._instance
        cls._instance = object.__new__(cls)
        cls._instance.args = list(args)
        cls._instance.kwargs = kwargs
        return cls._instance


s1 = Singleton(10)
s1.args[0] += 1
s2 = Singleton()
print(s2.args[0])


class SubSingleton(Singleton):
    pass


s3 = SubSingleton()
print(s3.args[0])
