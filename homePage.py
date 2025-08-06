# Code for the home page

import customtkinter as ctk
from PIL import Image, ImageTk

# Text describing what StudHealth is and its aim
aboutText = (
   "Here at StudHealth, we care about the wellbeing of \nall students - high school and university.\n"
   "We believe that all students should have the ability \nto learn how to deal with any kind of stress they \nexperience, and that is our main goal."
)

aimText = (
    "StudHealth aims to help all students deal with stress and \nanxiety that may arise from studies.\n"
    "We understand how hard it can be to navigate around a tight \nschedule, and we plan on helping \nstudents handle that efficiently and effectively, \nwhile also aiming for the high marks."
)


class HomePage(ctk.CTkFrame): 
    def __init__(self, parent, controller=None): 
        super().__init__(parent, fg_color="#EDF5FB") 

        # Page content -----------------------------------------------------------------------------
        mainFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        mainFrame.pack(padx=20, pady=50, expand=True)
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_rowconfigure(2, weight=1)

        # Text frame -------------------------------------------------------------------------------------
        textFrame = ctk.CTkFrame(mainFrame, fg_color="#EDF5FB")
        textFrame.grid(row=0, column=0, sticky="nsew", padx=10)

        aboutTitle = ctk.CTkLabel(textFrame, text="About Us", text_color="#0D2B50", font=("Georgia", 28, "bold", "underline", "italic"))
        aboutTitle.pack(pady=(0, 10), anchor="center")
        aboutLabel = ctk.CTkLabel(textFrame, text=aboutText, font=("Georgia", 18), text_color="black")
        aboutLabel.pack(anchor="center")

        filler = ctk.CTkLabel(textFrame, text="")
        filler.pack(pady=(0, 10), anchor="center")

        aimTitle = ctk.CTkLabel(textFrame, text="What do we aim for?", text_color="#0D2B50", font=("Georgia", 28, "bold", "underline", "italic"))
        aimTitle.pack(pady=(0, 10), anchor="center")
        aimLabel = ctk.CTkLabel(textFrame, text=aimText, font=("Georgia", 18), text_color="black")
        aimLabel.pack(anchor="center")

        filler = ctk.CTkLabel(mainFrame, text="")
        filler.grid(row=1, column=0)
        
        # Image frame --------------------------------------------------------------------------------
        imageFrame = ctk.CTkFrame(mainFrame, fg_color="#EDF5FB")
        imageFrame.grid(row=2, column=0, sticky="nsew", padx=10)

        originalImage = Image.open("studyingImage.jpg")
        resizedImage = originalImage.resize((250, 150))
        photoImage = ImageTk.PhotoImage(resizedImage)

        imageLabel = ctk.CTkLabel(imageFrame, image=photoImage, text="")
        imageLabel.image = photoImage
        imageLabel.pack()

 