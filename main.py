import tkinter as tk
import os
import openpyxl
import sqlite3

#defining function:
def new():
    win = tk.Tk()
    win.title('User Information')
    win.geometry('250x250')
    username = user_email_entry.get()
    password = user_password_entry.get()
    
    #creating connection for database
    conn = sqlite3.connect('data.db')
    #filepath = '/home/maverick/Desktop/TkinterProjets/Login/data.db'
    table_create_query = '''CREATE TABLE IF NOT EXISTS login_information
    (username TEXT, password TEXT)'''
    conn.execute(table_create_query)
    #Insert Data
    data_insert_query = '''INSERT INTO login_information(username,password) VALUES(?,?)'''
    data_insert_tuple = (username,password)
    cursor = conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    conn.commit()
    
    conn.close()
    
    
    user_name = tk.Label(win,text="welcome")
    user_name.pack()
    
    
    window.destroy()
    win.mainloop()
window = tk.Tk()

window.geometry('500x500')

window.title('Login CRED')
window.configure(bg='#333333')

frame = tk.Frame(bg='#333333')

#creating fields for username and password
user_login = tk.Label(frame,text='LOGIN',bg='#333333',fg='#911423',font=('Arial',30))
user_email = tk.Label(frame,text="Username",bg='#333333',fg='#ffffff',font=('Arial',16))
user_email_entry = tk.Entry(frame,bg='#ffffff')
user_password= tk.Label(frame,text='Password',bg='#333333',fg='#ffffff',font=('Arial',16))
user_password_entry = tk.Entry(frame,show='*',bg='#ffffff')
login_button = tk.Button(frame,text='Login',command=new,bg='#911423',fg='#ffffff')
#creating grid
user_login.grid(row=0,column=1,sticky='news')
user_email.grid(row=1,column=0,sticky='news',pady=2)
user_email_entry.grid(row=1,column=1,sticky='news',pady=2)
user_password.grid(row=2,column=0,sticky='news',pady=2)
user_password_entry.grid(row=2,column=1,sticky='news',pady=2)
login_button.grid(row=3,column=1,sticky='news',pady=10)

frame.pack()
window.mainloop()

