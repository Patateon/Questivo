import tkinter as tk
from tkinter import messagebox

# Fonction pour afficher un message d'aide
def aide():
    messagebox.showinfo("Aide", "Indice : Il est connu pour son rôle dans l'Histoire de France.")

# Fonction pour afficher un message quand le bouton "Deviner le thème" est cliqué
def deviner_theme():
    messagebox.showinfo("Thème", "Le thème est probablement 'Histoire de France'.")

# Fonction pour valider la réponse
def valider_reponse():
    reponse = entree_reponse.get()
    if reponse.lower() == "napoléon":
        messagebox.showinfo("Bonne réponse", "Bravo, c'est la bonne réponse !")
    else:
        messagebox.showerror("Mauvaise réponse", "Désolé, ce n'est pas la bonne réponse.")

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Questivo")

# Dimensions de la fenêtre
root.geometry("600x500")
root.config(bg='gray20')

# Ajout du chronomètre
label_timer = tk.Label(root, text="05:00", font=("Helvetica", 24), fg="white", bg="gray20")
label_timer.place(x=50, y=50)

# Ajout du robot souriant
canvas = tk.Canvas(root, width=80, height=80, bg="gray20", highlightthickness=0)
canvas.place(x=50, y=120)
robot_image = tk.PhotoImage(file="robot_image.png")  
canvas.create_image(40, 40, image=robot_image)

# Texte de la question
question_label = tk.Label(root, text="Je suis né en Corse et j'ai régné sur la France.\nQui suis-je ?", font=("Helvetica", 14), fg="white", bg="gray20")
question_label.place(x=150, y=50)

# Ajout d'un bouton "Besoin d'aide ?"
btn_aide = tk.Button(root, text="Besoin d'aide ?", font=("Helvetica", 12), command=aide)
btn_aide.place(x=50, y=220)

# Ajout d'une bulle de réflexion
canvas_bulle = tk.Canvas(root, width=150, height=100, bg="gray20", highlightthickness=0)
canvas_bulle.place(x=50, y=300)
lightbulb_image = tk.PhotoImage(file="lightbulb.png")  
canvas_bulle.create_image(75, 50, image=lightbulb_image)

# Ajout d'un bouton "Deviner le thème"
btn_theme = tk.Button(root, text="Deviner le thème", font=("Helvetica", 12), command=deviner_theme)
btn_theme.place(x=250, y=220)

# Ajout d'une zone de saisie pour la réponse
entree_reponse = tk.Entry(root, font=("Helvetica", 12))
entree_reponse.place(width=300, height=30, x=150, y=400)

# Ajout d'un bouton pour valider la réponse
btn_valider = tk.Button(root, text="Valider", font=("Helvetica", 12), command=valider_reponse)
btn_valider.place(x=470, y=400)

root.mainloop()
