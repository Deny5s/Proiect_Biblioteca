from biblioteca import Biblioteca
from models import Carte, Autor
from utils import afiseaza_titlu, filtrare_carti, rating_mediu, titluri_carti_autori_nationalitate

def meniu():
    biblioteca = Biblioteca()

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

        opt = input("Alege optiunea: ")
        if opt == "1":
            titlu = input("Titlu carte: ")
            gen = input("Gen carte: ")
            an_publicare = int(input("An publicare: "))
            autor = input("Autor carte: ")
            rating = float(input("Rating carte: "))
            biblioteca.adauga_carte(Carte(titlu, gen, an_publicare, autor, rating))
        elif opt == "2":
            nume = input("Nume autor: ")
            prenume = input("Prenume autor: ")
            nationalitate = input("Nationalitate autor: ")
            biblioteca.adauga_autor(Autor(nume, prenume, nationalitate))
        elif opt == "3":
            titlu = input("Titlu carte cautata: ")
            carti = biblioteca.cauta_carte_titlu(titlu)
            print("Carti gasite:" if carti else "Nimic gasit.")
            for c in carti:
                print(c.titlu)
        elif opt == "4":
            autor = input("Autor carte cautata: ")
            carti = biblioteca.cauta_carte_autor(autor)
            print("Carti gasite:" if carti else "Nimic gasit.")
            for c in carti:
                print(c.titlu)
        elif opt == "5":
            titlu = input("Titlu carte de sters: ")
            biblioteca.sterge_carte_dupa_titlu(titlu)
        elif opt == "6":
            autor = input("Autor carte de sters: ")
            biblioteca.stergere_carte_dupa_autor(autor)
        elif opt == "7":
            afiseaza_titlu(biblioteca.carti)
        elif opt == "8":
            filtrate = filtrare_carti(biblioteca.carti)
            for c in filtrate:
                print(c.titlu)
        elif opt == "9":
            print(f"Rating mediu: {rating_mediu(biblioteca.carti):.2f}")
        elif opt == "10":
            nat = input("Nationalitate autor: ")
            titluri = titluri_carti_autori_nationalitate(biblioteca.carti, biblioteca.autori, nat)
            for t in titluri:
                print(t)
        elif opt == "11":
            fisier = input("Nume fisier de incarcat: ")
            biblioteca.incarca_carti_din_fisier(fisier)
        elif opt == "12":
            fisier = input("Nume fisier pentru salvare: ")
            biblioteca.salveaza_carti_in_fisier(fisier)
        elif opt == "13":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")
