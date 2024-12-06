from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('世界最多人去旅遊的國家及地區')
        style = ttk.Style(self)     
           
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')  # top frame ---------------
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')

        btn1 = ttk.Button(topFrame,text="歐洲")
        btn1.pack(side='left',expand=True,fill='x',padx=10)

        btn2 = ttk.Button(topFrame,text="北美")
        btn2.pack(side='left',expand=True,fill='x')
        
        btn3 = ttk.Button(topFrame,text="亞洲")
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        
        bottomFrame = ttk.Frame(self,width=500,height=300,borderwidth=1,relief='sunken') # bottom frame ---------
        bottomFrame.pack(padx=5,pady=10)

        # create 3 columns in bottom frame
        for i in range(3):
            bottomFrame.columnconfigure(i,weight=1)
            bottomFrame.rowconfigure(0,weight=1)

        # Create a style object
        style = ttk.Style()

        # Define a new style for the buttons
        style.configure("Bold.TButton", font=("Helvetica", 40, "bold"), foreground="red", background="green")

        # Set a different background when the button is clicked or hovered over (optional)
        style.map("Bold.TButton", background=[("active", "lightblue"), ("pressed", "blue")])


        # List of the top 9 most popular travel destinations (replace these with the latest list if necessary)
        countries = [
            "法國", "西班牙", "土耳其", "中國", "義大利", 
            "美國", "墨西哥", "德國", "泰國"
        ]

        # Initialize a country counter
        country_counter = 0



        # create a frame in each column
        for col in range(3):
            column_frame = ttk.Frame(bottomFrame,relief='groove',borderwidth=2)
            column_frame.grid(row=0,column=col,sticky='nsew',padx=5)
            column_frame.columnconfigure(0,weight=1)
            if col == 0: # left column
                sizes = ["biggest",'small','small']
            elif col == 1: # middle column
                sizes = ["bigger","small","bigger"]
            else: # right column
                sizes = ["middle","middle","middle"]

            # add buttons in each column
            for row, size in enumerate(sizes):
                if country_counter < len(countries):
                    country_name = countries[country_counter]
                    btn = ttk.Button(column_frame, text=f"        {country_name}\n\n Botton: {size}")
                    if size == "biggest":
                        btn.grid(row=row, column=0, sticky="nsew", padx=5, pady=2, ipady=30)
                        column_frame.rowconfigure(row, weight=3)
                    elif size == "bigger":
                        btn.grid(row=row, column=0, sticky="nsew", padx=5, pady=2, ipady=20)
                        column_frame.rowconfigure(row, weight=2)
                    elif size == "middle":
                        btn.grid(row=row, column=0, sticky="nsew", padx=5, pady=2, ipady=5)
                        column_frame.rowconfigure(row, weight=1)
                    else:
                        btn.grid(row=row, column=0, sticky="nsew", padx=5, pady=1, ipady=5)
                        column_frame.rowconfigure(row, weight=1)

                    # Increment the country counter after placing each button
                    country_counter += 1
            



def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()


