import os, json


class highscore_manager:
    def __init__(self,dir=None,file_name='HS.json'):

        if dir == None:
            dir = os.path.dirname(os.path.realpath(__file__))

        self.dir = dir
        self.file = os.path.join(self.dir,file_name)
        self.data = self.get_data()

    def sorthelper(self,i):
        return i['score']

    def sort(self):
        self.data.sort(key=self.sorthelper,reverse=True)

    def get_top(self,top=10):
        self.sort()
        td = self.data[:top]
        l = ['{name}: {score:.0f}'.format(name=i['name'],score=i['score']) for i in td]
        return '\n'.join(l)

    def nth_score(self,n=10):
        self.sort()
        try:
            return self.data[n]['score']
        except:
            return 0

    def get_data(self):
        try:
            with open(self.file,'r',encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def set_data(self):
        self.sort()
        with open(self.file,'w',encoding='utf-8') as f:
            json.dump(self.data,f,indent=4)

    def save(self):
        self.set_data()
        


if __name__ == '__main__':
    pass

    # DIR = os.path.dirname(os.path.realpath(__file__))
    # HSM = highscore_manager(file_name='test.json')
    # print(HSM.data)
    # HSM.data.append({'name':'X','score':200})
    # HSM.data.append({'name':'A','score':50000})
    # HSM.set_data()
    # print(HSM.get_top(5))