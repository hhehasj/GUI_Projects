import customtkinter as ctk


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("920x550")

        greeting_lbl = ctk.CTkLabel(self, text="GUESSING GAME!!!",
                                    bg_color="green",
                                    font=("Helvetica", 75, "bold"),
                                    text_color="white",
                                    corner_radius=20)
        greeting_lbl.place(relx=0.5, rely=0.3, anchor="center",
                           relwidth=0.9, relheight=0.15)

        start_btn = ctk.CTkButton(self, text="GAME ON!!!",
                                  font=("Calibri", 25),
                                  fg_color="#ebebeb",
                                  text_color="red",
                                  hover_color="red",
                                  border_color="red",
                                  border_width=2
                                  )
        start_btn.place(relx=0.3, rely=0.5, anchor="center",
                        relwidth=0.17, relheight=0.1)

        leaderboard_btn = ctk.CTkButton(self, text="Leaderboard",
                                        font=("Calibri", 25),
                                        fg_color="#ebebeb",
                                        text_color="green",
                                        hover_color="#008000",
                                        border_color="green",
                                        border_width=2)
        leaderboard_btn.place(relx=0.7, rely=0.5, anchor="center",
                              relwidth=0.17, relheight=0.1)


window = Main()
window.mainloop()
