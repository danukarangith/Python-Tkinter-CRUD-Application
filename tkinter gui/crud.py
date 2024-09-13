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

# Function to insert user into the database
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
    conn.close()

# Function to update user details
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

# Function to delete user
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

# Creating the Tkinter window
root = Tk()
root.title("Simple CRUD with Tkinter and MySQL")

# GUI Components
label_name = Label(root, text="Name:")
label_name.grid(row=0, column=0)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

label_email = Label(root, text="Email:")
label_email.grid(row=1, column=0)
entry_email = Entry(root)
entry_email.grid(row=1, column=1)

add_button = Button(root, text="Add User", command=add_user)
add_button.grid(row=2, column=0, pady=10)

update_button = Button(root, text="Update User", command=update_user)
update_button.grid(row=2, column=1)

delete_button = Button(root, text="Delete User", command=delete_user)
delete_button.grid(row=2, column=2)

# Listbox to display users
user_list = Listbox(root, width=50)
user_list.grid(row=3, column=0, columnspan=3)
display_users()

root.mainloop()

