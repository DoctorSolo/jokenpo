from src.Jokenpo import Jokenpo
import src.Jokenpo as Jokenpo

def Joga(a: Jokenpo, b: Jokenpo):
    Opt = [Jokenpo.Pedra, Jokenpo.Papel, Jokenpo.Tesoura]
    
    try:
        a_is = Opt.index(a)
        
        if (b == Opt[a_is-1]):
            print(f"Voce {a} ganhou de {b}")
        elif(b == Opt[a_is-2]):
            print(f"Voce {a} perdeu para {b}")
        elif(b == a):
            print("Empada")
        else:
            raise Exception("Esse erro não era para aparecer")
            
    except:
        print("Isso não é pedra, papel e tesoura bexta")