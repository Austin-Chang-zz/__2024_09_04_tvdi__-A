import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Use tk package")
        self.geometry('400x300')
        style = ttk.Style(self)

        # Define a custom style for buttons
        style.configure('Main.TButton', font=('Arial', 15))  # Fixed style name

        # Create a button with the correct style name
        btn1 = ttk.Button(self, text="Bottom Demo", style="Main.TButton")  # Fixed style name
        btn1.pack(padx=10, pady=10, ipadx=10, ipady=10)

def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()