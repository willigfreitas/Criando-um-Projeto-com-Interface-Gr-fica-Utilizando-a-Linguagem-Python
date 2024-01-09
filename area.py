class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.a = lado_a
        self.b = lado_b
    
    def muda_valor(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b
    
    def retorna_lado(self):
        print(f'O Retângulo possui dimensões {self.a}m x {self.b}m')
    
    def area(self):
        return self.a * self.b

from area import Retangulo
import math

while True:
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite o outro lado do piso: "))
    piso = Retangulo(piso_a, piso_b)
    
    az_a = float(input("Digite o lado do azulejo: "))
    az_b = float(input("Digite o outro lado do azulejo: "))
    azulejo = Retangulo(az_a, az_b)
    
    area_piso = piso.area()
    area_az = azulejo.area()
    
    qntd_az = area_piso / area_az
    
    if area_piso % area_az == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qntd_az}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')
