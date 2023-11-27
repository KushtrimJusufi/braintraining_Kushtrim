# Exemple de conversion de tuple en tableau
# JCY oct 23
# PRO DB PY

import tkinter as tk

data=(("Barack","Obama",1962),
      ("Joe","Biden",1942),
      ("John","Kennedy",1917))

def display_tuple_in_table(mytuple):
   for line in range(0,len(mytuple)):
        for col in range(0, len(mytuple[line])):
            (tk.Label(frame_results, text=mytuple[line][col], width=15, font=("Arial", 10)).grid(row=line, column=col, padx=2, pady=2))

def clear(event):
    for widget in frame_results.winfo_children():
        widget.grid_forget()

window = tk.Tk()
window.title("Affichage braintraining")
window.geometry("1100x900")

# Title création
lbl_title = tk.Label(window, text="EXEMPLE AFFICHAGE", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

btn_display = tk.Button(window, text="Affiche", font=("Arial", 10))
btn_display.grid(row=1, column=0, padx=2, pady=2)
btn_display.bind("<Button-1>", lambda e: display_tuple_in_table(data))

btn_clear = tk.Button(window, text="Vide", font=("Arial", 10))
btn_clear.grid(row=1, column=1, padx=2, pady=2)
btn_clear.bind("<Button-1>", clear)

frame_results = tk.Frame(window)
frame_results.grid(row=2, sticky="ew", pady=2, padx=2)


# main loop
window.mainloop()
