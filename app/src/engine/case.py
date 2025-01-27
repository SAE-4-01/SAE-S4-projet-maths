class Case:
    def __init__(self, caratere: str):
        self.caractere = caratere

    def get_caractere(self):
        return self.caractere

    def __str__(self):
        return self.caractere

class Depart(Case):
    def __init__(self):
        super().__init__("D")
class Arrive(Case):
    def __init__(self):
        super().__init__("A")
class Rond(Case):
    def __init__(self):
        super().__init__("O")
class Croix(Case):
    def __init__(self):
        super().__init__("X")
class Point(Case):
    def __init__(self):
        super().__init__(".")
class Etoile(Case):
    def __init__(self):
        super().__init__("*")