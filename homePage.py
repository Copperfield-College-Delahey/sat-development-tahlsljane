# Code for the home page

import customtkinter as ctk
from PIL import Image, ImageTk

# Text describing what StudHealth is
aboutText = (
   "Here at StudHealth, we care about the wellbeing of \nall students - high school and university.\n"
   "We believe that all students should have the ability \nto learn how to deal with any kind of stress they \nexperience, and that is our main goal."
)


class HomePage(ctk.CTkFrame): 
    def __init__(self, parent, controller=None): 
        super().__init__(parent, fg_color="#EDF5FB") 

        # Page content -----------------------------------------------------------------------------
        mainFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        mainFrame.pack(padx=20, pady=50, expand=True)
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(1, weight=1)

        textFrame = ctk.CTkFrame(mainFrame, fg_color="#EDF5FB")
        textFrame.grid(row=0, column=0, sticky="nsew", padx=10)

        aboutTitle = ctk.CTkLabel(textFrame, text="About Us", text_color="#0D2B50", font=("Georgia", 24, "bold", "underline", "italic"))
        aboutTitle.pack(pady=(0, 10), anchor="w")
        aboutLabel = ctk.CTkLabel(textFrame, text=aboutText, font=("Georgia", 16), text_color="black", justify="left")
        aboutLabel.pack(anchor="w")

        imageFrame = ctk.CTkFrame(mainFrame, fg_color="#EDF5FB")
        imageFrame.grid(row=0, column=1, sticky="nsew", padx=10)

        # Load and resize image
        originalImage = Image.open("studyingImage.jpg")  # Replace with your image file
        resizedImage = originalImage.resize((250, 150))  # Adjust size as needed
        photoImage = ImageTk.PhotoImage(resizedImage)

        imageLabel = ctk.CTkLabel(imageFrame, image=photoImage, text="")
        imageLabel.image = photoImage  # Prevent garbage collection
        imageLabel.pack()

 