# Code for the lifelines page

import customtkinter as ctk

lifelinesText = (
    "• Beyond Blue - Mental health and wellbeing organisation for everyone \n"
    "• Kids Helpline - Mental health for people aged 5-25 \n"
    "• Headspace - Non profit mental health organisation for everyone \n"
    "• Lifeline Australia - Provides free, 24/7 telephone crisis support service in Australia"
)

class LifelinesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None): 
        super().__init__(parent, fg_color="#EDF5FB") 

        # Page content ---------------------------------------------------------------------------------
        mainFrame = ctk.CTkFrame(self, fg_color="#E9F5FF") 
        mainFrame.pack(padx=20, pady=50)
        lifelinesTitle = ctk.CTkLabel(mainFrame, text="Lifelines", text_color="#0D2B50", font=("Georgia", 24, "bold", "underline", "italic"))
        lifelinesTitle.pack(expand=True, padx=10, pady=10)
        lifelinesLabel = ctk.CTkLabel(mainFrame, text=lifelinesText, font=("Georgia", 16), text_color="#000000", justify="left")
        lifelinesLabel.pack(pady=10, padx=10)
