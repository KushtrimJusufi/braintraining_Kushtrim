import tkinter as tk
from tkinter import *
from database import *
import result


def create_user(name, password):
    query = "INSERT INTO users (name, password) values (%s,%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, password))
    lastrowid = cursor.lastrowid
    cursor.close()
    return lastrowid

def login_window_result(window):
    username = "kushtrim"
    password = "1234"


    window_login = tk.Toplevel(window)

    def connection(event):
        if username == entry_user.get() and password == entry_password.get():
            result.open_window_result(window)
            print("display_result")
            Tk.destroy(window_login)
        else:
            error_msg.pack()
            error_msg2.pack()
            frame5.pack()

    def register():
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
        window_login.configure(bg=hex_color)

        window_login.title("login")
        window_login.geometry("600x600")
        in_construction = ""
        #en construction



    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window_login.configure(bg=hex_color)

    window_login.title("login")
    window_login.geometry("600x600")

    #frame logo login
    frame1 = tk.Frame(window_login)
    frame1.pack(pady=10)

    # label logo login
    label_titre = tk.Label(frame1,text="Login", font=("Arial", 20))
    label_titre.pack()

    #frame le username
    frame2 = tk.Frame(window_login)
    frame2.pack(pady=30)

    #label de l'identifiant
    label_user = tk.Label(frame2, text="Identifiant:", font=("Arial", 20))
    label_user.pack(padx=5, side=LEFT)

    #entry de l'identifiant
    entry_user = tk.Entry(frame2, width=25, font=("Arial", 20))
    entry_user.pack(side=LEFT, pady=10)

    #frame le mot de passe
    frame3 = tk.Frame(window_login)
    frame3.pack(pady=30)

    # label du mot de passe
    label_password = tk.Label(frame3, text="Mot de passe:", font=("Arial", 20))
    label_password.pack(padx=5, side=LEFT)

    # entry du mot de passe
    entry_password = tk.Entry(frame3,width=25, font=("Arial", 20), show="*")
    entry_password.pack(side=LEFT, pady=10)

    #frame pour le bouton confirmer
    frame4 = tk.Frame(window_login)
    frame4.pack(pady=30)

    # frame pour le message d'erreur
    frame5 = tk.Frame(window_login, highlightthickness=4, highlightbackground="red")
    frame5.pack_forget()

    #label du message d'erreur
    error_msg = tk.Label(frame5, text="L'identifiant ou Le mot de passe est faux", font=("Arial", 20))
    error_msg.pack_forget()

    error_msg2 = tk.Label(frame5, text="ou mal écrit", font=("Arial", 20))
    error_msg2.pack_forget()

    # bouton connecter
    btn = tk.Button(frame4, text="login", font=("Arial", 20))
    btn.pack(pady= 10)
    btn.bind("<Button-1>", connection)

    # bouton s'inscrire
    btn = tk.Button(frame4, text="register", font=("Arial", 20))
    btn.pack()
    btn.bind("<Button-1>", register())
