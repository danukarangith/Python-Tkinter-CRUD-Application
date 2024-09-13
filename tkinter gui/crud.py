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

        # Function to read and display all users
def display_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    user_list.delete(0, END)
    for row in rows:
        user_list.insert(END, f"{row[0]} - {row[1]} - {row[2]}")
    conn.close

    def update_user():
    selected_user = user_list.curselection()
    if selected_user:
        user_id = user_list.get(selected_user).split(" - ")[0]
        name = entry_name.get()
        email = entry_email.get()
        if name and email:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User updated successfully")
            display_users()
        else:
            messagebox.showwarning("Input error", "Please fill in all fields")
    else:
        messagebox.showwarning("Selection error", "Please select a user to update")

        def delete_user():
    selected_user = user_list.curselection()
    if selected_user:
        user_id = user_list.get(selected_user).split(" - ")[0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User deleted successfully")
        display_users()
    else:
        messagebox.showwarning("Selection error", "Please select a user to delete")

