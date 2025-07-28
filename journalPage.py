import customtkinter as ctk
from datetime import datetime

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")
        self.controller = controller

        journalFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        journalFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        journalFrame.grid_rowconfigure(1, weight=1) 
        journalFrame.grid_columnconfigure(0, weight=1)

        journalLabel = ctk.CTkLabel(journalFrame, text="Journal Entry:", text_color="black", font=("Georgia", 20, "bold", "italic", "underline"))
        journalLabel.grid(row=0, column=0, pady=(10, 5), sticky="n")

        self.journalEntry = ctk.CTkTextbox(journalFrame, fg_color="#CCE3F5", text_color="black", font=("Georgia", 15))
        self.journalEntry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        saveButton = ctk.CTkButton(journalFrame, text="💾 Save Entry", command=self.save_entry)
        saveButton.grid(row=2, column=0, pady=(5, 10))

    def save_entry(self):
        content = self.journalEntry.get("1.0", "end").strip()
        if content:
            with open("journal_entries.txt", "a") as file:
                file.write(f"{datetime.now()}:\n{content}\n\n")
            self.journalEntry.delete("1.0", "end")









