import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('使用ttk的套件')  # title ---------
        self.geometry('400x300')

        # ttk style instance
        style = ttk.Style(self)
        # style.configure('TLabel',font=('Helvetica', 11)) #修改現有的
        style.configure('Title.TLabel',font=('Helvetica', 20),background="lightblue", foreground="red") #自訂的style  --- Label style ----------
        message = ttk.Label(self,text='使用ttk的Label',style='Title.TLabel')  # ----- Label Text ----------
        print(message.winfo_class())
        message.pack()

def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()