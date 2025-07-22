import customtkinter as ctk
from homePage import HomePage
from menuPage import MenuPage 

# Setup ----------------------------------------------------------------------------
app = ctk.CTk()
app.title("my app")
app.geometry("1000x700")
app.configure(fg_color="#E9F5FF")

app.grid_columnconfigure((0), weight=1)
#app.grid_columnconfigure((1), weight=1)
app.grid_rowconfigure((0), weight=2)
#app.grid_rowconfigure((1), weight=4)
app.grid_rowconfigure((2), weight=1)
app.grid_rowconfigure((3), weight=1)

# Top frame ----------------------------------------------------------------------------
headingFrame = ctk.CTkFrame(app, fg_color="#E9F5FF", height=60)
headingFrame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
appTitle = ctk.CTkLabel(headingFrame, text="StudHealth", font=("Georgia", 32, "bold", "italic", "underline"), text_color="#0D2B50")
appTitle.place(relx=0.5, rely=0.5, anchor="center")
menuButton = ctk.CTkButton(headingFrame, text="≡", font=("Arial", 50), text_color="black", fg_color="transparent", hover_color="#D9EDFF")
menuButton.place(x=0, y=0)

# Main frame ----------------------------------------------------------------------------
pageFrame = ctk.CTkFrame(app, fg_color="#EDF5FB")
pageFrame.grid(row=3, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
pageFrame.grid_rowconfigure(0, weight=1)
pageFrame.grid_columnconfigure(0, weight=1)
# Load page classes
homePage = HomePage(pageFrame) 
menuPage = MenuPage(pageFrame) 
# Dictionary of pages 
frames = {
    "HomePage": homePage, 
    "MenuPage": menuPage
} 
# Page-switching function 
def showFrame(pageName): 
    frames[pageName].tkraise() 
# Initially show Home Page 
showFrame("HomePage")
homePage.configure(fg_color="#D9EDFF")
menuPage.configure(fg_color="#D9EDFF")
# Configure buttons in header to raise the relevant pages 
menuButton.configure(command=lambda: showFrame("MenuPage")) 


app.mainloop()



