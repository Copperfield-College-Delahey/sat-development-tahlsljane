# Code for the menu page

import customtkinter as ctk

class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        # Content
        menuFrame = ctk.CTkFrame(self, fg_color="#D9EDFF") 
        menuFrame.pack(padx=20, pady=50)
        heading = ctk.CTkLabel(menuFrame, text="Menu", font=("Georgia", 32, "bold", "italic", "underline"), text_color="#0D2B50")
        heading.pack(expand=True, padx=10, pady=10)
        homeButton = ctk.CTkButton(menuFrame, text="Home", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        homeButton.pack(expand=True, padx=10, pady=10)
        strategiesButton = ctk.CTkButton(menuFrame, text="Strategies", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        strategiesButton.pack(expand=True, padx=10, pady=10)
        meditationButton = ctk.CTkButton(menuFrame, text="Meditation", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        meditationButton.pack(expand=True, padx=10, pady=10)
        journalButton = ctk.CTkButton(menuFrame, text="Journal Writing", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        journalButton.pack(expand=True, padx=10, pady=10)
        chatbotButton = ctk.CTkButton(menuFrame, text="Chatbot", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        chatbotButton.pack(expand=True, padx=10, pady=10)
        helpButton = ctk.CTkButton(menuFrame, text="Help & FAQs", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        helpButton.pack(expand=True, padx=10, pady=10)
        lifelinesButton = ctk.CTkButton(menuFrame, text="Lifelines", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
        lifelinesButton.pack(expand=True, padx=10, pady=10)
        



        