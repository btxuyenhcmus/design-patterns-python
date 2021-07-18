def showAllView(list):
    print("IN our db we have {} users. Here they are:".format(len(list)))
    for item in list:
        print(item)


def startView():
    print("MVC - the simplest example")
    print("Do you want to see everyone in my db?[y/n]")


def endView():
    print("Goodbye!")
