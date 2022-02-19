import math

def delta(a,b,c):
    delta = b**2 -4*a*c
    if (delta > 0):
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2
    elif (delta == 0):
        x1 = -b/(2*a)
        return x1
    else:
        return 'Não há raízes dentro do conjunto de número reais'
    
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

resposta = delta(a,b,c)
print(' ### solução da equação ### \n')
print(resposta)