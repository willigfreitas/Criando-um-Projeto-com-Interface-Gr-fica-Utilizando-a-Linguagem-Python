#Para isso, é preciso criar métodos para
 #aumentar/diminuir volume, trocar e sintonizar um novo canal, 
#adicionando um novo canal à lista (somente se esse canal não estiver nessa lista). 
#No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.

class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizaCanal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv  # Atribui a TV ao controle remoto

    def aumentaVolume(self):
        self.tv.aumentaVolume(90)  # Aumenta o volume da TV em 90 unidades

    def diminuiVolume(self):
        self.tv.diminuiVolume(90)  # Diminui o volume da TV em 90 unidades

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)  # Troca o canal da TV para o canal fornecido

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)  # Sintoniza um novo canal na TV

