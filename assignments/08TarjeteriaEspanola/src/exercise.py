
def maxi(pli, plu):
    if pli< plu:
        return pli*12
    
    elif plu<pli:
        return plu*35
         

def main():
    pliegos=int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones=int(input('Dame la cantidad de plumones '))
    tarjetas=maxi(pliegos, plumones)
    print('El número máximo de tarjetas que puedes hacer es: '+str(tarjetas))
    pass

if __name__=='__main__':
    main()
