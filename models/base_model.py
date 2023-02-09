#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the BaseModel Class"""
    
    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key =='created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dictionary = {'__class__':self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == 'updated_at' or key == 'created_at':
                value = value.isoformat()
            dictionary[key] = value
        return dictionary

def main():
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    print(my_model.to_dict())
    my_model_json = my_model.to_dict()
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    print('---------------------------------------------------------------')
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))
    print('-----------------------------------------------')
    print(my_model is my_new_model)
if __name__ == '__main__':
    main()

