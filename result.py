import tkinter as tk
from tkinter import *
from database import *

'''window = tk.Tk()
window.title("affichage")
window.geometry("1000x900")'''

def data_result():
    query = ("select name, exercise, date_hour, duration, nbtrials, nbsuccess from result")
    cursor = db_connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    return data

def disaplay(mytuple):
    for line in range(0,len(mytuple)):
        for col in range(0, len(mytuple[line])):
            (tk.Label(frame3, text=mytuple[line][col], width=15, font=("Arial", 10)).grid(row=line, column=col, padx=2, pady=2))

# cette fonction crée une fenêtre qui affiche les résultats
def open_window_result(window):
    global frame3

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

    # inutilisable pour l'instant
    but_result = tk.Button(frame2_2, text="Voir résultat")
    but_result.pack(side=LEFT,)

    # frame pour les donnée enregistré
    frame3 = tk.Frame(window_result)
    frame3.pack()

    # frame pour le label total
    frame4 = tk.Frame(window_result)
    frame4.pack()

    frame5 = tk.Frame(window_result)
    frame5.pack()

    data_result()
    data = data_result()

    disaplay(data)