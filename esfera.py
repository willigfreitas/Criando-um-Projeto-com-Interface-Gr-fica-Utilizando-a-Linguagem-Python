import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    
    def volume(self):
        vol = (4 / 3) * math.pi * (self.raio ** 3)
        return vol
    
    def area(self):
        ar = 4 * math.pi * (self.raio ** 2)
        return ar

bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)

print(f'O volume da bola 1 é {bola1.volume()} cm^3')
print(f'A área superficial da bola 1 é {bola1.area()} cm^2')

print(bola1.volume())  # Retorna o volume da bola1
print(Esfera.volume(bola1))  # Alternativamente, retorna o volume da bola1 usando a classe diretamente
