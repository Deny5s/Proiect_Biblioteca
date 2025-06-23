import datetime
from functools import wraps
from functools import reduce
import json
import os


# Clasa Carte

class Carte:
    def __init__ (self, titlu, gen, an_publicare, autor, rating):
        self.titlu = titlu
        self.gen = gen
        self.an_publicare = an_publicare 
        self.autor = autor
        self.rating = rating

# Clasa Autor

class Autor:
    def __init__(self, nume, prenume, nationalitate):
        self.nume = nume
        self.prenume = prenume
        self.nationalitate = nationalitate

#Creeaza un decorator pentru logarea actiunilor in fisier(log.txt)

def logare_actiuni(functie):
    def wrapper(*args, **kwargs):
        # Colectare data si ora curenta
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Linie log
        linie_log = f"[{timestamp}] Functia '{functie.__name__}' a fost apelata\n"
        
        # Deschidere fisier
        with open("log.txt", "a") as f:
            f.write(linie_log)
        
        return functie(*args, **kwargs)
    
    return wrapper


# Clasa biblioteca

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
        
# Aplicare decorator pentru logarea actiunilor
    @logare_actiuni
    
    def logare():
        print("Actiunea a fost logata in fisier cu succes")
        
    for _ in range(3):
        logare()


    def biblioteca():
        print("Sunt in functia biblioteca()")

    #Map
    
    def afiseaza_carte(self):
        print("--- Lista Carti ---")
        for carte in self.carti:
            titluri_carti = map(lambda carte: carte.titlu.upper(), self.carti)
            print(f"Titlu: {carte.titlu}, Gen: {carte.gen}, An Publicare: {carte.an_publicare}, Autor: {carte.autor}, Rating: {carte.rating}")
    
    # Filter

    def filtrare_carti(self):
        carti_filtrate = filter(lambda carte: carte.an_publicare > 2000 and carte.rating > 4.0, self.carti)
        return list(carti_filtrate)
    
    #Reduce 
    
    def rating_mediu(self):
        if not self.carti:
            return 0.0
        
        total_rating = reduce(lambda x, y: x + y.rating, self.carti, 0)
        return total_rating / len(self.carti)
    
    # Comprehension

    def titluri_carti_autori_nationalitate(self, nationalitate):
        return [carte.titlu for carte in self.carti if any(autor.nationalitate.lower() == nationalitate.lower () for autor in self.autori if autor.nume.lower() in carte.autor.lower())]
    
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


    def meniu(self):
        while True:
            print("\n --- Meniu Biblioteca ---")
            print("1. Adauga carte")
            print("2. Adauga autor")
            print("3. Cauta carte dupa titlu")
            print("4. Cauta carte dupa autor")
            print("5. Sterge carte dupa titlu")
            print("6. Sterge carte dupa autor")
            print("7. Afiseaza carti")
            print("8. Filtreaza carti")
            print("9. Calculeaza rating mediu")
            print("10. Titluri carti dupa nationalitate autor")
            print("11. Incarca fisier")
            print("12. Salveaza carti in fisier")
            print("13. Iesire")

            opt = int(input("Alege optiunea: "))
            if opt == 1:
                titlu = input("Titlu carte: ")
                gen = input("Gen carte: ")
                an_publicare = int(input("An publicare: "))
                autor = input("Autor carte: ")
                rating = float(input("Rating carte: "))
                self.adauga_carte(Carte(titlu, gen, an_publicare, autor, rating))
            elif opt == 2:
                nume = input("Nume autor: ")
                prenume = input("Prenume autor: ")
                nationalitate = input("Nationalitate autor: ")
                self.adauga_autor(Autor(nume, prenume, nationalitate))
            elif opt == 3:
                titlu = input("Titlu carte cautata: ")
                carti_gasite = self.cauta_carte_titlu(titlu)
                if carti_gasite:
                    print("Carti gasite:")
                    for carte in carti_gasite:
                        print(carte.titlu)
                else:
                    print("Nu s-au gasit carti cu acest titlu.")
            elif opt == 4:
                autor = input("Autor carte cautata: ")
                carti_gasite = self.cauta_carte_autor(autor)
                if carti_gasite:
                    print("Carti gasite:")
                    for carte in carti_gasite:
                        print(carte.titlu)
                else:
                    print("Nu s-au gasit carti cu acest autor.")
            elif opt == 5:
                titlu = input("Titlu carte de sters: ")
                self.sterge_carte_dupa_titlu(titlu)
                print(f"Cartea '{titlu}' a fost stearsa.")
            elif opt == 6:
                autor = input("Autor carte de sters: ")
                self.stergere_carte_dupa_autor(autor)
                print(f"Cartile scrise de '{autor}' au fost sterse.")
            elif opt == 7:
                self.afiseaza_carte()
            elif opt == 8:
                carti_filtrate = self.filtrare_carti()
                if carti_filtrate:
                    print("Carti filtrate:")
                    for carte in carti_filtrate:
                        print(carte.titlu)
                else:
                    print("Nu s-au gasit carti care sa indeplineasca criteriile de filtrare.")
            elif opt == 9:
                rating_mediu = self.rating_mediu()
                print(f"Rating mediu al cartilor: {rating_mediu:.2f}")
            elif opt == 10:
                nationalitate = input("Nationalitate autor: ")
                titluri = self.titluri_carti_autori_nationalitate(nationalitate)
                if titluri:
                    print("Titluri carti gasite:")
                    for titlu in titluri:
                        print(titlu)
                else:
                    print("Nu s-au gasit carti cu aceasta nationalitate.")
            elif opt == 11:
                nume_fisier = input("Nume fisier de incarcat: ")
                self.incarca_carti_din_fisier(nume_fisier)
                print(f"Cartile au fost incarcate din fisierul '{nume_fisier}'.")
            elif opt == 12:
                nume_fisier = input("Nume fisier pentru salvare: ")
                self.salveaza_carti_in_fisier(nume_fisier)
                print(f"Cartile au fost salvate in fisierul '{nume_fisier}'.")
            elif opt == 13:
                print("Iesire din aplicatie.")
                break
            else:
                print("Optiune invalida. Te rog sa alegi o optiune valida.")
        
# Creare instanta biblioteca si apelare meniu
biblioteca = Biblioteca()
biblioteca.meniu()













    

    




 








