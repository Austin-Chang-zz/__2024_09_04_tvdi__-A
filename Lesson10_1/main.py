import datasource
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import view
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Cooling Fan Indicators')
        # ============== Style ===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel', font=('Helvetica', 20))
        # =========== Top Frame =============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame, text='Cooling Fan Indicators (Production Data)', style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20, pady=20)
        # =========== Bottom Frame ==========
        bottomFrame = ttk.Frame(self, padding=[10, 10, 10, 10])
        # =========== Selected Frame ==========
        self.selectedFrame = ttk.Frame(self, padding=[10, 10, 10, 10])
        # Refresh Button
        icon_button = view.ImageButton(self.selectedFrame, command=lambda: datasource.download_data())
        icon_button.pack()
        # Combobox to select Sales ID
        sales_ids = datasource.get_sales_ids()
        self.selected_sales = tk.StringVar()
        sales_cb = ttk.Combobox(
            self.selectedFrame, textvariable=self.selected_sales, values=sales_ids, state='readonly'
        )
        self.selected_sales.set('Select Sales ID')
        
        sales_cb.bind('<<ComboboxSelected>>', self.sales_selected) #************working*******************************************
        
        sales_cb.pack(anchor='n', pady=10)
        self.customerFrame = None
        self.selectedFrame.pack(side='left', fill='y')
        # =========== Right Frame ==========
        rightFrame = ttk.LabelFrame(bottomFrame, text="Customer Data", padding=[10, 10, 10, 10])
        # Treeview for displaying customer data
        columns = ('order_date', 'deliver_date', 'customer_id', 'order_id', 'yield_rate', 'thru_put', 'factor')
        self.tree = ttk.Treeview(rightFrame, columns=columns, show='headings')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        for col in columns:
            self.tree.heading(col, text=col.replace('_', ' ').title())
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(side='top')
        # Placeholder for chart
        self.plotFrame = ttk.Frame(rightFrame)
        self.canvas = None
        self.plotFrame.pack(side='top')
        rightFrame.pack(side='right')
        bottomFrame.pack()
        
    def sales_selected(self, event):
        selected_sales = self.selected_sales.get()
        customers = datasource.get_customers_by_sales_id(selected_sales)
        if self.customerFrame:
            self.customerFrame.destroy()
        self.customerFrame = view.CustomerFrame(master=self.selectedFrame, customers=customers)
        self.bind("<<Radio_Button_Selected>>", self.radio_button_click)
        self.customerFrame.pack()
    
    def radio_button_click(self, event):
        selected_customer = event.widget.selected_customer
        for children in self.tree.get_children():
            self.tree.delete(children)
        selected_data = datasource.get_selected_data(selected_customer)
        for record in selected_data:
            self.tree.insert("", "end", values=record)
        dataframe = datasource.get_plot_data(customer_id=selected_customer)
        axes = dataframe.plot()
        figure = axes.get_figure()
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(figure, master=self.plotFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(20, 10))

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            record = self.tree.item(selected_item)
            dialog = view.MyCustomDialog(parent=self, title=f'Order Details - {record["values"][2]}', record=record['values'])

def main():
    datasource.download_data()  # Initialize database with required data
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
