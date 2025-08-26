class Classe:
    def __init__(self, nome, dado_vida, requisitos, habilidades):
        self.nome = nome
        self.dado_vida = dado_vida
        self.requisitos = requisitos
        self.habilidades = habilidades

    def __str__(self):
        return (f"Classe: {self.nome}\n"
                f"Dado de Vida: d{self.dado_vida}\n"
                f"Requisitos: {self.requisitos}\n"
                f"Habilidades: {', '.join(self.habilidades)}")


class Guerreiro(Classe):
    def __init__(self):
        super().__init__("Guerreiro", dado_vida=8,
                         requisitos={"Força": 9},
                         habilidades=["Uso de todas as armas", "Acesso a todas as armaduras"])


class Clerigo(Classe):
    def __init__(self):
        super().__init__("Clérigo", dado_vida=6,
                         requisitos={"Sabedoria": 9},
                         habilidades=["Uso de magias divinas", "Expulsar mortos-vivos"])


class Mago(Classe):
    def __init__(self):
        super().__init__("Mago", dado_vida=4,
                         requisitos={"Inteligência": 9},
                         habilidades=["Uso de magias arcanas", "Conhecimento de pergaminhos"])
