# Code for the strategies page

import customtkinter as ctk

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.showFrame = controller

        # Page content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#D9EDFF") 
        strategiesFrame.pack(padx=20, pady=50)
        happyLabel = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        happyLabel.pack(expand=True, padx=10, pady=10)

