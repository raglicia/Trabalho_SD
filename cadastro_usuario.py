import customtkinter as ctk
from tkinter import messagebox
from firebase_admin import auth
from firebase_config import initialize_firebase

initialize_firebase()

ctk.set_appearance_mode("black")  
ctk.set_default_color_theme("dark-blue")  

def cadastrar_usuario(email, senha):
    try:
        user = auth.create_user(
            email=email,
            password=senha
        )
        messagebox.showinfo("Sucesso", f"Usuário {email} cadastrado com sucesso!")
        cadastro_usuario_screen.destroy()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar usuário:")

def cadastro_usuario_screen():
    global cadastro_usuario_screen
    cadastro_usuario_screen = ctk.CTk()
    cadastro_usuario_screen.title("Cadastro de Usuário - Sistema de Biblioteca")
    cadastro_usuario_screen.geometry("400x400")

    header = ctk.CTkLabel(cadastro_usuario_screen, text="Cadastro de Usuário:", font=("Arial", 20, "bold"))
    header.pack(pady=10)

    email_label = ctk.CTkLabel(cadastro_usuario_screen, text="Email:")
    email_label.pack()
    email_entry = ctk.CTkEntry(cadastro_usuario_screen,placeholder_text='email')
    email_entry.pack(pady=5)

    senha_label = ctk.CTkLabel(cadastro_usuario_screen, text="Senha:")
    senha_label.pack()
    senha_entry = ctk.CTkEntry(cadastro_usuario_screen, placeholder_text='senha', show="*")
    senha_entry.pack(pady=5)

    cadastrar_button = ctk.CTkButton(
        cadastro_usuario_screen,
        text="Cadastrar",
        command=lambda: cadastrar_usuario(
            email_entry.get(), senha_entry.get()
        ),
        fg_color="#1472b4",
        hover_color="dark blue",
        corner_radius=10,
        width=140,
        height=30
    )
    cadastrar_button.pack(pady=20)

    cadastro_usuario_screen.mainloop()
