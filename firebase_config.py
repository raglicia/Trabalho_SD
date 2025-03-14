import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:/Sistemas de informação/8 periodo/Sistemas distribuidos/unidade 1/gerenciador de livros/cadastro-de-livros-3bbc2.json")
        firebase_admin.initialize_app(cred)
    else:
        print("Firebase já foi inicializado.")
