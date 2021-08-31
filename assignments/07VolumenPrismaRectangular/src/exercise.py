def area(bas, alt):
    return (bas*alt)/2
     
def volumen(ar, prof):
    return ar*prof
    


def main():
    #escribe tu código abajo de esta línea
    base=float(input('Dame la base '))
    altura=float(input('Dame la altura '))
    profundidad=float(input('Dame la profundiad '))
    aria=area(base, altura)
    vol=volumen(aria, profundidad)
    print('El volumen del prisma es: '+str(vol))


    pass

if __name__=='__main__':
    main()
