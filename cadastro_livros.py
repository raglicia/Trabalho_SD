
import customtkinter as ctk
from tkinter import messagebox
from firebase_admin import firestore

ctk.set_appearance_mode("black")  
ctk.set_default_color_theme("dark-blue")  

def adicionar_livro(titulo, autor, paginas, ano):
    if not titulo.strip() or not autor.strip() or not paginas.strip() or not ano.strip():
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    db = firestore.client()
    db.collection("livros").add({
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
        "ano": ano
    })
    messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
    cadastro_livros_screen.destroy()

def cadastro_livros_screen():
    global cadastro_livros_screen
    cadastro_livros_screen = ctk.CTk()
    cadastro_livros_screen.title("Cadastro de Livro - Sistema de Biblioteca")
    cadastro_livros_screen.geometry("400x400")

    header = ctk.CTkLabel(cadastro_livros_screen, text="Cadastro de Livro:", font=("Arial", 20, "bold"))
    header.pack(pady=10)

    titulo_label = ctk.CTkLabel(cadastro_livros_screen, text="Título:")
    titulo_label.pack()
    titulo_entry = ctk.CTkEntry(cadastro_livros_screen)
    titulo_entry.pack(pady=5)

    autor_label = ctk.CTkLabel(cadastro_livros_screen, text="Autor:")
    autor_label.pack()
    autor_entry = ctk.CTkEntry(cadastro_livros_screen)
    autor_entry.pack(pady=5)

    paginas_label = ctk.CTkLabel(cadastro_livros_screen, text="Número de Páginas:")
    paginas_label.pack()
    paginas_entry = ctk.CTkEntry(cadastro_livros_screen)
    paginas_entry.pack(pady=5)

    ano_label = ctk.CTkLabel(cadastro_livros_screen, text="Ano de Publicação:")
    ano_label.pack()
    ano_entry = ctk.CTkEntry(cadastro_livros_screen)
    ano_entry.pack(pady=5)

    adicionar_button = ctk.CTkButton(
        cadastro_livros_screen, 
        text="Cadastrar", 
        command=lambda: adicionar_livro(
            titulo_entry.get(),
            autor_entry.get(),
            paginas_entry.get(),
            ano_entry.get()
        ),
        fg_color="#1472b4",
        hover_color="dark blue",
        corner_radius=10,
        width=140,
        height=30
    )
    adicionar_button.pack(pady=20)

    cadastro_livros_screen.mainloop()

