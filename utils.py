from functools import reduce

# Afiseaza detalii carte
def afiseaza_carte(carti):
    print("--- Lista Carti ---")
    for carte in carti:
        print(f"Titlu: {carte.titlu}, Gen: {carte.gen}, An: {carte.an_publicare}, Autor: {carte.autor}, Rating: {carte.rating}")

# Map: 
def afiseaza_titlu(carti):
    titluri = map(lambda carte: carte.titlu.upper(), carti)
    for t in titluri:
        print(t)

# Filter
def filtrare_carti(carti):
    return list(filter(lambda carte: carte.an_publicare > 2000 and carte.rating > 4.0, carti))

# Reduce
def rating_mediu(carti):
    if not carti:
        return 0.0
    total = reduce(lambda x, y: x + y.rating, carti, 0)
    return total / len(carti)

# Comprehension
def titluri_carti_autori_nationalitate(carti, autori, nationalitate):
    return [
        carte.titlu
        for carte in carti
        if any(
            autor.nationalitate.lower() == nationalitate.lower()
            for autor in autori
            if autor.nume.lower() in carte.autor.lower()
        )
    ]
