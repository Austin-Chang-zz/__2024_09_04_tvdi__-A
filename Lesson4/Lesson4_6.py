
from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Use tk package")
        style =ttk.Style(self)
        topFrame =ttk.Frame(self,borderwidth=1,relief='groove',)

        btn1 =ttk.Button(topFrame,text='Button1')
        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 =ttk.Button(topFrame,text='Button2')
        btn2.pack(side='left',expand=True,fill='x',padx=10)

        btn3 =ttk.Button(topFrame,text='Button3')
        btn3.pack(side='left',expand=True,fill='x',padx=10)

        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')
        bottomFrame =ttk.Frame(self,width=500,height=300,borderwidth=1,relief='groove')
        bottomFrame.pack(padx=10,pady=10)



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()