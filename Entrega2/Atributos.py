import random

class Atributos:
    def __init__(self, forca=0, destreza=0, constituicao=0, inteligencia=0, sabedoria=0, carisma=0):
        self.valores = {
            'Força': forca,
            'Destreza': destreza,
            'Constituição': constituicao,
            'Inteligência': inteligencia,
            'Sabedoria': sabedoria,
            'Carisma': carisma
        }

    def __str__(self):
        return '\n'.join([f"{chave}: {valor}" for chave, valor in self.valores.items()])

    def distribuir(self, lista_valores):
        if len(lista_valores) != 6:
            raise ValueError("São necessários exatamente 6 valores.")
        for i, chave in enumerate(self.valores):
            self.valores[chave] = lista_valores[i]


class DistribuidorAtributos:
    def distribuir(self):
        raise NotImplementedError


class EstiloClassico(DistribuidorAtributos):
    def distribuir(self):
        return Atributos(*[self.rolar_3d6() for _ in range(6)])

    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3))


class EstiloAventureiro(DistribuidorAtributos):
    def distribuir(self):
        return Atributos(*[self.rolar_4d6_descartar_menor() for _ in range(6)])

    def rolar_4d6_descartar_menor(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)


class EstiloHeroico(DistribuidorAtributos):
    def distribuir(self):
        pontos_totais = 72
        atributos = []
        print("Você tem 72 pontos para distribuir entre os 6 atributos.")
        print("Cada atributo deve ter no mínimo 3 e no máximo 18 pontos.")
        for nome in ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']:
            while True:
                try:
                    restante = pontos_totais - sum(atributos)
                    valor = int(input(f"Digite o valor para {nome} (Restante: {restante}): "))
                    if 3 <= valor <= 18 and sum(atributos) + valor <= 72:
                        atributos.append(valor)
                        break
                    else:
                        print("Valor inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        return Atributos(*atributos)
