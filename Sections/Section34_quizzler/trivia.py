# import requests


# difficulties = [
#     'easy',
#     'medium',
#     'hard'
# ]

# def get_trivia(difficulty=''):
#     url = f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}&type=boolean'
#     response = requests.get(url)

#     print(response.status_code)
#     print(response.raise_for_status)
#     if response.status_code == 200:
#         return response.json()['results']
#     else:
#         return []



# if __name__ == '__main__':
#     print(get_trivia())
