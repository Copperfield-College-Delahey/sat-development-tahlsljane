# Code for the meditation page

import customtkinter as ctk
from PIL import Image, ImageTk

class MeditationPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        # Page content
        mainFrame = ctk.CTkFrame(self) 
        mainFrame.pack(padx=20, pady=50) 

        tenMinutes = ctk.CTkButton(mainFrame, text="10 minutes", )





















meditation = ctk.CTk()
meditation.title("Meditation")
meditation.geometry("1000x700")
meditation.configure(fg_color="#E9F5FF")

meditation.grid_columnconfigure((0), weight=1)
meditation.grid_rowconfigure((0), weight=1)
meditation.grid_rowconfigure((1), weight=1)
meditation.grid_rowconfigure((2), weight=1)
meditation.grid_rowconfigure((3), weight=1)
meditation.grid_rowconfigure((4), weight=1)

# Title & Frame
titleFrame = ctk.CTkFrame(meditation, fg_color="#EDF5FB", height=30)
titleFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

meditationTitle = ctk.CTkLabel(titleFrame, text="Meditation", text_color="#0D2B50", font=("Georgia", 32, "bold", "underline", "italic"))
meditationTitle.place(relx=0.5, rely=0.5, anchor="center")

menuButton = ctk.CTkButton(titleFrame, text="≡", font=("Arial", 50), text_color="black", fg_color="transparent", hover_color="#D9EDFF")
menuButton.place(x=0, y=0)


# Subtitle frame
subtitleFrame = ctk.CTkFrame(meditation, fg_color="#D9EDFF", height=30)
subtitleFrame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

subtitleText = ctk.CTkLabel(meditation, text="How long would you like?", font=("Georgia", 26, "bold", "italic"), text_color="#0D2B50", fg_color="#D9EDFF")
subtitleText.place(relx=0.5, rely=0.5, anchor="center")

# Times frame
timesFrame = ctk.CTkFrame(meditation, fg_color="#EDF5FB", height=60)
timesFrame.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

tenMinutes = ctk.CTkButton(timesFrame, text="10 minutes", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 20, "italic", "underline", "bold"))
tenMinutes.pack(side="left", expand=True, padx=10, pady=10)

thirtyMinutes = ctk.CTkButton(timesFrame, text="30 minutes", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 20, "italic", "underline", "bold"))
thirtyMinutes.pack(side="left", expand=True, padx=10, pady=10)

oneHour = ctk.CTkButton(timesFrame, text="1 hour", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 20, "italic", "underline", "bold"))
oneHour.pack(side="left", expand=True, padx=10, pady=10)

# Begin Button
beginButton = ctk.CTkButton(meditation, text="Begin", fg_color="#0D2B50", text_color="white", font=("Georgia", 24, "italic", "underline"))
beginButton.grid(row=4, column=0)


meditation.mainloop()