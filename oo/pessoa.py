class Pessoa:
    #atributo de classe
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome

        #atributos complexos
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

    #atributos dinamicos
    isabel.sobrenome = 'Paranhos'
    print(isabel.sobrenome)

    print(isabel.__dict__)
    print(alex.__dict__)

    del isabel.sobrenome
    print(isabel.__dict__)

    print(Pessoa.olhos)
    print(isabel.olhos)
    print(alex.olhos)