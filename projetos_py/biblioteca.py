'''class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False


    def comer(self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f'{self.nome} foi comer')
                    self.comendo = True
                else:
                    print(f'{self.nome} não pode comer pq está dormindo')
            else:
                print(f'{self.nome} não pode comer pq está andando')
        else:
            print(f'{self.nome} já está comendo')


    def andar(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f'{self.nome} foi andar')
                    self.andando = True
                else:
                    print(f'{self.nome} não pode andar pq está dormindo')
            else:
                print(f'{self.nome} não pode andar pq está comendo')
        else:
            print(f'{self.nome} já está andando')

    def dormir(self):
        if self.dormindo == False:
            if self.andando == False:
                if self.comendo == False:
                    print(f'{self.nome} foi dormir')
                    self.dormindo = True
                else:
                    print(f'{self.nome} não pode dormir pq esta comendo')

            else:
                print(f'{self.nome} não pode dormir pq está andando')

        else:
            print(f'{self.nome} já está dormindo')'''



'''class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor


    def comer(self):
        print(f'{self.nome} foi comer')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'{self.nome} mia')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'{self.nome} lati')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f'{self.nome} mugi')


class Leao(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def rugir(self):
        print(f'{self.nome} rugi')

'''



class Atleta:
    def __init__(self, nome,peso):
        self.nome = nome
        self.peso = peso
        self.aquecido = False
        self.aposentado = False

    def aposentar(self):
        if self.aposentado == False:
            print(f'{self.nome} foi aposentado com sucesso!')
            self.aposentado = True
        else:
            print(f'{self.nome} não pode aposentar pq já esta na rede!')

    def aquecer(self):
        if self.aquecido == False:
            print(f'{self.nome} foi aquecer!')
            self.aquecido = True
        else:
            print(f'{self.nome} já esta aquecendo!')

class Nadador(Atleta):
    def nadar(self):
        if self.
class Corredor(Atleta):
class Ciclista(Atleta):
