#

import tkinter as tk
from tkinter import ttk

import gui


def startup():
    ''' Create window and start loop '''

    window = tk.Tk()
    window.title('image-detector')
    window.geometry('400x200')
    window['bg'] = '#f3e6fa'
    s = ttk.Style()

    s.configure('TFrame', background = window['bg'])
    s.configure('TButton', sticky = 'e', background = window['bg'])
    s.configure('TLabel', background = window['bg'])

    main_frame = gui.create_main_frame(window)
    gui.create_text_frame(main_frame).pack()
    gui.create_info_frame(main_frame).pack()
    main_frame.pack()

    window.mainloop()



if __name__ == '__main__':
    startup()
