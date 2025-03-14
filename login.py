import customtkinter as ctk
from tkinter import messagebox
from firebase_admin import auth
from firebase_config import initialize_firebase
from cadastro_usuario import cadastro_usuario_screen 

initialize_firebase()

ctk.set_appearance_mode("black")  
ctk.set_default_color_theme("dark-blue")  

def login_user(email, senha):
    try:
        user = auth.get_user_by_email(email)
        return True
    except auth.AuthError:
        messagebox.showerror("Erro de autenticação. Verifique seu email ou senha.")
        return False

def attempt_login(email_entry, senha_entry):
    email = email_entry.get()
    senha = senha_entry.get()

    if login_user(email, senha):
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        login_screen.destroy()
        from principal import principal_screen
        principal_screen()
    else:
        messagebox.showerror("Erro", "Falha no login. Tente novamente.")

def login_screen():
    global login_screen
    login_screen = ctk.CTk()
    login_screen.title("Tela de Login - Sistema de Biblioteca")
    login_screen.geometry("400x400")

    header = ctk.CTkLabel(
        login_screen, 
        text="Usuário:", 
        font=("Arial", 20, "bold"))
    header.pack(pady=10)

    email_label = ctk.CTkLabel(login_screen, text="Email:")
    email_label.pack()
    email_entry = ctk.CTkEntry(login_screen,placeholder_text='Digite seu email')
    email_entry.pack(pady=5)

    senha_label = ctk.CTkLabel(login_screen, text="Senha:")
    senha_label.pack()
    senha_entry = ctk.CTkEntry(login_screen, placeholder_text= 'Digite sua senha', show="*")
    senha_entry.pack(pady=5)

    login_button = ctk.CTkButton(
        login_screen, 
        text="Entrar", command=lambda: attempt_login(email_entry, senha_entry), 
        fg_color="#1472b4", 
        hover_color="dark blue", 
        corner_radius=10, 
        width=140, 
        height=30)
    login_button.pack(pady=10)

    cadastro_button = ctk.CTkButton(
        login_screen, 
        text="Cadastrar Novo Usuário", 
        command=cadastro_usuario_screen, 
        fg_color="#1472b4", 
        hover_color="dark blue", 
        corner_radius=10, 
        width=115, 
        height=30, 
        font=("Arial", 11))
    cadastro_button.pack(pady=5)

    login_screen.mainloop()


