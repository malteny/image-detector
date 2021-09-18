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


def create_browse_frame(container):
    '''Create frame with "browse" button and entry widget'''

    frame = ttk.Frame(
        container,
        style = 'TFrame'
    )

    button = ttk.Button(
        frame,
        text = 'Browse',
        style = 'TButton'
    )

    entry = ttk.Entry(
        frame,
        style = 'TEntry',
        width = 20
        )

    entry.grid(row = 0, column = 0)
    button.grid(row = 0, column = 1)

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


def create_main_window():
    '''Create window and start loop'''

    window = tk.Tk()
    window.title('image-detector')
    window.geometry('400x200')
    s = ttk.Style()
    s.configure('TFrame', background = '#f3e6fa')
    s.configure('TButton', sticky = 'e')

    main_frame = create_main_frame(window)
    create_text_frame(main_frame).pack()
    create_browse_frame(main_frame).pack()
    main_frame.pack()

    window.mainloop()


if __name__ == '__main__':
    create_main_window()
