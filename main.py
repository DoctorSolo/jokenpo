from random import SystemRandom

from src.Jokenpo import Jokenpo
import src.Jokenpo as Jokenpo
from src.Joga import Joga
from src.Opt import Opt as Joke

while(True):
    Maquina = Joke[SystemRandom.randint(0, 2)]
    
    try:
        escolha_usuario = (int(input("Informe 1 para PEDRA, 2 para PAPEL e 3 para TESOURA: ")) - 1)
        if escolha_usuario not in [0, 1, 2]:
            raise Exception()
        
        Usuario = Joke[escolha_usuario]
        print(Usuario)
    except:
        continue
    
    Joga(Usuario, Maquina)