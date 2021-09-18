import requests
import json


def analyze_image(file_path):
    ''' Sends file specified by path to openvisionapi and returns result '''
    URL = 'https://api.openvisionapi.com'
    PATH = '/api/v1/detection'

    with open(file_path, 'rb') as f:
        image_bytes = f.read()

    url = URL + PATH

    files = {'image': (file_path, image_bytes, 'image/jpg')}

    body = {'model': 'yolov4'}

    response = requests.post(url=url, files=files, data=body)

    print(response)


analyze_image('cat.jpg')
