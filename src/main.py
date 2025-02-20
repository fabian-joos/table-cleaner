import tkinter as tk
from view import TcView
from model import TcModel
from controller import TcController

if __name__ == "__main__":
    root = tk.Tk()
    model = TcModel()
    view = TcView(root)
    controller = TcController(view, model)
    root.mainloop()
    