class TcController():
    def __init__(self, view):
        self.view = view
        self.setup()

    def setup(self):
        self.view.load_file_button.config(command=self.load_file_button_click)

    def load_file_button_click(self):
        print("Load file button clicked!")