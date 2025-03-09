import customtkinter as ctk
from PIL import Image


class Game_Window(ctk.CTk):
    class MechanicsContent(ctk.CTkLabel):
        def __init__(self, parent, start_position: float, end_position: float):
            super().__init__(master=parent)

            self.start_position = start_position
            self.end_position = end_position
            self.position = start_position
            self.in_start_position = True

            self.configure(fg_color="transparent",
                           font=("Arial", 15, "bold"),
                           text="Enter your guess in the Empty Box. For every\nwrong guess, the guess counter increases.\nThe lower the guess counts, the better.\n😁",
                           )
            self.place(relx=0.225, rely=start_position, anchor="center", relwidth=0.35, relheight=0.2)

        def animate(self, event):  # allows the frame to move up or down when dropdown_button is pressed
            if self.in_start_position:
                self.animate_down()

            else:
                self.animate_up()

        def animate_down(self):
            if self.position < self.end_position:

                self.position += 0.01
                self.place_configure(rely=self.position)
                self.after(15, self.animate_down)

            else:
                self.in_start_position = False

        def animate_up(self):
            if self.position > self.start_position:

                self.position -= 0.01
                self.place_configure(rely=self.position)
                self.after(15, self.animate_up)

            else:
                self.in_start_position = True

    def __init__(self):
        super().__init__()

        self.title("Game On")
        self.geometry("920x550")

        # Frames
        self.hidden_frame = ctk.CTkFrame(self,
                                         fg_color="transparent",
                                         corner_radius=1,
                                         )
        self.hidden_frame.place(relx=0.225, rely=0.25, anchor="center",
                                relwidth=0.35, relheight=0.2)

        self.submit_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.submit_frame.place(relx=0.25, rely=0.8, anchor="center",
                                relwidth=0.4, relheight=0.1)

        # WIDGETS
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
                                        border_width=3, )
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

        self.content_of_mechanics_btn = self.MechanicsContent(self, start_position=0.25, end_position=0.55)

        self.mechanics_btn = ctk.CTkButton(self, text="Mechanics of the Game",
                                           # image=,
                                           # compound=,
                                           font=("Arial", 18, "bold"),
                                           border_color="black",
                                           border_width=2,
                                           border_spacing=20,
                                           anchor="w"
                                           )
        self.mechanics_btn.place(relx=0.225, rely=0.4, anchor="center",
                                 relwidth=0.35, relheight=0.1)

        self.mechanics_btn.bind("<Button-1>", self.content_of_mechanics_btn.animate)

        # The content goes behind the hidden_frame then the hidden_frame is behind greeting_lbl
        self.greeting_lbl.lower()
        self.hidden_frame.lower()
        self.content_of_mechanics_btn.lower()

    def start_loop(self):
        self.mainloop()

    def


class GuessCounter(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)



