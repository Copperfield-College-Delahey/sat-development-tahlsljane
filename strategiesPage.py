# Code for the strategies page

import customtkinter as ctk

# Text for different moods ---------------------------------------------------------------------
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

frustratedText = (
    "That can be annoying. Here are some strategies you can use to redeem yourself: \n"
    "- Express yourself by talking to someone \n"
    "- Challenge your negative thoughts \n"
    "- Try and prioritize sleep \n"
)

stressedText = (
    "Stress is very common among young people. Here are some ways you can help yourself: \n"
    "- Create a schedule; lines out what needs to be done and when \n"
    "- Briefly engage in enjoyable activities \n"
    "- Maintain a healthy diet \n"
)

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        # Button functions ---------------------------------------------------------------
        def Happy():
            if happyButton:
                strategiesText.configure(text=happyText)
        def Sad():
            if sadButton:
                strategiesText.configure(text=sadText)
        def Angry():
            if angryButton:
                strategiesText.configure(text=angryText)
        def Frustrated():
            if frustratedButton:
                strategiesText.configure(text=frustratedText)
        def Stressed():
            if stressedButton:
                strategiesText.configure(text=stressedText)

        # Page content ------------------------------------------------------------------------------
        strategiesFrame = ctk.CTkFrame(self, fg_color="#EDF5FB") 
        strategiesFrame.pack(padx=20, pady=50)

        questionText = ctk.CTkLabel(strategiesFrame, text="How are you feeling today?", text_color="black", font=("Georgia", 23, "italic", "underline", "bold"))
        questionText.grid(row=0, column=0)
        filler = ctk.CTkLabel(strategiesFrame, text="")
        filler.grid(row=1, column=0)

        happyButton = ctk.CTkButton(strategiesFrame, text="Happy", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Happy)
        happyButton.grid(row=2, column=0)
        filler1 = ctk.CTkLabel(strategiesFrame, text="")
        filler1.grid(row=3, column=0)

        sadButton = ctk.CTkButton(strategiesFrame, text="Sad", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Sad)
        sadButton.grid(row=4, column=0)
        filler2 = ctk.CTkLabel(strategiesFrame, text="")
        filler2.grid(row=5, column=0)

        angryButton = ctk.CTkButton(strategiesFrame, text="Angry", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Angry)
        angryButton.grid(row=6, column=0)
        filler3 = ctk.CTkLabel(strategiesFrame, text="")
        filler3.grid(row=7, column=0)

        frustratedButton = ctk.CTkButton(strategiesFrame, text="Frustrated", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Frustrated)
        frustratedButton.grid(row=8, column=0)
        filler4 = ctk.CTkLabel(strategiesFrame, text="")
        filler4.grid(row=9, column=0)
        
        stressedButton = ctk.CTkButton(strategiesFrame, text="Stressed", text_color="black", font=("Georgia", 20, "italic", "underline"), hover_color="#CCE3F5", command=Stressed)
        stressedButton.grid(row=10, column=0)
        filler5 = ctk.CTkLabel(strategiesFrame, text="")
        filler5.grid(row=11, column=0)

        # Text to show strategies based on the mood selected 
        strategiesText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15), justify="center")
        strategiesText.grid(row=12, column=0)

