import customtkinter as ctk
from PIL import Image, ImageTk

from homePage import HomePage
from journalPage import JournalPage
from strategiesPage import StrategiesPage
from lifelinesPage import LifelinesPage
from meditationPage import MeditationPage

# Setup ----------------------------------------------------------------------------
app = ctk.CTk()
app.title("my app")
app.geometry("1000x700")
app.configure(fg_color="#E9F5FF")

app.grid_columnconfigure((0), weight=1)
app.grid_rowconfigure((0), weight=0)
app.grid_rowconfigure((1), weight=0)
app.grid_rowconfigure((2), weight=0)
app.grid_rowconfigure((3), weight=1)

# Top frame ----------------------------------------------------------------------------
headingFrame = ctk.CTkFrame(app, fg_color="#E9F5FF", height=60)
headingFrame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
appTitle = ctk.CTkLabel(headingFrame, text="StudHealth", font=("Georgia", 32, "bold", "italic", "underline"), text_color="#0D2B50")
appTitle.place(relx=0.5, rely=0.5, anchor="center")

# Importing an image
originalImage = Image.open("strategiesImage.jpg")
imageWidth = 1600
imageHeight = 150

resizedImage = originalImage.resize((imageWidth, imageHeight))
photoImage = ImageTk.PhotoImage(resizedImage)

image_label = ctk.CTkLabel(app, image=photoImage, text="")
image_label.image = photoImage 
image_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Buttons frame ----------------------
buttonsFrame = ctk.CTkFrame(app, fg_color="#CCE3F5", height=60)
buttonsFrame.grid(row=2, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
buttonsFrame.grid_rowconfigure((0), weight=1)
buttonsFrame.grid_columnconfigure((0), weight=1)

homeButton = ctk.CTkButton(buttonsFrame, text="Home", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 15, "italic", "underline", "bold"))
homeButton.pack(side="left", expand=True, padx=10, pady=10)

journalButton = ctk.CTkButton(buttonsFrame, text="Journal", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 15, "italic", "underline", "bold"))
journalButton.pack(side="left", expand=True, padx=10, pady=10)

strategiesButton = ctk.CTkButton(buttonsFrame, text="Strategies", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 15, "italic", "underline", "bold"))
strategiesButton.pack(side="left", expand=True, padx=10, pady=10)

meditationButton = ctk.CTkButton(buttonsFrame, text="Meditation", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 15, "italic", "underline", "bold"))
meditationButton.pack(side="left", expand=True, padx=10, pady=10)

lifelinesButton = ctk.CTkButton(buttonsFrame, text="Lifelines", fg_color="transparent", text_color="black", hover_color="#D9EDFF", font=("Georgia", 15, "italic", "underline", "bold"))
lifelinesButton.pack(side="left", expand=True, padx=10, pady=10)

# Main frame ----------------------------------------------------------------------------
pageFrame = ctk.CTkFrame(app)
pageFrame.grid(row=3, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
pageFrame.grid_rowconfigure(0, weight=1)
pageFrame.grid_columnconfigure(0, weight=1)
# Load page classes
homePage = HomePage(pageFrame)
homePage.grid(row=0, column=0, sticky="nsew")
journalPage = JournalPage(pageFrame)
journalPage.grid(row=0, column=0, sticky="nsew")
strategiesPage = StrategiesPage(pageFrame)
strategiesPage.grid(row=0, column=0, sticky="nsew")
lifelinesPage = LifelinesPage(pageFrame)
lifelinesPage.grid(row=0, column=0, sticky="nsew")
meditationPage = MeditationPage(pageFrame)
meditationPage.grid(row=0, column=0, sticky="nsew")
# Dictionary of pages 
frames = {
    "HomePage": homePage, 
    "JournalPage": journalPage,
    "StrategiesPage": strategiesPage,
    "LifelinesPage": lifelinesPage,
    "MeditationPage": meditationPage,
} 
# Page-switching function 
def showFrame(pageName): 
    frames[pageName].tkraise() 
# Initially show Home Page 
showFrame("HomePage")
# Configure buttons in header to raise the relevant pages 
journalButton.configure(command=lambda: showFrame("JournalPage")) 
homeButton.configure(command=lambda: showFrame("HomePage")) 
strategiesButton.configure(command=lambda: showFrame("StrategiesPage"))
lifelinesButton.configure(command=lambda: showFrame("LifelinesPage"))
meditationButton.configure(command=lambda: showFrame("MeditationPage"))


app.mainloop()



