# Code for the strategies page

import customtkinter as ctk

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.showFrame = controller

        def showStrategies():
            if happyLabel:
                happyLabel.configure(text="test")

        # Page content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#D9EDFF") 
        strategiesFrame.pack(padx=20, pady=50)
        happyLabel = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        happyLabel.pack(expand=True, padx=10, pady=10)
        sadLabel = ctk.CTkButton(strategiesFrame, text="Sad", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        sadLabel.pack(expand=True, padx=10, pady=10)
        angryLabel = ctk.CTkButton(strategiesFrame, text="Angry", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        angryLabel.pack(expand=True, padx=10, pady=10)
        frustratedLabel = ctk.CTkButton(strategiesFrame, text="Frustrated", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        frustratedLabel.pack(expand=True, padx=10, pady=10)
        stressedLabel = ctk.CTkButton(strategiesFrame, text="Stressed", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#E9F5FF")
        stressedLabel.pack(expand=True, padx=10, pady=10)

