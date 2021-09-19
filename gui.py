# 21-09-18: Problems with styling, tkk.Style() does not apply on mac.

import requests
import json

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def enter_path(dir_selected):
    '''
    Opens file dialog, selected png file is saved in StringVar
    dir_selected.
    '''
    # Save chosen file path
    dialog_response = filedialog.askopenfilename(
        filetypes=[("jpeg file", "*.jpg")]
    )

    # Set StringVar value to file path
    return dir_selected.set(dialog_response)


def get_selected_path(dir_selected):
    ''' Used to access StringVar dir_selected '''
    # Return StringVar file path
    return dir_selected.get()


def update_result(result_text, result):
    return result_text.set(result)


def create_text_frame(container):
    ''' Create frame with text prompt '''

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    # Actual text displayed
    label = ttk.Label(
        frame,
        text = 'Browse for a photo to identify',
        style = 'TLabel'
    )

    label.pack()

    return frame


def create_info_frame(container):
    '''
    Create frame with "browse" button, entry widget and
    submit button. Instantiates dir_selected.
    '''

    # If StringVar dir_selected is changed, text in entry is updated
    dir_selected = tk.StringVar()
    result_text = tk.StringVar()

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    # Button which allows you to browse for files
    choose_button = ttk.Button(
        frame,
        text = 'Browse',
        style = 'TButton',
        command = lambda: enter_path(dir_selected)
    )

    # Text field which displays chosen path
    entry = ttk.Entry(
        frame,
        style = 'TEntry',
        width = 20,
        textvariable = dir_selected
    )

    # Text field which contains image result / error messages
    results_label = ttk.Label(
        frame,
        style = 'TLabel',
        width = 35,
        textvariable = result_text
    )

    # Button to analyze image at specified path, result is displayed
    # in new label in the same frame.
    analyze_button = ttk.Button(
        frame,
        text = 'Analyze',
        style = 'TButton',
        command = lambda: update_result(result_text,
            analyze_image(get_selected_path(dir_selected))
        )
    )

    entry.grid(row = 0, column = 0)
    choose_button.grid(row = 0, column = 1)
    analyze_button.grid(row = 1, column = 1)
    results_label.grid(row = 2, column = 0)

    return frame


def create_results_label(frame, result):
    '''Creates label contiaining results of query'''

    return results_label


def create_main_frame(container):
    ''' Creates main frame inside window '''

    frame = ttk.Frame(
        container,
        padding = (20, 20, 20, 20),
        style = 'TFrame',
        height = 50,
        width = 55
        )

    return frame


def analyze_image(file_path):
    '''
    Sends file specified by path to openvisionapi and returns
    tuple containing item predictions and accuracy.
    '''
    URL = 'https://api.openvisionapi.com'
    PATH = '/api/v1/detection'

    if not file_path:
        return 'No path specified'

    try:
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
    except FileNotFoundError:
        return 'File not found, try another path'

    url = URL + PATH
    files = {'image': (file_path, image_bytes, 'image/jpeg')}
    body = {'model': 'yolov4'}

    response = requests.post(url=url, files=files, data=body)

    json_response = response.json()

    if len(json_response['predictions']) > 0:
        result = []
        for item in json_response['predictions']:
            result.append(item['label'])
            result.append(item['score'])

        return tuple(result)

    else:
        return 'No items were identified, try a different image'
