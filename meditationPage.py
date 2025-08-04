# Code for the meditation page

import customtkinter as ctk

class MeditationPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        # Page content
        mainFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        mainFrame.pack(padx=20, pady=50) 

        questionText = ctk.CTkLabel(mainFrame, text="How long would you like?", text_color="black", font=("Georgia", 24, "bold"))
        questionText.grid(row=0, column=0, columnspan=3, sticky="nsew")

        filler = ctk.CTkLabel(mainFrame, text="")
        filler.grid(row=1, column=0)

        tenMinutes = ctk.CTkButton(mainFrame, text="10 minutes", text_color="#0D2B50", fg_color="transparent", hover_color="#CCE3F5", font=("Georgia", 15, "italic", "bold", "underline"))
        tenMinutes.grid(row=2, column=0, sticky="nsew")

        thirtyMinutes = ctk.CTkButton(mainFrame, text="30 minutes", text_color="#0D2B50", fg_color="transparent", hover_color="#CCE3F5", font=("Georgia", 15, "italic", "bold", "underline"))
        thirtyMinutes.grid(row=2, column=1, sticky="nsew")

        oneHour = ctk.CTkButton(mainFrame, text="1 hour", text_color="#0D2B50", fg_color="transparent", hover_color="#CCE3F5", font=("Georgia", 15, "italic", "bold", "underline"))
        oneHour.grid(row=2, column=2, sticky="nsew")