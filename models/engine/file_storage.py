#!/usr/bin/python3
import sys
sys.path.append("..")
from base_model import BaseModel

class FileStorage:

    __file_path = ""
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open("file.json","w") as f:
            f.write(str(self.__objects))
            self.__file_path = "file.json"

    def reload(self):
        if self.__file_path != "":
            with open(self.__file_path,"r") as f:
                data = f.read().replace("\n","")
            self.__objects = data


def main():
    b = BaseModel()
    c = BaseModel()
    File = FileStorage()
    File.new(b)
    File.new(c)
    File.save()

if __name__ == '__main__':
    main()
