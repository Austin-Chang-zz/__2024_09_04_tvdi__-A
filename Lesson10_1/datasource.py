import sqlite3
import os
from pandas import DataFrame
import pandas as pd

def get_sales_ids() -> list[str]:
    conn = sqlite3.connect("sales_orders1.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT sales_id FROM sales_orders1")
        sales_ids = [row[0] for row in cursor.fetchall()]
    return sales_ids

def get_customers_by_sales_id(sales_id: str) -> list[str]:
    conn = sqlite3.connect("sales_orders1.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT customer_id FROM sales_orders1 WHERE sales_id = ?", (sales_id,))
        customers = [row[0] for row in cursor.fetchall()]
    return customers

def get_selected_data(customer_id: str) -> list[list]:
    conn = sqlite3.connect("sales_orders1.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT order_date, deliver_date, customer_id, order_id, yield_rate, thru_put, factor
            FROM sales_orders1 WHERE customer_id = ?
            ORDER BY order_date DESC
        """, (customer_id,))
        return [list(row) for row in cursor.fetchall()]

def get_plot_data(customer_id: str) -> DataFrame:
    conn = sqlite3.connect("sales_orders1.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT order_date, yield_rate, thru_put FROM sales_orders1 WHERE customer_id = ?
        """, (customer_id,))
        data = [{'order_date': row[0], 'yield_rate': row[1], 'thru_put': row[2]} for row in cursor.fetchall()]
    df = pd.DataFrame(data)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df.set_index('order_date')

def download_data():
    # Placeholder for downloading and initializing data
    print("Downloading and populating sales_orders1.db...")
