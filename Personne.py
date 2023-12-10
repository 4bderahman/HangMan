from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, code, nom, prenom, age):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age

    @abstractmethod
    def get_code(self):
        pass

    @abstractmethod
    def get_nom(self):
        pass

    @abstractmethod
    def get_prenom(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, autre):
        return self._code == autre.get_code() if isinstance(autre, Personne) else False

class Employe(Personne):
    employe_count = 0

    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        self._grade = grade
        Employe.employe_count += 1

    def get_code(self):
        return self._code

    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_age(self):
        return self._age

    def __str__(self):
        return f'Code: {self._code}, Nom: {self._nom}, Prénom: {self._prenom}, Âge: {self._age}, Grade: {self._grade}'

    def __eq__(self, autre):
        return super().__eq__(autre)

class Eleve(Personne):
    eleve_count = 0

    def __init__(self, code, nom, prenom, age, niveau, moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau = niveau
        self._moyenne = moyenne
        Eleve.eleve_count += 1

    def get_code(self):
        return self._code

    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_age(self):
        return self._age

    def __str__(self):
        return f'Code: {self._code}, Nom: {self._nom}, Prénom: {self._prenom}, Âge: {self._age}, Niveau: {self._niveau}, Moyenne: {self._moyenne}'

    def __eq__(self, autre):
        return super().__eq__(autre)

# Test Program
employe1 = Employe(7, "wa2il", "appah", 40, "Chef")

eleve1 = Eleve(10, "spiko", "miko", 18, "Débutant", 75.0)


print("Liste des employés:")
print(employe1)


print("\nListe des élèves:")
print(eleve1)


print(f'\nNombre total des classes créés: {Employe.employe_count + Eleve.eleve_count}')
print(f'\nNombre total d\'employés créés: {Employe.employe_count}')
print(f'Nombre total d\'élèves créés: {Eleve.eleve_count}')
