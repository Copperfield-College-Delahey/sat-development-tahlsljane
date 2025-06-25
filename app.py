import customtkinter as ctk

app = ctk.CTk()
app.title("my app")
app.geometry("400x150")
app.configure(fg_color='light blue')

# Layout grid
app.grid_columnconfigure((0), weight=1)
app.grid_rowconfigure((0), weight=2)
app.grid_rowconfigure((1), weight=4)
app.grid_rowconfigure((2), weight=1)
app.grid_rowconfigure((3), weight=1)

# Title
titleText = ctk.CTkLabel(app, text="StudHealth", text_color="black", font=("Georgia", 30))
titleText.grid(row=0, column=0, sticky="nw", padx=5, pady=5) 

# Frame
menuFrame = ctk.CTkFrame(app, border_width=1) 
menuFrame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5) 
menuFrame.grid_columnconfigure(0, weight=1) 
menuFrame.grid_rowconfigure(1, weight=1) 

#btnStrategies = ctk.CTkButton(menuFrame, ) 


app.mainloop()