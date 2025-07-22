import customtkinter as ctk

#aboutText = (
   #"Here at StudHealth, we care about the wellbeing of \nall students - high school and university.\n"
   #"We believe that all students should have the ability \nto learn how to deal with any kind of stress they \nexperience, and that is our main goal."
#)


class HomePage(ctk.CTkFrame): 
    def __init__(self, parent, controller=None): 
        super().__init__(parent) 
        # Page content
        mainFrame = ctk.CTkFrame(self, fg_color="#D9EDFF") 
        mainFrame.pack(padx=20, pady=50)
        aboutTitle = ctk.CTkLabel(mainFrame, text="About Us", text_color="#0D2B50", font=("Georgia", 24, "bold", "underline", "italic"))
        aboutTitle.pack(pady=10, padx=10)
        #aboutLabel = ctk.CTkLabel(mainFrame, text=aboutText, font=("Georgia", 16), text_color="#000000", justify="left")
        #aboutLabel.pack(pady=10, padx=10)
 