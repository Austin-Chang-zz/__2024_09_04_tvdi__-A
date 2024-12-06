
from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Use tk package")
        self.geometry('400x300')
        style = ttk.Style(self)

        # Define a custom style for buttons
        style.configure('Main.TButton', font=('Arial', 15))  # Fixed style name

        # Create a button with the correct style name
        btn1 = ttk.Button(self, text="Bottom Demo", style="Main.TButton")  # Fixed style name
        btn1.pack(padx=10, pady=10, ipadx=10, ipady=10)

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()