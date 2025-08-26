class Personagem:
    def __init__(self, nome, atributos, raca, classe):
        self.nome = nome
        self.atributos = atributos
        self.raca = raca
        self.classe = classe

    def __str__(self):
        return (f"Personagem: {self.nome}\n"
                f"{self.atributos}\n\n"
                f"{self.raca}\n\n"
                f"{self.classe}")
