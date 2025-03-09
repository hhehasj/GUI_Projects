import customtkinter as ctk
from game_window import Game_Window


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("920x550")

        def show_username_window():
            # hasattr() prevents an AttributeError caused by .winfo_exists()
            # It checks if the object contains the attribute(prefix: self.) in "attr"
            if hasattr(self, "username_window") and self.username_window.winfo_exists():
                self.username_window.destroy()

            self.username_window = Username_window(self.master)

        self.greeting_lbl = ctk.CTkLabel(
            self,
            text="GUESSING GAME!!!",
            bg_color="green",
            font=("Helvetica", 75, "bold"),
            text_color="white",
            corner_radius=20,
        )
        self.greeting_lbl.place(
            relx=0.5, rely=0.25, anchor="center", relwidth=0.9, relheight=0.15
        )

        self.start_btn = ctk.CTkButton(
            self,
            text="GAME ON!!!",
            font=("Calibri", 25),
            fg_color="#ebebeb",
            text_color="red",
            hover_color="red",
            border_color="red",
            border_width=3,
            command=show_username_window,
        )
        self.start_btn.place(
            relx=0.3, rely=0.5, anchor="center", relwidth=0.17, relheight=0.1
        )

        self.leaderboard_btn = ctk.CTkButton(
            self,
            text="Leaderboard",
            font=("Calibri", 25),
            fg_color="#ebebeb",
            text_color="green",
            hover_color="#008000",
            border_color="green",
            border_width=3,
        )
        self.leaderboard_btn.place(
            relx=0.7, rely=0.5, anchor="center", relwidth=0.17, relheight=0.1
        )


class Username_window(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master=parent)

        def show_game_window():
            self.parent_name = self.winfo_parent()
            self.parent_window = self.nametowidget(self.parent_name)

            Game_Window(self.master)
            if self.parent_window:
                self.parent_window.withdraw()
                self.withdraw()

        self.geometry("300x185")
        self.title("Enter Username")
        self.attributes("-topmost", True)

        self.text_msg = ctk.CTkLabel(
            self, text="Enter your username:", font=("Arial", 25)
        )
        self.text_msg.place(relx=0.5, rely=0.2, anchor="center")

        Username_variable = ctk.StringVar()
        self.username_input = ctk.CTkEntry(
            self,
            textvariable=Username_variable,
            font=("Arial", 15),
            border_width=3,
            border_color="black",
        )
        self.username_input.place(
            relx=0.5, rely=0.45, anchor="center", relwidth=0.8, relheight=0.18
        )

        self.enter_btn = ctk.CTkButton(
            self,
            text="Enter",
            font=("Calibri", 28, "bold"),
            border_width=3,
            border_color="black",
            border_spacing=2,
            corner_radius=7,
            command=show_game_window,
        )
        self.enter_btn.place(
            relx=0.5, rely=0.72, anchor="center", relwidth=0.25, relheight=0.2
        )


main_window = Main()
main_window.mainloop()
