#funcao retorna o dobro
def dobro(x):
  return x*2

#lista
value = [1, 2, 3, 4, 5, 6]

#variavel com map
doubled_value = map(dobro, value)

#laco imprimindo
for v in doubled_value:
  print(v)
