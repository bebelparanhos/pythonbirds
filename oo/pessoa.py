class Pessoa:
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    alex = Pessoa(nome='Alex')
    eduarda = Pessoa(nome='Eduarda')
    isabel = Pessoa(eduarda, alex, nome='Isabel')

    print(isabel.cumprimentar())
    print(isabel.nome)
    print(isabel.idade)

    for filho in isabel.filhos:
        print(filho.nome)

