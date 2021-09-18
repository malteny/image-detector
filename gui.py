# 21-09-18: Problems with styling, tkk.Style() does not seem to apply.

import tkinter as tk
from tkinter import ttk


def create_text_frame(container):
    '''Create frame with instruction text'''

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


def create_button_frame(container):
    '''Create frame with "browse" button'''

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    button = ttk.Button(
        frame,
        text = 'Browse',
        style = 'TButton'
    )

    button.pack()

    return frame


def create_main_frame(container):
    ''' Creates main frame inside window '''

    frame = ttk.Frame(
        container,
        padding = (5,5,5,5),
        style = 'TFrame',
        height = 50,
        width = 40
        )

    return frame


def create_main_window():
    '''Create window and start loop'''

    window = tk.Tk()
    window.title('image-detector')
    window.geometry('400x200')
    s = ttk.Style()

    main_frame = create_main_frame(window).pack()
    create_text_frame(main_frame).pack()
    create_button_frame(main_frame).pack()

    window.mainloop()


if __name__ == '__main__':
    create_main_window()
