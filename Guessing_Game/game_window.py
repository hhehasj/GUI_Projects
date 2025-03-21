import customtkinter as ctk
from PIL import Image
from random import choice
from string import digits
from tkinter.messagebox import showerror
from database_connection import Update_Guesses


class Game_Window(ctk.CTkToplevel):
    class MechanicsContent(ctk.CTkLabel):
        def __init__(self, parent, start_position: float, end_position: float):
            super().__init__(master=parent)

            self.start_position = start_position
            self.end_position = end_position
            self.position = start_position
            self.in_start_position = True

            self.configure(
                fg_color="transparent",
                font=("Arial", 15, "bold"),
                text="Enter your guess in the Empty Box. For every\nwrong guess, the guess counter increases.\nThe lower the guess counts, the better.\n😁",
            )
            self.place(
                relx=0.225,
                rely=start_position,
                anchor="center",
                relwidth=0.35,
                relheight=0.2,
            )

        def animate(self, event):  # allows the frame to move up or down when dropdown_button is pressed
            def animate_down():
                if self.position < self.end_position:
                    self.position += 0.01
                    self.place_configure(rely=self.position)
                    self.after(15, animate_down)

                else:
                    self.in_start_position = False

            def animate_up():
                if self.position > self.start_position:
                    self.position -= 0.01
                    self.place_configure(rely=self.position)
                    self.after(15, animate_up)

                else:
                    self.in_start_position = True

            if self.in_start_position:
                animate_down()

            else:
                animate_up()

    def __init__(self, parent):
        super().__init__(master=parent)

        self.width_of_screen = self.winfo_screenwidth()
        self.height_of_screen = self.winfo_screenheight()

        self.center_x = int(self.width_of_screen - 920) // 2
        self.center_y = int(self.height_of_screen - 550) // 2

        self.title("Game On")
        self.geometry(f"920x550+{self.center_x}+{self.center_y}")

        self.answer_number: str = choice(digits)
        self.number_of_wrong_guesses: int = 0

        self.down_arrow = ctk.CTkImage(
            light_image=Image.open("./arrows/test_arrow_down.png"),
            dark_image=Image.open("./arrows/test_arrow_down.png"),
        )

        self.up_arrow = ctk.CTkImage(
            light_image=Image.open("./arrows/test_arrow_up.png"),
            dark_image=Image.open("./arrows/test_arrow_up.png"),
        )

        # Frames
        self.hidden_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=1,
        )
        self.hidden_frame.place(
            relx=0.225, rely=0.25, anchor="center", relwidth=0.35, relheight=0.2
        )

        self.submit_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.submit_frame.place(
            relx=0.25, rely=0.8, anchor="center", relwidth=0.4, relheight=0.1
        )

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

        self.submit_btn = ctk.CTkButton(
            self.submit_frame,
            text="Submit",
            font=("Arial", 18, "bold"),
            border_color="black",
            border_width=3,
            corner_radius=1,
            command=self.answer_checker
        )
        self.submit_btn.place(
            relx=0.15, rely=0.5, anchor="center", relwidth=0.3, relheight=1
        )

        self.Guesses = ctk.StringVar()
        self.input_field = ctk.CTkEntry(
            self.submit_frame,
            textvariable=self.Guesses,
            border_color="black",
            border_width=3,
            font=("Helvetica", 18, "bold"),
            corner_radius=1,
        )
        self.input_field.place(
            relx=0.65, rely=0.5, anchor="center", relwidth=0.7, relheight=1
        )

        self.content_of_mechanics_btn = self.MechanicsContent(
            self, start_position=0.25, end_position=0.55
        )

        self.mechanics_btn = ctk.CTkButton(
            master=self,
            text="Mechanics of the Game",
            image=self.down_arrow,
            compound="right",
            font=("Arial", 18, "bold"),
            border_color="black",
            border_width=2,
            border_spacing=20,
        )
        self.mechanics_btn.place(
            relx=0.225, rely=0.4, anchor="center", relwidth=0.35, relheight=0.1
        )

        self.mechanics_btn.bind("<Button-1>", self.content_of_mechanics_btn.animate)
        self.mechanics_btn.bind("<Button-1>", self.change_icon, add="+")

        # The content goes behind the hidden_frame then the hidden_frame is behind greeting_lbl
        self.greeting_lbl.lower()
        self.hidden_frame.lower()
        self.content_of_mechanics_btn.lower()

        self.Counter_Widget = GuessCounter(self)
        self.Counter_Widget.place(
            relx=0.7, rely=0.6, anchor="center", relwidth=0.3, relheight=0.50
        )
        self.Counter_Widget.tries_num_lbl.lower()
        self.Counter_Widget.tries_lbl.lower()
        self.Counter_Widget.correct_answer_lbl.lower()

    def change_icon(self, event):
        if self.content_of_mechanics_btn.in_start_position:
            self.mechanics_btn.configure(image=self.up_arrow)
        else:
            self.mechanics_btn.configure(image=self.down_arrow)

    def answer_checker(self):
        users_answer = self.Guesses.get()

        try:
            if int(users_answer) < 0 or int(users_answer) > 9:
                showerror("Number out of bounds", message="It is only 0 to 9.")

            if users_answer != self.answer_number:
                self.number_of_wrong_guesses += 1

            else:
                self.number_of_wrong_guesses += 1  # This only increments by 1 once. To get the actuall # of guesses.

                self.Counter_Widget.tries_num_lbl.configure(text=f'{self.number_of_wrong_guesses} tries')
                self.Counter_Widget.correct_answer_lbl.configure(text=f'({self.answer_number}) was the answer')
                Update_Guesses(final_num_guesses=self.number_of_wrong_guesses)

                self.Counter_Widget.tries_num_lbl.lift()
                self.Counter_Widget.tries_lbl.lift()
                self.Counter_Widget.correct_answer_lbl.lift()

                # Submit btn changes to the back_btn
                self.back_btn_appear()

            self.Counter_Widget.counter.configure(text=f"{self.number_of_wrong_guesses}")

        except ValueError:
            self.input_field.delete(0, "end")
            showerror("Invalid input", message="Only put digits!")

    def back_btn_appear(self):
        self.input_field.destroy()
        self.submit_btn.configure(text="BACK", command=self.return_to_main_window)
        self.submit_btn.place_configure(relx=0.5, rely=0.5, anchor='center',
                                        relwidth=1, relheight=1)

    def return_to_main_window(self):
        parent = self.winfo_parent()
        parent_window = self.nametowidget(parent)

        parent_window.deiconify()
        self.destroy()


class GuessCounter(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        self.configure(
            fg_color="transparent",
            border_width=3,
            border_color="black",
        )

        self.guesses_lbl = ctk.CTkLabel(
            self,
            text="GUESSES:",
            font=("Arial", 20, "bold"),
        )
        self.guesses_lbl.place(
            relx=0.5, rely=0.02, anchor="n", relwidth=0.5, relheight=0.1
        )

        self.counter = ctk.CTkLabel(
            self,
            text="0",
            font=("Arial", 45, "bold"),
        )
        self.counter.place(
            relx=0.5, rely=0.25, anchor="center", relwidth=0.2, relheight=0.25
        )

        self.tries_lbl = ctk.CTkLabel(
            self,
            text="It took you:",
            font=("Arial", 25, "bold"),
        )

        self.tries_lbl.place(
            relx=0.345,
            rely=0.6,
            anchor="center",
            relwidth=0.48,
            relheight=0.2,
        )

        self.tries_num_lbl = ctk.CTkLabel(
            self,
            text=f"0 tries",
            font=("Arial", 25, "bold"),
        )
        self.tries_num_lbl.place(
            relx=0.755, rely=0.6, anchor="center", relwidth=0.35, relheight=0.2
        )

        self.correct_answer_lbl = ctk.CTkLabel(
            self,
            text="() was the answer",
            font=("Arial", 25, "bold"),
        )
        self.correct_answer_lbl.place(
            relx=0.5, rely=0.8, anchor="center", relwidth=0.8, relheight=0.2
        )
