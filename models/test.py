import json

class Home():

    attr1 = "none"
    attr2 = 13
    dic = {}

    def func(self):
        return ("this is a test for json")

    def to_dic(self):
        self.dic = {"obj" : self}

    def save(self):
        with open("file.json", "w") as fjson:
            json.dump(self.dic, fjson, indent=4)

ham1 = Home()

dec = {"abc" : 15}

print(str(dec["abc"]))