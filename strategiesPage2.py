import customtkinter as ctk
from PIL import Image, ImageTk

strategies = ctk.CTk()
strategies.title("Strategies Questions")
strategies.geometry("1000x700")
strategies.configure(fg_color="#E9F5FF")

strategies.grid_columnconfigure((0), weight=1)
strategies.grid_columnconfigure((1), weight=1)
strategies.grid_rowconfigure((0), weight=1)
strategies.grid_rowconfigure((1), weight=1)
strategies.grid_rowconfigure((2), weight=1)
strategies.grid_rowconfigure((3), weight=1)
strategies.grid_rowconfigure((4), weight=1)

# Functions for buttons
#def happyClicked():
 #   happyButton.configure(text="• Happy ᥫ᭡")
#def sadClicked():
 #   sadButton.configure(text="• Sad ˙◠˙")
#def frustratedClicked():
 #   frustratedButton.configure(text="• Frustrated ☔︎")
#def angryClicked():
 #   angryButton.configure(text="• Angry 𓇢𓆸")
#def stressedClicked():
 #   stressedButton.configure(text="• Stressed ☹")

#def processAnswer():
 #   if happyButton:
  #      subtitle.configure(text="You have been feeling...")
   #     strategiesTitle.configure(text="Happy!")

#def changeAnswer():
 #   if changeButton():
  #      happyButton.configure(text="◦ Happy ᥫ᭡")
   #     sadButton.configure(text="◦ Sad ˙◠˙")
    #    frustratedButton.configure(text="◦ Frustrated ☔︎")
     #   angryButton.configure(text="◦ Angry 𓇢𓆸")
      #  stressedButton.configure(text="◦ Stressed ☹")


# Title & frame
titleFrame = ctk.CTkFrame(strategies, fg_color="#EDF5FB", height=30)
titleFrame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

subtitle = ctk.CTkLabel(titleFrame, text="", text_color="#0D2B50", font=("Georgia", 15, "italic"))
subtitle.place(relx=0.48, rely=0.2)

strategiesTitle = ctk.CTkLabel(titleFrame, text="Strategies", text_color="#0D2B50", font=("Georgia", 32, "bold", "underline", "italic"))
strategiesTitle.place(relx=0.5, rely=0.7, anchor="center")

menuButton = ctk.CTkButton(titleFrame, text="≡", font=("Arial", 50), text_color="black", fg_color="transparent", hover_color="#D9EDFF")
menuButton.place(x=0, y=0)

# Ending buttons
submitButton = ctk.CTkButton(strategies, text="Submit", fg_color="#0D2B50", text_color="white", font=("Georgia", 24, "italic", "underline")) #command=processAnswer)
submitButton.grid(row=4, column=0)

changeButton = ctk.CTkButton(strategies, text="Change answer", fg_color="#0D2B50", text_color="white", font=("Georgia", 24, "italic", "underline")) #command=changeAnswer)
changeButton.grid(row=4, column=1)

strategies.mainloop()