import tkinter as tk
import create
from tkinter import *
from database import *

#les catégories des résultats
categorie_result = [('Elève', 'Exercice', 'Date heure', 'Temps', 'nb Total', 'nb OK')]

# les catégorie des totales
categorie_total = [('NBLignes', 'Temps total', 'Nb OK', 'Nb total')]

# requête SQL qui va prendre les données de la base de données
def data_result(pseudo):
    condition = ""
    i = 0

    if entry_pseudo.get() == "" and entry_exercice.get() == "" and entry_date_start.get() == "" and entry_date_end.get() == "":
        query = ("select name, exercise, date_hour, duration, nbtrials, nbsuccess from result LIMIT 10")
        cursor = db_connection.cursor()
        cursor.execute(query,)
        data = cursor.fetchall()
        return data
    else:
        if entry_pseudo.get() != "":
            condition += f" where name = '{entry_pseudo.get()}' "
            i += 1

        if entry_exercice.get() != "" and i > 0:
            condition += f" and exercise = '{entry_exercice.get()}' "
        elif entry_exercice.get() != "" and i == 0:
            condition += f" where exercise = '{entry_exercice.get()}' "
            i += 1

        if entry_date_start.get() != "" and i > 0:
            condition += f" and date_hour LIKE '{entry_date_start.get()}%' "
        elif entry_date_start.get() != "" and i == 0:
            condition += f" where date_hour LIKE '%{entry_date_start.get()}%' "
            i += 1

        query = "select name, exercise, date_hour, duration, nbtrials, nbsuccess from result"
        query = query + condition
        print(query)
        cursor = db_connection.cursor()
        cursor.execute(query, )
        data = cursor.fetchall()
        return data

# requête SQL qui va prendre le total des résultats
def data_total(e):
    if entry_pseudo.get() == "":
        query = ("select count(id), SEC_TO_TIME(SUM(TIME_TO_SEC(result.duration))), sum(nbtrials) ,sum(nbsuccess) from result")
        cursor = db_connection.cursor()
        cursor.execute(query)
        total = cursor.fetchall()
        return total
    else:
        query = ("select count(id), SEC_TO_TIME(SUM(TIME_TO_SEC(result.duration))), sum(nbtrials) ,sum(nbsuccess) from result where name = (%s)")
        cursor = db_connection.cursor()
        cursor.execute(query, (e,))
        total = cursor.fetchall()
        return total


# fonction qui va creer un tableau avec les données
def disaplay(mytuple, frame):
    for line in range(0,len(mytuple)):
        for col in range(0, len(mytuple[line])):
            (tk.Label(frame, text=mytuple[line][col], width=16, font=("Arial", 14)).grid(row=line, column=col, padx=2, pady=4))

# cette fonction crée une fenêtre qui affiche les résultats
def open_window_result(window):
    global frame3_1
    global frame3_2
    global frame5_1
    global frame5_2
    global entry_pseudo
    global entry_exercice
    global entry_date_end
    global entry_date_start

    window_result = tk.Toplevel(window)

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window_result.configure(bg=hex_color)

    window_result.title("résultat")
    window_result.geometry("1100x900")

    # frame pour le titre
    frame1 = tk.Frame(window_result)
    frame1.pack()

    lbl_title = tk.Label(frame1, text="TRAINING AFFICHAGE", font=("Arial", 20))
    lbl_title.pack(pady = 20)

    # frame pour les entrées pour filtrer et le bouton pour afficher les résultats avec les filtres
    frame2 = tk.Frame(window_result)
    frame2.pack(pady=20)

    # frame pour les entrées
    frame2_1 = tk.Frame(frame2)
    frame2_1.pack(side=TOP)

    lbl_pseudo = tk.Label(frame2_1, text="Pseudo: ", font=("Arial", 13))
    lbl_pseudo.pack(side=LEFT, padx=5)

    entry_pseudo = tk.Entry(frame2_1)
    entry_pseudo.pack(side=LEFT, padx=5)

    lbl_exercice = tk.Label(frame2_1, text="exercice: ", font=("Arial", 13))
    lbl_exercice.pack(side=LEFT, padx=5)

    entry_exercice= tk.Entry(frame2_1)
    entry_exercice.pack(side=LEFT, padx=5)

    lbl_date_start = tk.Label(frame2_1, text="Date début: ", font=("Arial", 13))
    lbl_date_start.pack(side=LEFT, padx=5)

    entry_date_start = tk.Entry(frame2_1)
    entry_date_start.pack(side=LEFT, padx=5)

    lbl_date_end = tk.Label(frame2_1, text="Date fin: ", font=("Arial", 13))
    lbl_date_end.pack(side=LEFT, padx=5)

    entry_date_end = tk.Entry(frame2_1)
    entry_date_end.pack(side=LEFT, padx=5)

    # frame pour le bouton qui confirme le filtre
    frame2_2 = tk.Frame(frame2)
    frame2_2.pack(side=BOTTOM, fill=X)

    # frame pour les donnée enregistré
    frame3 = tk.Frame(window_result)
    frame3.pack()

    # frame pour les catégories
    frame3_1 = tk.Frame(frame3)
    frame3_1.pack(side=TOP, pady=10)


    # frame pour les résultats
    frame3_2 = tk.Frame(frame3)
    frame3_2.pack(side=BOTTOM)

    # frame pour le label total
    frame4 = tk.Frame(window_result)
    frame4.pack(pady=5)

    # label total
    lbl_total = tk.Label(frame4, text="Total", font=("Arial", 15))
    lbl_total.pack()

    # frame pour le total des résultats
    frame5 = tk.Frame(window_result)
    frame5.pack()

    frame5_1 = tk.Frame(frame5)
    frame5_1.pack(side = TOP)

    frame5_2 = tk.Frame(frame5)
    frame5_2.pack()

    # fonction qui permet d'ouvrir la fenêtre de la creation
    def open_create(event):
        CRUD.open_window_CRUD(window_result)
        print("display_result")

    # avoir le pseudo dans l'entry
    pseudo = entry_pseudo.get()

    # fonction qui rafraichie les résultats
    def change_the_result(e):
        for widget in frame3_2.winfo_children():
            widget.grid_forget()
        pseudo = entry_pseudo.get()
        pseudo = str(pseudo)

        data_result(pseudo)
        data = data_result(pseudo)
        disaplay(data, frame3_2)

        data_total(pseudo)
        total = data_total(pseudo)
        disaplay(total, frame5_2)
        return pseudo


    # affiche le tableau des résultats
    data_result(pseudo)
    data = data_result(pseudo)
    disaplay(categorie_result, frame3_1)
    disaplay(data, frame3_2)

    # affiche le tableau des totaux
    data_total(pseudo)
    total = data_total(pseudo)
    disaplay(categorie_total, frame5_1)
    disaplay(total, frame5_2)

    # bouton qui trie les resultats
    but_result = tk.Button(frame2_2, text="Voir résultat")
    but_result.pack(side=LEFT, )
    but_result.bind("<Button-1>", change_the_result)

    # bouton qui ouvre une fenêtre avec les résultats
    but_result = tk.Button(frame2_2, text="Créer")
    but_result.pack(side=LEFT, padx=20)
    but_result.bind("<Button-1>", open_create)
