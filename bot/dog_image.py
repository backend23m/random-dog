import requests

def get_dog_image():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['url']
    
    raise ValueError('image not found.')

