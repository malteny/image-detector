import requests
import json


def analyze_image(file_path):
    '''
    Sends file specified by path to openvisionapi and returns
    tuple of prediction and accuracy.
    '''
    URL = 'https://api.openvisionapi.com'
    PATH = '/api/v1/detection'

    with open(file_path, 'rb') as f:
        image_bytes = f.read()

    url = URL + PATH

    files = {'image': (file_path, image_bytes, 'image/jpeg')}

    body = {'model': 'yolov4'}

    response = requests.post(url=url, files=files, data=body)

    json_response = response.json()

    if json_response['description'] == 'Detected objects':
        return (json_response['predictions']['label'],
                json_response['predictions']['score'])
