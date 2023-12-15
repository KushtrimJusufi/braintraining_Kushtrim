
from result import *
from tkinter import *
from database import *

# fonction qui crée un résultat
def create_result(create):
    # date complet
    date_complet = f"{entry_dateY.get()}-{entry_dateM.get()}-{entry_dateD.get()}"

    #duration complet
    duration_complet = f"{entry_durationM.get()}:{entry_durationS.get()}"

    # les valeurs pour le insert into
    create = f" values ('{entry_pseudo.get()}', '{entry_exercise.get()}', '{date_complet}', '{duration_complet}', '{entry_nb_total.get()}', '{entry_nb_W.get()}')"

    # une requête SQL qui va créer un résultat
    query = ("insert into result (name, exercise, date_hour, duration, nbtrials, nbsuccess)")
    query = query + create
    print(query)
    cursor = db_connection.cursor()
    cursor.execute(query, )

def open_window_CRUD(window_result):
    global entry_pseudo
    global entry_exercise
    global entry_dateY
    global entry_dateM
    global entry_dateD
    global entry_durationM
    global entry_durationS
    global entry_nb_total
    global entry_nb_W
    window_CRUD = tk.Toplevel(window_result)

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window_CRUD.configure(bg=hex_color)

    window_CRUD.title("creation d'un résultat")
    window_CRUD.geometry("900x50")

    # entry qui servent à creer une donnée
    frame1 = tk.Frame(window_CRUD)
    frame1.pack()

    # titre du pseudo
    lbl_Pseudo = tk.Label(frame1, text="Pseudo:", font=("Arial", 13))
    lbl_Pseudo.pack(side=LEFT,)

    # entry de pseudo
    entry_pseudo = tk.Entry(frame1, width=10)
    entry_pseudo.pack(side=LEFT,padx=5)

    # titre du exercise
    lbl_exercise = tk.Label(frame1, text="Exercise:", font=("Arial", 13))
    lbl_exercise.pack(side=LEFT)

    # entrée de l'exercice
    entry_exercise = tk.Entry(frame1, width=10)
    entry_exercise.pack(side=LEFT,padx=5)

    # titre de la date
    lbl_dateY = tk.Label(frame1, text="date:", font=("Arial", 13))
    lbl_dateY.pack(side=LEFT)

    # entrée de la date pour l'année
    entry_dateY = tk.Entry(frame1, width=4)
    entry_dateY.pack(side=LEFT)

    # titre de le mois
    lbl_dateM = tk.Label(frame1, text="/", font=("Arial", 13))
    lbl_dateM.pack(side=LEFT)

    # entrée de la date pour le mois
    entry_dateM = tk.Entry(frame1, width=4)
    entry_dateM.pack(side=LEFT)

    # titre de le jour
    lbl_dateD = tk.Label(frame1, text="/", font=("Arial", 13))
    lbl_dateD.pack(side=LEFT)

    # entrée de la date pour le jour
    entry_dateD = tk.Entry(frame1, width=4)
    entry_dateD.pack(side=LEFT)

    # titre duration minute
    lbl_durationM = tk.Label(frame1, text="Chrono:", font=("Arial", 13))
    lbl_durationM.pack(side=LEFT)

    # entrée de duration minute
    entry_durationM = tk.Entry(frame1, width=4)
    entry_durationM.pack(side=LEFT)

    # titre duration seconde
    lbl_durationS = tk.Label(frame1, text=":", font=("Arial", 13))
    lbl_durationS.pack(side=LEFT)

    # entrée de duration seconde
    entry_durationS = tk.Entry(frame1, width=4)
    entry_durationS.pack(side=LEFT)

    # titre nb total
    lbl_nb_total = tk.Label(frame1, text="Nb total:", font=("Arial", 13))
    lbl_nb_total.pack(side=LEFT)

    # entrée de nb total
    entry_nb_total = tk.Entry(frame1, width=4)
    entry_nb_total.pack(side=LEFT)

    # titre nb réussi
    lbl_nb_W = tk.Label(frame1, text="Nb réussi:", font=("Arial", 13))
    lbl_nb_W.pack(side=LEFT)

    # entrée de nb réussi
    entry_nb_W = tk.Entry(frame1, width=4)
    entry_nb_W.pack(side=LEFT)

    # bouton qui va créer le résultat
    btn_create = tk.Button(frame1, text="create", font=("Arial", 13))
    btn_create.pack(side=BOTTOM, padx=30)
    btn_create.bind("<Button-1>", create_result)