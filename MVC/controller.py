from model import Persion
import view


def showAll():
    people_in_db = Persion.getAll()
    return view.showAllView(people_in_db)


def start():
    view.startView()
    inp = input()
    if inp == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    start()