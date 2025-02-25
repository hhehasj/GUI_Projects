import customtkinter as ctk


class Game_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Game On")
        self.geometry("920x550")

        self.greeting_lbl = ctk.CTkLabel(
            self,
            text="GUESSING GAME!!!",
            bg_color="green",
            font=("Helvetica", 75, "bold"),
            text_color="white",
            corner_radius=20,
        )
        self.greeting_lbl.place(
            relx=0.5, rely=0.3, anchor="center", relwidth=0.9, relheight=0.15
        )

        Guesses = ctk.IntVar()
        self.input_field = ctk.CTkEntry(self,
                                        placeholder_text="Enter your guesses here.",
                                        textvariable=Guesses,
                                        border_color="black",
                                        border_width=2,
                                        font=("Helvetica", 20, "bold"))
        self.input_field.place(relx=0.4, rely=0.7, anchor="center",
                               relwidth=0.4, relheight=0.08)

        # self.mechanics_lbl =
        # self.mechanics_lbl.place()
        #
        # self.submit_btn =
        # self.submit_btn.place()

    def start_loop(self):
        self.mainloop()