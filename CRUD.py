import tkinter as tk
from tkinter import *
from database import *


#def open_window_CRUD(window_result):

window_CRUD = tk.Tk()

rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
window_CRUD.configure(bg=hex_color)

window_CRUD.title("creation d'un résultat")
window_CRUD.geometry("500x400")

# une requête SQL qui va créer un résultat
def create_result(create):
    query = (f"insert into result (name, exercise, date_hour, duration, nbtrials, nbsuccess values {create}")
    cursor = db_connection.cursor()
    cursor.execute(query, )
    create = cursor.fetchall()
    return create

# entry qui servent à creer une donnée
frame1 = tk.Frame(window_CRUD)
frame1.pack()

# titre du pseudo
lbl_Pseudo = tk.Label(frame1, text="Pseudo:")
lbl_Pseudo.pack(side=LEFT,)

# entry de pseudo
entry_pseudo = tk.Entry(frame1, width=10)
entry_pseudo.pack(side=LEFT,padx=5)

# titre du exercise
lbl_Pseudo = tk.Label(frame1, text="Exercise:")
lbl_Pseudo.pack(side=LEFT)

# entrée de l'exercice
entry_exercise = tk.Entry(frame1, width=10)
entry_exercise.pack(side=LEFT,padx=5)

# titre de la date
lbl_dateY = tk.Label(frame1, text="date:")
lbl_dateY.pack(side=LEFT)

# entrée de la date pour l'année
entry_dateY = tk.Entry(frame1, width=4)
entry_dateY.pack(side=LEFT)

# titre de le mois
lbl_dateM = tk.Label(frame1, text="/")
lbl_dateM.pack(side=LEFT)

# entrée de la date pour le mois
entry_dateM = tk.Entry(frame1, width=4)
entry_dateM.pack(side=LEFT)

# titre de le jour
lbl_dateD = tk.Label(frame1, text="/")
lbl_dateD.pack(side=LEFT)

# entrée de la date pour le jour
entry_dateD = tk.Entry(frame1, width=4)
entry_dateD.pack(side=LEFT)

# titre duration minute
lbl_durationM = tk.Label(frame1, text="Chrono:")
lbl_durationM.pack(side=LEFT)

# entrée de duration minute
entry_durationM = tk.Entry(frame1, width=4)
entry_durationM.pack(side=LEFT)

# titre duration minute
lbl_durationS = tk.Label(frame1, text=":")
lbl_durationS.pack(side=LEFT)

# entrée de duration minute
entry_durationS = tk.Entry(frame1, width=4)
entry_durationS.pack(side=LEFT)



window_CRUD.mainloop()