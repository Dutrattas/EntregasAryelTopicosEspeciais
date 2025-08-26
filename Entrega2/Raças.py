class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

    def __str__(self):
        return (f"Raça: {self.nome}\n"
                f"Movimento: {self.movimento}\n"
                f"Infravisão: {self.infravisao}\n"
                f"Alinhamento: {self.alinhamento}\n"
                f"Habilidades: {', '.join(self.habilidades)}")


class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", movimento=9, infravisao="Nenhuma", alinhamento="Qualquer",
                         habilidades=["Versatilidade: ganha 10% XP adicional."])


class Anao(Raca):
    def __init__(self):
        super().__init__("Anão", movimento=6, infravisao="18m", alinhamento="Leal ou Neutro",
                         habilidades=["Detectar portas secretas", "Resistência a venenos"])


class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", movimento=9, infravisao="18m", alinhamento="Qualquer não caótico",
                         habilidades=["Uso de magia", "Visão aguçada"])

class Halfling(Raca):
    def __init__(self):
        super().__init__("Halfling", movimento=6, infravisao="Nenhuma", alinhamento="Neutro",
                         habilidades=["Dificil de tomar golpes", "Bom de mira"])
