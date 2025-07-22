# Code for journal page

import customtkinter as ctk
from datetime import datetime

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        journalFrame = ctk.CTkFrame(self, fg_color="#D9EDFF") 
        journalFrame.pack(padx=20, pady=50)

        ctk.CTkLabel(self, text="Journal Entry", font=("Helvetica", 20)).pack(pady=20)
        self.text_entry = ctk.CTkTextbox(self, width=500, height=200)
        self.text_entry.pack(pady=10)

        saveButton = ctk.CTkButton(self, text="💾 Save Entry", command=self.save_entry).pack(pady=5)

    def save_entry(self):
        content = self.text_entry.get("1.0", "end").strip()
        if content:
            with open("journal_entries.txt", "a") as file:
                file.write(f"{datetime.now()}\n{content}\n\n")
            self.text_entry.delete("1.0", "end")



