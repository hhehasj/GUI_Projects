import customtkinter as ctk


class Game_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Game On")
        self.geometry("920x550")
