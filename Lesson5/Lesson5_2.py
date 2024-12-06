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
        ttk.Label(topFrame,text='請多選一',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
        self.selected_size = tk.StringVar()
        sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))
        label = ttk.Label(bottomFrame,text="what is your t-short size ?")
        label.pack(fill='x',padx=5,pady=5)

        # radio buttons
        for size in sizes:
            r = ttk.Radiobutton(
                root,
                text=size[0],
                value=size[1],
                variable=selected_size
            )
            r.pack(fill='x', padx=5, pady=5)

        # button
        button = ttk.Button(
            bottomFrame,
            text="Get Selected Size",
            command=self.show_selected_size)
        
        




        #==============end bottomFrame===============

 
        

        


        



def main():
    window = Window(theme="arc")
    #window.username.set('這裏放姓名')
    #window.password.set('這裏打password')
    window.mainloop()

if __name__ == '__main__':
    main()