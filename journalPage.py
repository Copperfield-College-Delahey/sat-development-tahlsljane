# Code for journal page

import customtkinter as ctk
from homePage import HomePage
from datetime import datetime

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Journal Entry", font=("Helvetica", 20)).pack(pady=20)
        self.text_entry = ctk.CTkTextbox(self, width=500, height=200)
        self.text_entry.pack(pady=10)

        ctk.CTkButton(self, text="💾 Save Entry", command=self.save_entry).pack(pady=5)
        ctk.CTkButton(self, text="⬅️ Back to Home", command=lambda: controller.show_frame(HomePage)).pack(pady=10)

    def save_entry(self):
        content = self.text_entry.get("1.0", "end").strip()
        if content:
            with open("journal_entries.txt", "a") as file:
                file.write(f"{datetime.now()}\n{content}\n\n")
            self.text_entry.delete("1.0", "end")
