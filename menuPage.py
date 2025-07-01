# Code for the menu page

import customtkinter as ctk

class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=1) 

menu = ctk.CTk()
menu.title("Menu")
menu.geometry("1000x700")
menu.configure(fg_color="#E9F5FF")

# Title & icon
headingFrame = ctk.CTkFrame(menu, fg_color="#EDF5FB", height=30)
headingFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

menuIcon = ctk.CTkLabel(headingFrame, text="|||", font=("Arial", 30), text_color="black")
menuIcon.place(x=20, y=10)

heading = ctk.CTkLabel(headingFrame, text="Menu", font=("Georgia", 32, "bold", "italic", "underline"), text_color="#0D2B50")
heading.place(relx=0.5, rely=0.5, anchor="center")

# Buttons
buttonsFrame = ctk.CTkFrame(menu, fg_color="#D9EDFF")
buttonsFrame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
buttonsFrame.grid_rowconfigure((0), weight=1)
buttonsFrame.grid_rowconfigure((1), weight=1)
buttonsFrame.grid_rowconfigure((2), weight=1)
buttonsFrame.grid_rowconfigure((3), weight=1)
buttonsFrame.grid_rowconfigure((4), weight=1)
buttonsFrame.grid_rowconfigure((5), weight=1)
buttonsFrame.grid_rowconfigure((6), weight=1)

strategiesButton = ctk.CTkButton(buttonsFrame, text="Strategies", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
strategiesButton.pack(expand=True, padx=10, pady=10)

meditationButton = ctk.CTkButton(buttonsFrame, text="Meditation", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
meditationButton.pack(expand=True, padx=10, pady=10)

journalButton = ctk.CTkButton(buttonsFrame, text="Journal Writing", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
journalButton.pack(expand=True, padx=10, pady=10)

chatbotButton = ctk.CTkButton(buttonsFrame, text="Chatbot", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
chatbotButton.pack(expand=True, padx=10, pady=10)

helpButton = ctk.CTkButton(buttonsFrame, text="Help & FAQs", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
helpButton.pack(expand=True, padx=10, pady=10)

lifelinesButton = ctk.CTkButton(buttonsFrame, text="Lifelines", fg_color="transparent", text_color="black", font=("Georgia", 24, "italic", "underline"), hover_color="#E9F5FF")
lifelinesButton.pack(expand=True, padx=10, pady=10)


menu.mainloop()