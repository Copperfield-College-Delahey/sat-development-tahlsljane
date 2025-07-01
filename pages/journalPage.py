import customtkinter as ctk

journal = ctk.CTk()
journal.title("Journal Writing")
journal.geometry("1000x700")
journal.configure(fg_color="#E9F5FF")

journal.grid_columnconfigure((0), weight=1)
journal.grid_rowconfigure((0), weight=1)
journal.grid_rowconfigure((1), weight=1)
journal.grid_rowconfigure((1), weight=1)




journal.mainloop()