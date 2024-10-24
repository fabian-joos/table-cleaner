import tkinter as tk
#from tkinter import ttk

from view import TcView


if __name__ == "__main__":
    root = tk.Tk()
    view = TcView(root)
    root.mainloop()