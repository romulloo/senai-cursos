import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
janela.title("Meu App")
janela.geometry("400x200")#Largura x altura em pixels

label = ttk.Label(janela, text="Ola!")
label.pack(pady=20, padx=20)
texto = ttk.Entry(janela, width=20)
texto.pack(pady=30)
#Loop eventos
janela.mainloop()
