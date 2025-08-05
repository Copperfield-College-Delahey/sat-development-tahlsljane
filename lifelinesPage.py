# Code for the lifelines page

import customtkinter as ctk
import webbrowser

class LifelinesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None): 
        super().__init__(parent, fg_color="#EDF5FB") 

        # Page content ---------------------------------------------------------------------------------
        mainFrame = ctk.CTkFrame(self, fg_color="#E9F5FF") 
        mainFrame.pack(padx=20, pady=50)
        lifelinesTitle = ctk.CTkLabel(mainFrame, text="Lifelines", text_color="#0D2B50", font=("Georgia", 24, "bold", "underline", "italic"))
        lifelinesTitle.pack(expand=True, padx=10, pady=10)
        beyondBlue = ctk.CTkButton(mainFrame, text="• Beyond Blue - Mental health and wellbeing organisation for everyone", text_color="black", font=("Georgia", 16), fg_color="transparent", hover_color="#CCE3F5", command=lambda: webbrowser.open("https://www.beyondblue.org.au/"))
        beyondBlue.pack(padx=10, pady=10)
        kidsHelpline = ctk.CTkButton(mainFrame, text="• Kids Helpline - Mental health for people aged 5-25", text_color="black", font=("Georgia", 16), fg_color="transparent", hover_color="#CCE3F5", command=lambda: webbrowser.open("https://kidshelpline.com.au/"))
        kidsHelpline.pack(padx=10, pady=10) 
        headspace = ctk.CTkButton(mainFrame, text="• Headspace - Non profit mental health organisation for everyone", text_color="black", font=("Georgia", 16), fg_color="transparent", hover_color="#CCE3F5", command=lambda: webbrowser.open("https://headspace.org.au/"))
        headspace.pack(padx=10, pady=10)
        lifelineAustralia = ctk.CTkButton(mainFrame, text="• Lifeline Australia - Provides free, 24/7 telephone crisis support service in Australia", text_color="black", font=("Georgia", 16), fg_color="transparent", hover_color="#CCE3F5", command=lambda: webbrowser.open("https://www.lifeline.org.au/"))
        lifelineAustralia.pack(padx=10, pady=10)
