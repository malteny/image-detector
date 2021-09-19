# 21-09-18: Problems with styling, tkk.Style() does not apply on mac.

import requests
import json

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from analyzer import analyze_image


def enter_path():
    '''
    Opens file dialog, selected png file is saved in StringVar
    dir_selected.
    '''
    dialog_response = filedialog.askopenfilename(
        filetypes=[("jpeg file", "*.jpg")]
    )

    dir_selected.set(dialog_response)


def get_selected_path():
    ''' Used to access StringVar dir_selected '''
    return dir_selected.get()


def create_text_frame(container):
    ''' Create frame with text prompt '''

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    label = ttk.Label(
        frame,
        text = 'Browse for a photo to identify',
        style = 'TLabel'
    )

    label.pack()

    return frame


def create_browse_frame(container):
    '''
    Create frame with "browse" button, entry widget and
    submit button. Instantiates dir_selected globally.
    '''

    global dir_selected
    dir_selected = tk.StringVar()

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    choose_button = ttk.Button(
        frame,
        text = 'Browse',
        style = 'TButton',
        command = enter_path
    )

    entry = ttk.Entry(
        frame,
        style = 'TEntry',
        width = 20,
        textvariable = dir_selected
        )

    analyze_button = ttk.Button(
        frame,
        text = 'Analyze',
        style = 'TButton',
        command = analyze_image
        )

    entry.grid(row = 0, column = 0)
    choose_button.grid(row = 0, column = 1)
    analyze_button.grid(row = 1, column = 1)

    return frame


def create_main_frame(container):
    ''' Creates main frame inside window '''

    frame = ttk.Frame(
        container,
        padding = (20, 20, 20, 20),
        style = 'TFrame',
        height = 50,
        width = 40
        )

    return frame


def analyze_image():
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
