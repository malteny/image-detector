
import tkinter as tk
from tkinter import ttk


def create_text_frame(container):

    frame = ttk.Frame(container)

    label = ttk.Label(
        frame,
        text = 'Browse for a photo to identify',
        background = container['bg'],
        font = ('Arial', 20)
    )

    label.pack()

    return frame


def create_button_frame(container):

    frame = ttk.Frame(container)

    button = ttk.Button(
        frame,
        text = 'Browse',
        style = 'TButton'
    )

    button.pack()

    return frame


def create_main_window():
    window = tk.Tk()
    window.title('image-detector')
    window.geometry('500x200')
    window.configure(bg='#D8BFD8')

    text = create_text_frame(window)
    button = create_button_frame(window)

    text.grid( row = 0, column = 0 )
    button.grid( row = 1, column = 2 )

    window.mainloop()


if __name__ == '__main__':
    create_main_window()
