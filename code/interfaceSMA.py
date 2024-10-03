import tkinter as tk
from tkinter import messagebox
import random
import time
import json
from PIL import Image, ImageTk

# Chargement des questions depuis le fichier JSON
with open('questions_college.json', 'r', encoding='utf-8') as json_file:
    themes_questions = json.load(json_file)

# Variables pour le jeu
score = 0
current_question = None
start_time = None  # Pour enregistrer le début du chronomètre
asked_questions = []  # Liste pour garder les questions déjà posées

def choisir_theme():
    global theme_secret, filtered_questions, asked_questions
    theme_secret = random.choice(list(themes_questions.keys()))
    filtered_questions = themes_questions[theme_secret]
    asked_questions = []  # Réinitialiser les questions posées
    start_timer()
    poser_question()

# Fonction pour afficher une nouvelle question
def poser_question():
    global current_question
    if len(filtered_questions) == 0:
        messagebox.showinfo("Thème épuisé", f"Vous avez épuisé toutes les questions pour le thème '{theme_secret}'.\nUn nouveau thème sera choisi.")
        choisir_theme()  # Choisir un nouveau thème
        return
    
    current_question = random.choice(filtered_questions)
    question_label.config(text=current_question["question"])
    asked_questions.append(current_question)  # Ajouter la question posée à la liste
    filtered_questions.remove(current_question)  # Retirer la question de la liste des questions restantes

# Fonction pour valider la réponse
def valider_reponse():
    global score
    reponse = entree_reponse.get().lower().strip()
    
    if reponse == current_question["answer"]:
        score += 1
        score_label.config(text=f"Score : {score}")
        messagebox.showinfo("Bonne réponse", f"Bravo ! Vous avez {score} point(s).")
        poser_question()
    else:
        messagebox.showerror("Mauvaise réponse", f"Désolé, la bonne réponse était : {current_question['answer']}.")
        poser_question()  # Passer à la question suivante même si la réponse est incorrecte
    entree_reponse.delete(0, tk.END)

# Fonction pour deviner le thème secret
def deviner_theme():
    global start_time
    devine = entree_theme.get().lower().strip()
    if devine == theme_secret:
        end_time = time.time()  # Enregistrer le temps de fin
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        messagebox.showinfo("Thème", f"Félicitations ! Vous avez deviné le thème secret : {theme_secret}.\n"
                                     f"Temps écoulé : {minutes} minute(s) et {seconds} seconde(s).\n"
                                     f"Score final : {score}.")
        choisir_theme()  # Choisir un nouveau thème après avoir deviné correctement
    else:
        messagebox.showerror("Thème", "Ce n'est pas le bon thème. Essayez encore !")

# Fonction pour démarrer le chronomètre
def start_timer():
    global start_time
    start_time = time.time()

# Affichage du chronomètre en haut à droite
def update_timer():
    if start_time:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
    root.after(1000, update_timer)

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Questivo")
root.geometry("800x600")  # Taille par défaut
root.config(bg='gray20')

# Affichage du score en haut à gauche
score_label = tk.Label(root, text="Score : 0", font=("Helvetica", 14), fg="white", bg="gray20")
score_label.place(relx=0.05, rely=0.05)

# Charger et afficher l'image "Questivo"
original_image = Image.open("images/Questivo.png")
photo = ImageTk.PhotoImage(original_image)
image_label = tk.Label(root, image=photo, bg="gray20")
image_label.place(relx=0.25, rely=0.05)

# Cadre pour la question avec un encadré autour
question_frame = tk.Frame(root, bg='gray30', bd=3, relief="ridge")
question_frame.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.2)
question_label = tk.Label(question_frame, text="Question ici", font=("Helvetica", 14), fg="white", bg="gray30")
question_label.pack(expand=True, fill="both")

# Label pour la réponse à la question
label_reponse = tk.Label(root, text="Réponse à la question :", font=("Helvetica", 12), fg="white", bg="gray20")
label_reponse.place(relx=0.1, rely=0.65)

# Zone de saisie pour la réponse
entree_reponse = tk.Entry(root, font=("Helvetica", 12))
entree_reponse.place(relx=0.1, rely=0.7, relwidth=0.6, relheight=0.05)

# Bouton pour valider la réponse
btn_valider = tk.Button(root, text="Valider", font=("Helvetica", 12), command=valider_reponse)
btn_valider.place(relx=0.75, rely=0.7, relwidth=0.15, relheight=0.05)

# Label pour la devinette du thème
label_theme = tk.Label(root, text="Deviner le thème :", font=("Helvetica", 12), fg="white", bg="gray20")
label_theme.place(relx=0.1, rely=0.8)

# Zone de saisie pour deviner le thème
entree_theme = tk.Entry(root, font=("Helvetica", 12))
entree_theme.place(relx=0.1, rely=0.85, relwidth=0.6, relheight=0.05)

# Bouton "Deviner le thème"
btn_theme = tk.Button(root, text="Deviner le thème", font=("Helvetica", 12), command=deviner_theme)
btn_theme.place(relx=0.75, rely=0.85, relwidth=0.15, relheight=0.05)

# Affichage du chronomètre en haut à droite
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 14), fg="white", bg="gray20")
timer_label.place(relx=0.85, rely=0.05)

# Démarrage du chronomètre et de la première question
choisir_theme()
update_timer()

root.mainloop()
