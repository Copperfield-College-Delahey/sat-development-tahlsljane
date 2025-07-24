# Code for the strategies page

import customtkinter as ctk

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.showFrame = controller

        # Page content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#EDF5FB") 
        strategiesFrame.pack(padx=20, pady=50)
        happyButton = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        happyButton.pack(expand=True, padx=10, pady=10)
        sadButton = ctk.CTkButton(strategiesFrame, text="Sad", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        sadButton.pack(expand=True, padx=10, pady=10)
        angryButton = ctk.CTkButton(strategiesFrame, text="Angry", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        angryButton.pack(expand=True, padx=10, pady=10)
        frustratedButton = ctk.CTkButton(strategiesFrame, text="Frustrated", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        frustratedButton.pack(expand=True, padx=10, pady=10)
        stressedButton = ctk.CTkButton(strategiesFrame, text="Stressed", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        stressedButton.pack(expand=True, padx=10, pady=10)

