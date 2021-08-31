def area(bas, alt):
    return bas*alt

def main():
    base=float(input('Dame la base: '))
    altura= float(input('Dame la altura: '))
    resultado=area(base, altura)
    print('El área del rectángulo es: '+str(resultado))
    pass

if __name__=='__main__':
    main()
