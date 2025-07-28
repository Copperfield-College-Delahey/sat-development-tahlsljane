# Code for the strategies page

import customtkinter as ctk

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        def Happy():
            if happyButton:
                happyText.configure(text="yay")
        def Sad():
            if sadButton:
                sadText.configure(text=":(")

        # Page content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#EDF5FB") 
        strategiesFrame.pack(padx=20, pady=50)

        happyButton = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Happy)
        happyButton.grid(row=0, column=0)
        happyText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15, "italic"))
        happyText.grid(row=1, column=0)

        sadButton = ctk.CTkButton(strategiesFrame, text="Sad", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Sad)
        sadButton.grid(row=2, column=0)
        sadText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15, "italic"))
        sadText.grid(row=3, column=0)

        angryButton = ctk.CTkButton(strategiesFrame, text="Angry", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5")
        angryButton.grid(row=4, column=0)
        angryText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15, "italic"))
        angryText.grid(row=5, column=0)

        frustratedButton = ctk.CTkButton(strategiesFrame, text="Frustrated", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5")
        frustratedButton.grid(row=6, column=0)
        frustratedText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15, "italic"))
        frustratedText.grid(row=7, column=0)
        
        stressedButton = ctk.CTkButton(strategiesFrame, text="Stressed", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5")
        stressedButton.grid(row=8, column=0)
        stressedText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15, "italic"))
        stressedText.grid(row=9, column=0)

