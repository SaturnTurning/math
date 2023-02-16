#as funcoes agrupam linhas de código
import math

#introduzindo a funcao delta 
#da formula de baskara: -b mais ou menos 
#raiz quadrada b ao quadrado -4ac
#sobre 2a
#para teste, parametros a b c
# , 1 12 -13(196),2 -16 -18(400)
# 1 -1 -6(25)


def delta (a,b,c):
	return b ** 2 - 4*a*c

def teste_delta ():
    assert     delta(1, -1, -6) ==25


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprimeRaizes(a,b,c)

def imprimeRaizes(a,b,c):
    if delta(a,b,c) < 0:
        print("esta equação não possui raízes reais.")

    else:
        if delta == 0:
                raiz1 = (-b + math.sqrt(delta(a,b,c))) / (2 * a)
                print ('a raiz desta equação é', raiz1)
        else:
                raiz1 = (-b + math.sqrt(delta(a,b,c))) / (2 * a)
                raiz2 = (-b - math.sqrt(delta(a,b,c))) / (2 * a)
                if raiz1 < raiz2:
                        print('as raízes da equação são', raiz1, 'e', raiz2)
                else:
                        print('as raízes da equação são', raiz2, 'e', raiz1)

