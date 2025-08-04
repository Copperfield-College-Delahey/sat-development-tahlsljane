# Code for the journal page

import customtkinter as ctk
from datetime import datetime

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")
        self.controller = controller

        # Journal page grid -----------------------------------------------------------------
        journalFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        journalFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        journalFrame.grid_rowconfigure(1, weight=1) 
        journalFrame.grid_columnconfigure(0, weight=1)
        journalFrame.grid_columnconfigure(1, weight=1)

        # Journal textbox -----------------------------------------------------------------
        journalLabel = ctk.CTkLabel(journalFrame, text="Journal Entry:", text_color="black", font=("Georgia", 20, "bold", "italic", "underline"))
        journalLabel.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="n")

        self.journalEntry = ctk.CTkTextbox(journalFrame, fg_color="#CCE3F5", text_color="black", font=("Georgia", 15))
        self.journalEntry.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Buttons frame -----------------------------------------------------------------
        buttonsFrame = ctk.CTkFrame(journalFrame, fg_color="#EDF5FB", height=60)
        buttonsFrame.grid(row=2, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
        buttonsFrame.grid_rowconfigure((0), weight=1)
        buttonsFrame.grid_columnconfigure((0), weight=1)
        buttonsFrame.grid_columnconfigure((1), weight=1)

        saveButton = ctk.CTkButton(buttonsFrame, text="Save Entry", font=("Georgia", 18, "bold", "italic", "underline"), command=self.save_entry)
        saveButton.grid(row=0, column=0)

        reloadButton = ctk.CTkButton(buttonsFrame, text="Reload Entry", font=("Georgia", 18, "bold", "italic", "underline"), command=self.reload_entry)
        reloadButton.grid(row=0, column=1)

    # Button functions -----------------------------------------------------------------
    
    # Saving the user's journal entry
    def save_entry(self):
        content = self.journalEntry.get("1.0", "end").strip()
        if content:
            with open("journal_entries.txt", "a") as file:
                file.write(f"{datetime.now()}:\n{content}\n\n")
            self.journalEntry.delete("1.0", "end")

    # Reloading the user's most recently saved entry
    def reload_entry(self):
        try:
            with open("journal_entries.txt", "r") as file:
                content = file.read().strip()
                if not content:
                    return
                
                entries = content.split("\n\n")
                latest_entry = entries[-1] 

                if ":" in latest_entry:
                    latest_entry_lines = latest_entry.split("\n")
                    entry_text_only = "\n".join(latest_entry_lines[1:])
                else:
                    entry_text_only = latest_entry

                self.journalEntry.delete("1.0", "end")
                self.journalEntry.insert("1.0", entry_text_only)
        except FileNotFoundError:
            print("No journal entries found.")









