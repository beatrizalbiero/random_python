'''
Calculo lambda
'''

def adder(x):
    return lambda y: x + y
add5 = adder(5)
add5(1)

add5(2)
add3 = adder(3)
add3(8)
add3(10)

seq = range(8)
print(seq)

lista = [1,2,3,4]

def quadrado(x):
    return lambda y: x**2

lista_map = map(quadrado,lista)

print(lista_map)
print(lista)

'''
in lista
'''

#lista = ['bota','leilao',['sabor']]
#sabor = 'sabor'
#for item in lista:
    #print(item)

#lista[0]

'''
matrix
'''
import numpy as np
a = np.matrix('1 2; 3 4')
print(a.shape)

'''
filtro
'''
from itertools import compress
list_a = ['abc', 2, 4, 6]
fil = [True, False, True, False]
list(compress(list_a, fil))

'''
Caso ocorra uma alteração em um modulo importado em outro arquivo:
-> import importlib
-> importlib.reload(modulo desatualizado)
'''


a = 27
id(a)



def testifelse(x):
    if x[0] == 0:
        if x[1] == 1:
            print("x0 = 0 e x1 = 1")
        else:
            print("x0 = 0 e x1 != 1")
    else:
        print("x0 != 0")
    pass

x = [0,1]
y = [1,0]
z = [0,0]
testifelse(x)
testifelse(y)
testifelse(z)
position = 3
if position not in range(0,2):
    print("position must be an integer between 0 and 2")



def g(x):
  y0 = x + 1
  y1 = x * 3
  y2 = y0 ** y1
  return {'y0':y0, 'y1':y1 ,'y2':y2 }
g(0)['y0']

g(0)
