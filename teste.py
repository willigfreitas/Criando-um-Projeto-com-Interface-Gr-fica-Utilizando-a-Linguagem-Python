from funcionalidades import *

tv = Televisor('SONY', 'SONY-123')  # Cria uma instância de Televisor com a marca 'SONY' e modelo 'SONY-123'
controle = ControleRemoto(tv)  # Cria uma instância de ControleRemoto associada à TV criada

controle.sintonizaCanal('SBT')  # Sintoniza o canal 'SBT' usando o controle remoto
controle.trocaCanal('SBT')  # Troca o canal atual para 'SBT' usando o controle remoto

print(tv.canal_atual)  # Imprime o canal atual da TV
