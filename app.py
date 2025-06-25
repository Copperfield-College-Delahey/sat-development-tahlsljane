import customtkinter as ctk

app = ctk.CTk()
app.title("my app")
app.geometry("900x700")
app.configure(fg_color="light blue")

# Layout grid
app.grid_columnconfigure((0), weight=1)
app.grid_rowconfigure((0), weight=2)
app.grid_rowconfigure((1), weight=4)
app.grid_rowconfigure((2), weight=1)
app.grid_rowconfigure((3), weight=1)

# Title
titleText = ctk.CTkLabel(app, text="StudHealth", text_color="black", font=("Georgia", 30))
titleText.grid(row=0, column=0, sticky="we", padx=30, pady=30) 

# Frame
menuFrame = ctk.CTkFrame(app, border_width=1, fg_color="blue") 
menuFrame.grid(row=1, column=0, sticky="nsew", padx=0, pady=50) 
menuFrame.grid_rowconfigure(0, weight=1)
menuFrame.grid_columnconfigure(0, weight=1) 
menuFrame.grid_columnconfigure(1, weight=1) 
menuFrame.grid_columnconfigure(2, weight=1) 

btnStrategies = ctk.CTkButton(menuFrame, text="Strategies", text_color="black", fg_color="blue", font=("Georgia", 15))
btnStrategies.grid(row=0, column=0) 
btnMeditation = ctk.CTkButton(menuFrame, text="Meditation", text_color="black", fg_color="blue", font=("Georgia", 15))
btnMeditation.grid(row=0, column=1) 
btnJournalWriting = ctk.CTkButton(menuFrame, text="Journal Writing", text_color="black", fg_color="blue", font=("Georgia", 15))
btnJournalWriting.grid(row=0, column=2) 



app.mainloop()