import customtkinter as ctk


class Game_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Game On")
        self.geometry("920x550")

        # Frames
        self.test_frame = ctk.CTkFrame(self, fg_color="red")
        self.test_frame.place(relx=0.5, rely=0.6, anchor="center",
                              relwidth=0.3, relheight=0.3)

        self.submit_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.submit_frame.place(relx=0.25, rely=0.8, anchor="center",
                                relwidth=0.4, relheight=0.1)

        self.greeting_lbl = ctk.CTkLabel(
            self,
            text="GUESSING GAME!!!",
            bg_color="green",
            font=("Helvetica", 75, "bold"),
            text_color="white",
            corner_radius=20,
        )
        self.greeting_lbl.place(
            relx=0.5, rely=0.2, anchor="center", relwidth=0.9, relheight=0.15
        )

        self.submit_btn = ctk.CTkButton(self.submit_frame,
                                        text="Submit",
                                        font=("Arial", 18, "bold"),
                                        border_color="black",
                                        border_width=3,)
        self.submit_btn.place(relx=0.15, rely=0.5, anchor='center',
                              relwidth=0.3, relheight=1)

        Guesses = ctk.IntVar()
        self.input_field = ctk.CTkEntry(self.submit_frame,
                                        placeholder_text="Enter your guesses here.",
                                        textvariable=Guesses,
                                        border_color="black",
                                        border_width=3,
                                        font=("Helvetica", 18, "bold"))
        self.input_field.place(relx=0.65, rely=0.5, anchor="center",
                               relwidth=0.7, relheight=1)

        self.mechanics_btn = ctk.CTkButton(self, text="Mechanics of the Game",
                                         # image=,
                                           font=("Arial", 18, "bold"),
                                           border_color="black",
                                           border_width=2,
                                           border_spacing=20,
                                           anchor="w"
                                           )
        self.mechanics_btn.place(relx=0.225, rely=0.4, anchor="center",
                                 relwidth=0.35, relheight=0.1)

        self.content_of_mechanics_btn = ctk.CTkLabel(self, text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonum",
                                                     font=("Helvetica", 15),
                                                     )
        self.content_of_mechanics_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.content_of_mechanics_btn.lower()

    def mouse_inbounds(self, event):
        print("Mouse inside frame")

    def start_loop(self):
        self.mainloop()
