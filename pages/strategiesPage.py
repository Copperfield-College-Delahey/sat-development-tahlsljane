import customtkinter as ctk
from PIL import Image, ImageTk

strategies = ctk.CTk()
strategies.title("Strategies Questions")
strategies.geometry("1000x700")
strategies.configure(fg_color="#E9F5FF")

strategies.grid_columnconfigure((0), weight=1)
strategies.grid_rowconfigure((0), weight=1)
strategies.grid_rowconfigure((1), weight=1)
strategies.grid_rowconfigure((2), weight=1)
strategies.grid_rowconfigure((3), weight=1)
strategies.grid_rowconfigure((4), weight=1)

# Title & frame
titleFrame = ctk.CTkFrame(strategies, fg_color="#EDF5FB", height=30)
titleFrame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

strategiestitle = ctk.CTkLabel(titleFrame, text="Strategies", text_color="#0D2B50", font=("Georgia", 32, "bold", "underline", "italic"))
strategiestitle.place(relx=0.5, rely=0.5, anchor="center")

menuButton = ctk.CTkButton(titleFrame, text="≡", font=("Arial", 50), text_color="black", fg_color="transparent", hover_color="#D9EDFF")
menuButton.place(x=0, y=0)

# Question & frame
questionFrame = ctk.CTkFrame(strategies, fg_color="#D9EDFF", height=30)
questionFrame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

questionText = ctk.CTkLabel(questionFrame, text="How have you been feeling recently?", font=("Georgia", 26, "bold", "italic"), text_color="#0D2B50", fg_color="#D9EDFF")
questionText.place(relx=0.5, rely=0.5, anchor="center")

# Answers & frame
answersFrame = ctk.CTkFrame(strategies, fg_color="#EDF5FB", height=60)
answersFrame.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

answersText = ctk.CTkLabel(answersFrame, text_color="black", text="○ Happy \n○ Sad \n○ Frustrated \n○ Angry \n○ Stressed", font=("Georgia", 17))
answersText.place(relx=0.5, rely=0.5, anchor="center")

# Submit button
submitButton = ctk.CTkButton(strategies, text="Submit", fg_color="#0D2B50", text_color="white", font=("Georgia", 24, "italic", "underline"))
submitButton.grid(row=4, column=0)

strategies.mainloop()