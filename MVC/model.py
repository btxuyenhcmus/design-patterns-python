import json


class Persion(object):
    def __init__(self, first_name=None, last_name=None) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def getAll(self):
        def get(item):
            return Persion(item['first_name'], item['last_name'])
        database = open('db.txt', 'r')
        json_list = json.loads(database.read())
        return list(map(get, json_list))
