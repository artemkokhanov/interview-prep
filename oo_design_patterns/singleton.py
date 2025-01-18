class Singleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("This is a Singleton class.")

    def _init__(self):
        # add initialization logic here
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)  # create new class instance
            cls._instance._init__()  # initialize Singleton instance
        return cls._instance


instance_1 = Singleton.get_instance()
instance_2 = Singleton.get_instance()
print(instance_1 is instance_2)  # This should print True
