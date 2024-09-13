import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",   
        password="Ijse@1234",  
        database="danukatest"   
    )

 def add_user():
    name = entry_name.get()
    email = entry_email.get()
    if name and email:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User added successfully")
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        display_users()
    else:
        messagebox.showwarning("Input error", "Please fill in all fields")

