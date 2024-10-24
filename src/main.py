import tkinter as tk
from view import TcView
from controller import TcController

if __name__ == "__main__":
    root = tk.Tk()
    view = TcView(root)
    controller = TcController(view)
    root.mainloop()