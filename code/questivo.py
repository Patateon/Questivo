import tkinter as tk
import openai
import threading

# Initialisation de l'API OpenAI avec votre clé API
openai.api_key = ""

# Fonction pour interroger l'API GPT via la nouvelle interface ChatCompletion
def get_answer(question):
    try:
        # Appel de l'API GPT pour obtenir la réponse
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Utilise GPT-3.5-turbo ou GPT-4 si vous y avez accès
            messages=[
                {"role": "system", "content": "Tu es un assistant utile."},  # Contexte donné à l'assistant
                {"role": "user", "content": question},  # La question de l'utilisateur
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erreur lors de la récupération de la réponse : {str(e)}"

# Classe principale de l'interface utilisateur
class QuestionAnswerTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Outil de Question-Réponse avec LLM")
        
        # Interface utilisateur
        self.label_question = tk.Label(self.root, text="Entrez votre question :")
        self.label_question.pack()

        self.entry_question = tk.Entry(self.root, width=50)
        self.entry_question.pack()

        self.button_ask = tk.Button(self.root, text="Poser la question", command=self.ask_question)
        self.button_ask.pack()

        self.label_answer = tk.Label(self.root, text="Réponse :", pady=10)
        self.label_answer.pack()

        self.text_answer = tk.Text(self.root, wrap=tk.WORD, height=10, width=60)
        self.text_answer.pack()

    def ask_question(self):
        question = self.entry_question.get()
        if question:
            # Utiliser un thread pour ne pas bloquer l'interface
            threading.Thread(target=self.display_answer, args=(question,)).start()

    def display_answer(self, question):
        self.text_answer.delete(1.0, tk.END)  # Efface la réponse précédente
        self.text_answer.insert(tk.END, "Réponse en cours...\n")
        
        # Obtenir la réponse via l'API LLM
        answer = get_answer(question)
        self.text_answer.delete(1.0, tk.END)  # Efface l'indication de réponse en cours
        self.text_answer.insert(tk.END, answer)  # Affiche la réponse finale

# Lancer l'application Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionAnswerTool(root)
    root.mainloop()
