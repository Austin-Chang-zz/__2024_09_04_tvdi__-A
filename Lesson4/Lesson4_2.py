import tkinter as tk

def main():
    root = tk.Tk()
    print(type(root))
    root.title('MY window')
    root.geometry("800x300")
    message = tk.Label(root,text='Hello! this is my window')
    message.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
