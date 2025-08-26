from Atributos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from Raças import Humano, Anao, Elfo, Halfling
from Classes import Guerreiro, Clerigo, Mago
from Personagem import Personagem

def escolher_estilo():
    print("\nEscolha um estilo de distribuição de atributos:")
    print("1 - Estilo Clássico (3d6)")
    print("2 - Estilo Aventureiro (4d6, descarta o menor)")
    print("3 - Estilo Heróico (Distribuir 72 pontos)")
    escolha = input("Digite o número do estilo desejado: ")
    estilos = {
        '1': EstiloClassico(),
        '2': EstiloAventureiro(),
        '3': EstiloHeroico()
    }
    return estilos[escolha].distribuir()

def escolher_raca():
    print("\nEscolha a raça do personagem:")
    print("1 - Humano")
    print("2 - Anão")
    print("3 - Elfo")
    print("4 - Halfling")
    escolha = input("Digite o número da raça desejada: ")
    racas = {
        '1': Humano(),
        '2': Anao(),
        '3': Elfo(),
        '4': Halfling()
    }
    return racas[escolha]

def escolher_classe(atributos):
    print("\nEscolha a classe do personagem:")
    print("1 - Guerreiro (Requisito: Força 9+)")
    print("2 - Clérigo (Requisito: Sabedoria 9+)")
    print("3 - Mago (Requisito: Inteligência 9+)")
    while True:
        escolha = input("Digite o número da classe desejada: ")
        classes = {
            '1': Guerreiro(),
            '2': Clerigo(),
            '3': Mago()
        }
        classe = classes.get(escolha)
        if classe:
            valido = True
            for atributo, minimo in classe.requisitos.items():
                if atributos.valores[atributo] < minimo:
                    print(f"\nRequisito não atendido para {classe.nome}: "
                          f"{atributo} precisa ser {minimo}+ (você tem {atributos.valores[atributo]})")
                    valido = False
                    break
            if valido:
                return classe
        else:
            print("Opção inválida.")

def main():
    nome = input("Digite o nome do personagem: ")
    atributos = escolher_estilo()
    print("\n--- Atributos Gerados ---")
    print(atributos)
    raca = escolher_raca()
    classe = escolher_classe(atributos)
    personagem = Personagem(nome, atributos, raca, classe)
    print("\n--- Personagem Criado ---")
    print(personagem)

if __name__ == "__main__":
    main()
