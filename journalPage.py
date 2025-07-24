import customtkinter as ctk
from datetime import datetime

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        # This frame fills the entire JournalPage
        journalFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        journalFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Make JournalPage expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Make journalFrame expandable
        journalFrame.grid_rowconfigure(1, weight=1)  # Journal Entry (textbox)
        journalFrame.grid_columnconfigure(0, weight=1)

        # Label at the top
        journalLabel = ctk.CTkLabel(journalFrame, text="Journal Entry", font=("Helvetica", 20))
        journalLabel.grid(row=0, column=0, pady=(10, 5), sticky="n")

        # Expandable textbox
        self.journalEntry = ctk.CTkTextbox(journalFrame)
        self.journalEntry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Save button
        saveButton = ctk.CTkButton(journalFrame, text="💾 Save Entry", command=self.save_entry)
        saveButton.grid(row=2, column=0, pady=(5, 10))

    def save_entry(self):
        content = self.journalEntry.get("1.0", "end").strip()
        if content:
            with open("journal_entries.txt", "a") as file:
                file.write(f"{datetime.now()}:\n{content}\n\n")
            self.journalEntry.delete("1.0", "end")









