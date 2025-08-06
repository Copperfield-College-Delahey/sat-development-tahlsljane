# Code for the journal page

import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import os

journalFile = "journals"
if not os.path.exists(journalFile):
    os.makedirs(journalFile)

class JournalPage(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, fg_color="#EDF5FB")
        self.controller = controller

        # Journal page grid -----------------------------------------------------------------
        journalFrame = ctk.CTkFrame(self, fg_color="#EDF5FB")
        journalFrame.pack(pady=40)

        # Journal textbox -----------------------------------------------------------------
        journalLabel = ctk.CTkLabel(journalFrame, text="Journal Entry:", text_color="black", font=("Georgia", 20, "bold", "italic", "underline"))
        journalLabel.pack(pady=(10, 5))

        self.journalEntry = ctk.CTkTextbox(journalFrame, fg_color="#CCE3F5", text_color="black", font=("Georgia", 15), width=700, height=300)
        self.journalEntry.pack(padx=10, pady=10)

        self.dateEntryLabel = ctk.CTkLabel(journalFrame, text="Enter Date (DD-MM-YYYY):", text_color="black", font=("Georgia", 15))
        self.dateEntryLabel.pack(pady=(10, 5))

        self.dateEntry = ctk.CTkEntry(journalFrame, width=200, font=("Georgia", 15))
        self.dateEntry.pack(pady=5)

        # Buttons frame -----------------------------------------------------------------
        buttonsFrame = ctk.CTkFrame(journalFrame, fg_color="#EDF5FB", height=60)
        buttonsFrame.pack(pady=(10, 0))

        saveButton = ctk.CTkButton(buttonsFrame, text="Save Entry", font=("Georgia", 18, "bold", "italic", "underline"), command=self.saveEntry)
        saveButton.pack(side="left", padx=20)

        reloadButton = ctk.CTkButton(buttonsFrame, text="Reload Entry", font=("Georgia", 18, "bold", "italic", "underline"), command=self.reloadEntry)
        reloadButton.pack(side="left", padx=20)


    # Button functions -----------------------------------------------------------------
    
    # Saving each journal
    def saveEntry(self):
        content = self.journalEntry.get("1.0", "end").strip()
        if content:
            currentDate = datetime.now().strftime("%d-%m-%Y")
            filePath = os.path.join(journalFile, f"{currentDate}.txt")
            with open(filePath, "w") as file:
                file.write(f"{content}\n")
            self.journalEntry.delete("1.0", "end")

    # Reloading a journal from a specific date
    def reloadEntry(self):
        dateInput = self.dateEntry.get().strip()
        if dateInput:
            try:
                filePath = os.path.join(journalFile, f"{dateInput}.txt")
                with open(filePath, "r") as file:
                    entryContent = file.read().strip()
                    self.journalEntry.delete("1.0", "end")
                    self.journalEntry.insert("1.0", entryContent)
            except FileNotFoundError:
                self.journalEntry.delete("1.0", "end")
                messagebox.showerror("ERROR!", "No journal entry found for this date.")
        else:
            self.journalEntry.delete("1.0", "end")
            messagebox.showerror("ERROR!", "Please enter a valid date.")  



