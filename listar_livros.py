
import customtkinter as ctk
from tkinter import messagebox
from firebase_admin import firestore

def excluir_livro(livro_id, listar_livros_window):
    db = firestore.client()
    db.collection("livros").document(livro_id).delete()
    messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
    listar_livros_window.destroy()
    listar_livros_screen()  

def editar_livro(livro_id, listar_livros_window):
    db = firestore.client()
    livro_ref = db.collection("livros").document(livro_id)
    livro_data = livro_ref.get().to_dict()

    editar_window = ctk.CTkToplevel()
    editar_window.title("Editar Livro")
    editar_window.geometry("400x400")

    ctk.CTkLabel(editar_window, text="Editar Livro", font=("Arial", 18, "bold")).pack(pady=10)

    titulo_entry = ctk.CTkEntry(editar_window, width=250)
    titulo_entry.insert(0, livro_data["titulo"])
    titulo_entry.pack(pady=5)

    autor_entry = ctk.CTkEntry(editar_window, width=250)
    autor_entry.insert(0, livro_data["autor"])
    autor_entry.pack(pady=5)

    paginas_entry = ctk.CTkEntry(editar_window, width=250)
    paginas_entry.insert(0, str(livro_data["paginas"]))
    paginas_entry.pack(pady=5)

    ano_entry = ctk.CTkEntry(editar_window, width=250)
    ano_entry.insert(0, str(livro_data["ano"]))
    ano_entry.pack(pady=5)

    def salvar_edicao():
        livro_ref.update({
            "titulo": titulo_entry.get(),
            "autor": autor_entry.get(),
            "paginas": int(paginas_entry.get()),
            "ano": int(ano_entry.get()),
        })
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
        editar_window.destroy()
        listar_livros_window.destroy()
        listar_livros_screen()

    salvar_button = ctk.CTkButton(editar_window, text="Salvar", command=salvar_edicao, corner_radius=10, fg_color="blue")
    salvar_button.pack(pady=10)

def listar_livros_screen():
    listar_livros_window = ctk.CTk()
    listar_livros_window.title("Listar Livros - Sistema de Biblioteca")
    listar_livros_window.geometry("500x400")

    header = ctk.CTkLabel(listar_livros_window, text="Lista de Livros Cadastrados:", font=("Arial", 20, "bold"))
    header.pack(pady=10)

    tabela_frame = ctk.CTkFrame(listar_livros_window)
    tabela_frame.pack(pady=10, padx=10, fill="both", expand=True)

    colunas = ["Título", "Autor", "Páginas", "Ano", "Ações"]
    for col_idx, col_name in enumerate(colunas):
        label = ctk.CTkLabel(tabela_frame, text=col_name, font=("Arial", 12, "bold"), padx=5, pady=5)
        label.grid(row=0, column=col_idx, sticky="nsew")

    db = firestore.client()
    livros_ref = db.collection("livros")
    livros = livros_ref.stream()

    for row_idx, livro in enumerate(livros, start=1):
        livro_data = livro.to_dict()
        livro_id = livro.id

        ctk.CTkLabel(tabela_frame, text=livro_data["titulo"], font=("Arial", 10)).grid(row=row_idx, column=0, sticky="nsew")
        ctk.CTkLabel(tabela_frame, text=livro_data["autor"], font=("Arial", 10)).grid(row=row_idx, column=1, sticky="nsew")
        ctk.CTkLabel(tabela_frame, text=livro_data["paginas"], font=("Arial", 10)).grid(row=row_idx, column=2, sticky="nsew")
        ctk.CTkLabel(tabela_frame, text=livro_data["ano"], font=("Arial", 10)).grid(row=row_idx, column=3, sticky="nsew")

        editar_button = ctk.CTkButton(
            tabela_frame, 
            text="Editar", 
            command=lambda livro_id=livro_id: editar_livro(livro_id, listar_livros_window), 
            corner_radius=10, 
            fg_color="#1472b4"  
        )
        editar_button.grid(row=row_idx, column=4, padx=5, pady=5)

        excluir_button = ctk.CTkButton(
            tabela_frame, 
            text="Excluir", 
            command=lambda livro_id=livro_id: excluir_livro(livro_id, listar_livros_window), 
            corner_radius=10, 
            fg_color="#1472b4"  
        )
        excluir_button.grid(row=row_idx, column=5, padx=5, pady=5)

    fechar_button = ctk.CTkButton(
        listar_livros_window, 
        text="Fechar", 
        command=listar_livros_window.destroy, 
        fg_color="blue", 
        hover_color="dark blue", 
        corner_radius=20, 
        width=150, 
        height=40
    )
    fechar_button.pack(pady=20)

    listar_livros_window.mainloop()


