import os
import json5 as json


class User_Data:
    def __init__(self):
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.file = os.path.join(self.DIR, 'user_data.json')
        self.data = self.get_data(self.file)

    def get_data(self,file):
        try:
            with open(file,'r',encoding='utf-8') as f:
                return json.load(f)
        except:
            return []

    def set_data(self,data,file):
        with open(file,'w',encoding='utf-8') as f:
            json.dump(data,f,indent=4)

    def save(self):
        self.set_data(self.data,self.file)