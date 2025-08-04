# Code for the strategies page

import customtkinter as ctk

happyText = (
    "I'm glad you feel that way! Here's how you can stay happy: \n"
    "- Go for a walk once a day \n"
    "- Stay hydrated \n"
    "- Sleep at a reasonable time (if possible)"
)

sadText = (
    "I'm sorry you feel that way. Here's some ways that you can get back on track: \n"
    "- Exercise daily \n"
    "- Participate in meditation \n"
    "- Take a brief break from your screen every 30 minutes \n"
)

angryText = (
    "It's okay to feel angry. Here are some ways that you can calm yourself: \n"
    "- Practice deep breathing during those moments \n"
    "- Change the scenery in which you're surrounded by \n"
    "- Identify solutions that could be used to fix this problem \n"
)


class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        def Happy():
            if happyButton:
                strategiesText.configure(text=happyText)
        def Sad():
            if sadButton:
                strategiesText.configure(text=sadText)
        def Angry():
            if angryButton:
                strategiesText.configure(text=angryText)

        # Page content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#EDF5FB") 
        strategiesFrame.pack(padx=20, pady=50)

        happyButton = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Happy)
        happyButton.grid(row=0, column=0)

        sadButton = ctk.CTkButton(strategiesFrame, text="Sad", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Sad)
        sadButton.grid(row=2, column=0)

        angryButton = ctk.CTkButton(strategiesFrame, text="Angry", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Angry)
        angryButton.grid(row=4, column=0)

        frustratedButton = ctk.CTkButton(strategiesFrame, text="Frustrated", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5")
        frustratedButton.grid(row=6, column=0)
        
        stressedButton = ctk.CTkButton(strategiesFrame, text="Stressed", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5")
        stressedButton.grid(row=8, column=0)

        strategiesText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15), justify="left")
        strategiesText.grid(row=10, column=0)

