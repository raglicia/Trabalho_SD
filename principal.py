
import customtkinter as ctk
from cadastro_livros import cadastro_livros_screen
from listar_livros import listar_livros_screen  


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

def principal_screen():
    principal = ctk.CTk()
    principal.title("Tela Principal - Sistema de Biblioteca")
    principal.geometry("400x400")

   
    header = ctk.CTkLabel(principal, text="Bem-vindo ao Sistema de Biblioteca:", font=("Arial", 20, "bold"))
    header.pack(pady=20)

   
    cadastro_button = ctk.CTkButton(principal, text="Cadastrar Livro", command=cadastro_livros_screen, corner_radius=20, width=200, height=40)
    cadastro_button.pack(pady=15)

    listar_button = ctk.CTkButton(principal, text="Listar Livros", command=listar_livros_screen, corner_radius=20, width=200, height=40)
    listar_button.pack(pady=10)

    logout_button = ctk.CTkButton(principal, text="Sair", command=principal.quit, fg_color="blue", hover_color="dark blue", corner_radius=20, width=200, height=40)
    logout_button.pack(pady=20)

    principal.mainloop()



