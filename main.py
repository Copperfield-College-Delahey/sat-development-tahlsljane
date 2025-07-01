import customtkinter as ctk
from PIL import Image, ImageTk
#from pages.menuPage import menuPage

app = ctk.CTk()
app.title("my app")
app.geometry("1000x700")
app.configure(fg_color="#E9F5FF")

# Layout grid
app.grid_columnconfigure((0), weight=1)
#app.grid_columnconfigure((1), weight=1)
app.grid_rowconfigure((0), weight=2)
#app.grid_rowconfigure((1), weight=4)
app.grid_rowconfigure((2), weight=1)
app.grid_rowconfigure((3), weight=1)

# Top frame & text
headingFrame = ctk.CTkFrame(app, fg_color="#E9F5FF", height=60)
headingFrame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

appTitle = ctk.CTkLabel(headingFrame, text="StudHealth", font=("Georgia", 32, "bold"), text_color="#0D2B50")
appTitle.place(relx=0.5, rely=0.5, anchor="center")

menuButton = ctk.CTkButton(headingFrame, text="≡", font=("Arial", 50), text_color="black", fg_color="transparent", hover_color="#D9EDFF")
menuButton.place(x=0, y=0)


# Menu frame & buttons
menuFrame = ctk.CTkFrame(app, fg_color="#D9EDFF", height=30)
menuFrame.grid(row=2, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

strategiesButton = ctk.CTkButton(menuFrame, text="Strategies", text_color="black", fg_color="transparent", font=("Georgia", 15, "italic", "underline", "bold"))
strategiesButton.pack(side="left", expand=True, padx=10, pady=10)

meditationButton = ctk.CTkButton(menuFrame, text="Meditation", text_color="black", fg_color="transparent", font=("Georgia", 15, "italic", "underline", "bold"))
meditationButton.pack(side="left", expand=True, padx=10, pady=10)

journalButton = ctk.CTkButton(menuFrame, text="Journal Writing", text_color="black", fg_color="transparent", font=("Georgia", 15, "italic", "underline", "bold"))
journalButton.pack(side="left", expand=True, padx=10, pady=10)

# Main content frame
mainFrame = ctk.CTkFrame(app, fg_color="#EDF5FB")
mainFrame.grid(row=3, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
mainFrame.grid_rowconfigure(0, weight=1)
mainFrame.grid_rowconfigure(1, weight=1)
mainFrame.grid_columnconfigure(0, weight=1)
#mainFrame.grid_columnconfigure(1, weight=1)

# About us text
about_text = (
    "Here at StudHealth, we care about the wellbeing of \nall students - high school and university.\n"
    "We believe that all students should have the ability \nto learn how to deal with any kind of stress they \nexperience, and that is our main goal."
)

aboutTitle = ctk.CTkLabel(mainFrame, text="About Us", text_color="#0D2B50", font=("Georgia", 24, "bold", "underline"))
aboutTitle.grid(row=0, column=0, sticky="w", padx=20, pady=20)

about_label = ctk.CTkLabel(mainFrame, text=about_text, font=("Georgia", 16), text_color="#000000", justify="left")
about_label.grid(row=1, column=0, sticky="w", padx=20, pady=10)


app.mainloop()