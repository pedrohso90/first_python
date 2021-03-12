from functools import reduce

#funcao soma
def soma(x, y):
  return x+y

#lista
lista = [1, 2, 4, 6, 50]

#usando função reduce para retornar soma dos valores da lista
soma = reduce(soma, lista)

#imprimindo soma
print(soma)
