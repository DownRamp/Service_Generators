#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import customtkinter
import json

starter = {
    "swagger": "2.0",
    "info": {
        "description": "FILL",
        "version": "1.0.0",
        "title": "FILL",
        "contact": {
            "email": "FILL"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "schemes": ["http"],
    "host": "localhost:5472",
    "basePath": "/FILL"
}

class Window():
    def __init__(self, main):
        width_val = 200
        self.main = main

        self.win = customtkinter.CTkFrame(master=self.main, corner_radius=15)
        self.win.pack(fill=BOTH, expand =1)
        self.canvas = Canvas(self.win)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scroll = ttk.Scrollbar(self.win, orient=VERTICAL, command = self.canvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        self.frm = customtkinter.CTkFrame(master=self.canvas, corner_radius=15)
        self.canvas.create_window((0,0), window = self.frm, anchor="nw")
        self.label = customtkinter.CTkLabel(master=self.frm, justify=LEFT, text="Enter chapter information")
        self.label.pack(padx=20, pady=20)
        self.entry_des = customtkinter.CTkEntry(master=self.frm,
                                    height = 120,
                                    width=width_val,
                                    placeholder_text="Enter Description")
        self.entry_des.pack(pady=20, padx=20)
        self.entry_title = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Title")
        self.entry_title.pack(pady=20, padx=20)
        self.entry_email = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Email")
        self.entry_email.pack(pady=20, padx=20)
        self.entry_basePath = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter base path")
        self.entry_basePath.pack(pady=20, padx=20)

        self.add_path = customtkinter.CTkButton(master=self.frm, text="Add paths", command=lambda: enter_number_paths())
        self.add_path.pack(padx=20, pady=20)

        self.add_def = customtkinter.CTkButton(master=self.frm, text="Add defintions", command=lambda: enter_number_definitions())
        self.add_def.pack(padx=20, pady=20)

        self.button =customtkinter.CTkButton(master=self.frm, text="Submit", command=lambda: enter_values(
            self.entry_des.get(), self.entry_title.get(), self.entry_email.get(), self.entry_basePath.get()
        ))

        self.button.pack(padx=20, pady=20)

    def enter_number_paths():
        pass

    def create_paths():
        pass

    def enter_number_definitions():
        pass

    def create_definitions():
        pass

def enter_values(description, title, email, basePath):
    starter["info"]["description"] = description
    starter["info"]["title"] = title
    starter["info"]["contact"]["email"] = email
    starter["basePath"] = basePath
    create_file()
    return starter

def create_file():
    with open("swagger.json", "w") as outfile:
        json.dump(starter, outfile)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    root = customtkinter.CTk()
    root.title("Chapter maker")
    root.geometry("300x800")
    Window(root)
    root.mainloop()

