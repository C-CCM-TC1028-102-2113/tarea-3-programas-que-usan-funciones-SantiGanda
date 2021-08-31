def check(a):
    if a%100==0 and a%400!=0 or a%4!=0:
        return 'No es bisiesto'
    elif a%4==0 and a%100!=0:
        return 'Es bisiesto'
    else:
        return 'Selecciona un valor apropiado'

def main():
    año=int(input('Dame un año: '))
    respuesta=check(año)
    print(respuesta)

    pass

if __name__=='__main__':
    main()

