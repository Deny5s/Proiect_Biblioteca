

class Carte:
    def __init__ (self, titlu, gen, an_publicare, autor, rating):
        self.titlu = titlu
        self.gen = gen
        self.an_publicare = an_publicare 
        self.autor = autor
        self.rating = rating

class Autor:
    def __init__(self, nume, prenume, nationalitate):
        self.nume = nume
        self.prenume = prenume
        self.nationalitate = nationalitate