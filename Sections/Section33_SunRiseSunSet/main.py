# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.raise_for_status())
# print(response.json())


import requests

parameters = {
    "lat":35.227085,
    "lng":-80.843124
}

response = requests.get(url="http://api.sunrise-sunset.org/json",params=parameters)
print(response)
print(response.raise_for_status())
print(response.json())