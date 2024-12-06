from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text='Hi there! It is nice to see you!', style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20, pady=20)
        #==============end topFrame===============
        
        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
        self.agreement = tk.StringVar()

        # Create the checkbutton here, outside of the function
        checkbutton = ttk.Checkbutton(bottomFrame,
                                      text='Thanks',
                                      variable=self.agreement,
                                      onvalue='It is wonderful to see you too!',
                                      offvalue='Thanks, but I have had a rough week.',
                                      command=self.agreement_changed)
    
        checkbutton.pack()

        bottomFrame.pack(expand=True, fill='x', padx=20, pady=(0, 20), ipadx=10, ipady=10)
        #==============end bottomFrame===============
    
    def agreement_changed(self):
        # This function is called when the checkbox state changes
        showinfo(title='Result', message=self.agreement.get())
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
