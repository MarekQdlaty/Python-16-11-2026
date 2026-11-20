# tkinter, pyQt, PySide, gtk+
# customtkinter

import tkinter


class MyGui:
    """
    Okienko
    """

    def __init__(self):
        self.main_window = tkinter.Tk()

        tkinter.mainloop()


my_gui = MyGui()
