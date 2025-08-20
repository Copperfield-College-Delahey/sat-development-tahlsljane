# Code for the strategies page

import customtkinter as ctk

# Strategies for feelings -------------------------------------------------------------------------

strategies_dict = {
    "happy": (
        "I'm glad you feel that way! Here's how you can stay happy: \n"
        "• Go for a walk once a day \n"
        "• Stay hydrated \n"
        "• Sleep at a reasonable time (if possible) \n"
        "• Do something fun everyday \n"
        "• Take photos of things that make you smile and revisit them \n"
    ),
    "sad": (
        "I'm sorry you feel that way. Here's some ways that you can get back on track: \n"
        "• Exercise daily \n"
        "• Participate in meditation \n"
        "• Take a brief break from your screen every 30 minutes \n"
        "• Listen to your favourite songs \n"
        "• Watch your favourite movie/tv show \n"
        "• Limit your social media use \n"
        "• Take a nap \n"
        "• Eat something nourishing!"
    ),
    "angry": (
        "It's okay to feel angry. Here are some ways that you can calm yourself: \n"
        "• Practice deep breathing during those moments \n"
        "• Change the scenery in which you're surrounded by \n"
        "• Identify solutions that could be used to fix this problem \n"
        "• Write all your feelings in a letter then destroy it \n"
        "• Go for a brisk walk or run \n"
        "• Clean something small \n"
        "• Use a stress ball or fidget tool"
    ),
    "frustrated": (
        "That can be annoying. Here are some strategies you can use to redeem yourself: \n"
        "• Express yourself by talking to someone \n"
        "• Challenge your negative thoughts \n"
        "• Try and prioritize sleep \n"
        "• Do something repetitive \n"
        "• Safely yell it out \n"
        "• Draw it out \n"
        "• Stretch out your body"
    ),
    "stressed": (
        "Stress is very common among young people. Here are some ways you can help yourself: \n"
        "• Create a schedule; lines out what needs to be done and when \n"
        "• Briefly engage in enjoyable activities \n"
        "• Maintain a healthy diet \n"
        "• Call or text a friend \n"
        "• Limit caffeine and sugar consumption \n"
        "• Spend some time outside \n"
        "• Set realistic expectations \n"
        "• Chew gum \n"
        "• Splash cold water on your face"
    )
}

# Strategies page content -------------------------------------------------------------------------

class StrategiesPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")

        # Search mood function
        def searchMood():
            mood = searchEntry.get().lower().strip()
            if mood:
                if mood in strategies_dict:
                    strategiesText.configure(text=strategies_dict[mood])
                else:
                 strategiesText.configure(
                     text="Sorry, I don't have strategies for that feeling yet. Try: happy, sad, angry, frustrated, stressed."
                )
            else:
                strategiesText.configure(
                    text="Please input a feeling."
                )
        
        # Main content
        strategiesFrame = ctk.CTkFrame(self, fg_color="#EDF5FB") 
        strategiesFrame.pack(padx=20, pady=50)

        questionText = ctk.CTkLabel(strategiesFrame, text="How are you feeling today?", text_color="black", font=("Georgia", 23, "italic", "underline", "bold"))
        questionText.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        searchEntry = ctk.CTkEntry(strategiesFrame, text_color="white", width=300, placeholder_text="Type your feeling.. (eg. Happy, Sad)", font=("Georgia", 15))
        searchEntry.grid(row=1, column=0, padx=5, pady=5)
        searchEntry.bind("<Return>", lambda event: searchMood())

        searchButton = ctk.CTkButton(strategiesFrame, text="Search", text_color="#0D2B50", fg_color="#CCE3F5", hover_color="#AACBE4", font=("Georgia", 15, "bold", "italic"), command=searchMood)
        searchButton.grid(row=1, column=1, padx=5, pady=5)

        strategiesText = ctk.CTkLabel(strategiesFrame, text="", text_color="black", font=("Georgia", 15), justify="left", wraplength=600)
        strategiesText.grid(row=2, column=0, columnspan=2, pady=20)

        

