from models import Singleton

if __name__ == '__main__':
    instance = Singleton.getInstance("This is the first object!")
    print(instance)

    instance2 = Singleton.getInstance("This is the second object!")
    print(instance2)

    try:
        instance3 = Singleton("This is the thirst object!")
    except Exception as e:
        print(e)