# just makes some folders

import os


DIR = os.path.dirname(os.path.realpath(__file__))
DIR_Resources = os.path.join(DIR,'Resources')


for i in range(100):
    # print('Resources\\Sections'+i)
    try:
        temp = os.path.join(DIR_Resources,'Section' + str(i+1))
        os.mkdir(temp)
    except:
        pass


