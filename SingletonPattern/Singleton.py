class Singleton():

    _instance = None

    def __new__(cls):
        
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

    

if __name__ == "__main__":

    a = Singleton()
    b = Singleton()
    c = Singleton()

    print(id(a))
    print(id(b))
    print(id(c))