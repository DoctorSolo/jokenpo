from random import randint

from src.Jokenpo import Jokenpo
import src.Jokenpo as Jokenpo
from src.Joga import Joga

Joke = [Jokenpo.Pedra, Jokenpo.Papel, Jokenpo.Tesoura]


while(True):
    Maquina = Joke[randint(0,2)]
    
    try:
        escolha_usuario = (int(input("Informe 1 para PEDRA, 2 para PAPEL e 3 para TESOURA: ")) - 1)
        if escolha_usuario not in [0, 1, 2]:
            raise Exception("Isso não é jokenpo")
        
        Usuario = Joke[escolha_usuario]
        print(Usuario)
    except:
        continue
    
    Joga(Usuario, Maquina)