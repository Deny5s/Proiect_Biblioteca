import json
import os
from models import Carte, Autor
from decorators import logare_actiuni
from utils import afiseaza_titlu, filtrare_carti, rating_mediu, titluri_carti_autori_nationalitate

class Biblioteca:
    def __init__(self):
        self.carti = []
        self. autori = []


    def adauga_carte(self, carte):
        self.carti.append(carte)

    def adauga_autor(self, autor):
        self.autori.append(autor)

    def cauta_carte_titlu(self,titlu):
        carti_gasite = []

        for carte in self.carti:
            if titlu.lower() in carte.titlu.lower():
                carti_gasite.append(carte)

        return carti_gasite
        
    def cauta_carte_autor(self, autor):
        carti_gasite = []

        for carte in self.carti:
            if autor.lower() in carte.autor.lower():
                carti_gasite.append(carte)
            
        return carti_gasite
    
    def sterge_carte_dupa_titlu(self, titlu):
        carti_dupa_stergere = []

        for carte in self.carti:
            if carte.titlu.lower() != titlu.lower():
                carti_dupa_stergere.append(carte)
        self.carti = carti_dupa_stergere

    def stergere_carte_dupa_autor(self, autor):
        carti_dupa_stergere = []

        for carte in self.carti:
            if carte.autor.lower() != autor.lower():
                carti_dupa_stergere.append(carte)
        self.carti = carti_dupa_stergere

# Scriere si citire din fisier
    
    def incarca_carti_din_fisier(self, nume_fisier):
        if not nume_fisier.endswith('.json'):
            nume_fisier += '.json'

        if not os.path.exists(nume_fisier):
            print(f"Fisierul '{nume_fisier}' nu exista. Se va crea automat la salvare.")
            return

        try:
            with open(nume_fisier, 'r') as f:
                carti_json = json.load(f)
                for carte in carti_json:
                    self.adauga_carte(Carte(**carte))
        except json.JSONDecodeError:
            print(f"Eroare: Fisierul '{nume_fisier}' contine date invalide.")
        except Exception as e:
            print(f'Eroare la incarcarea cartilor: {str(e)}')

    def salveaza_carti_in_fisier(self, nume_fisier):
        if not nume_fisier.endswith('.json'):
            nume_fisier += '.json'

        try:
            with open(nume_fisier, "w") as f:
                carti_json = [carte.__dict__ for carte in self.carti]
                json.dump(carti_json, f, indent=4)
        except Exception as e:
            print(f"Eroare la salvarea cartilor in fisier: {str(e)}")
        
# Aplicare decorator pentru logarea actiunilor
@logare_actiuni
    
def logare():
        print("Actiunea a fost logata in fisier cu succes")