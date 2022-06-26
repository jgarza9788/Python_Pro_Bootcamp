
# docs for pixela
# https://docs.pixe.la/

import os,json
import requests

DIR = os.path.dirname(os.path.realpath(__file__))

def get_data(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def set_data(data,file):
    # self.sort()
    with open(file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)

config_file = os.path.join(DIR,'config.json')
config_data = get_data(config_file)
# set_data(config_data,config_file)

# print(config_data)

pixela_url = 'https://pixe.la'
pixela_user_endpoint = '/v1/users'
pixela_graph_endpoint = f"{pixela_url}/{pixela_user_endpoint}/{config_data['username']}/graphs/"
pixela_pixel_endpoint = f"{pixela_url}/{pixela_user_endpoint}/{config_data['username']}/graphs/graph0"
pixela_token = config_data['pixela_token']
pixela_header = {
    "X-USER-TOKEN":pixela_token
}

# print(pixela_graph_endpoint)
"""
# used to create a new user...
user_params = {
    "token": pixela_token,
    "username":"jgarza9788",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(url=pixela_url + pixela_user_endpoint,json=user_params)
print(response.status_code)
print(response.text)
print(response.json())
"""

"""
# used to create a graph
graph_colors = {
    "green":"shibafu",
    "red":"momiji",
    "blue":"sora",
    "yellow":"ichou",
    "purple":"ajisai",
    "black":"kuro",
}

graph_config ={
    "id":"graph0",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":graph_colors['purple']
}

response = requests.post(url=pixela_graph_endpoint,headers=pixela_header,json=graph_config)
print(response.status_code)
print(response.text)
# print(response.json())
"""

"""
pixel_config = {
    "date":"20220625",
    "quantity":"5.5",
}

response = requests.post(url=pixela_pixel_endpoint,headers=pixela_header,json=pixel_config)
print(response.status_code)
print(response.text)
"""

"""
# returns the data as an html/SVG
response = requests.get(url=pixela_pixel_endpoint,headers=pixela_header) #,json=pixel_config)
print(response.status_code)
print(response.text)
"""

"""
# open graph in chrome...
os.system('start chrome ' + pixela_graph_endpoint + 'graph0.html')
"""