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

 

