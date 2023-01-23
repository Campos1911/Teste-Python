print("\n\n\tHello, World\n")

#Isso aqui é um comentário

#Variáveis
a = 19
b = "Anthoni"

#Printando variáveis
print(a)
print(b)

#Descobrindo o tipo das variáveis
print(type(a))
print(type(b))
print("\n")

#Muitos valores em uma variável

carros = ["volvo", "mercedes", "chevrolet"]
x, y, z = carros

print(x)
print(y)
print(z)
print("\n")

#Imprimir variáveis inteiras

t = "Anthoni tem 19 anos"
print(t)
print("\n")

#Funções

o = "Isso é um teste de funções"

def func():
    print("Testando a variável: " + o)
func()
print("\n")

#Tipos de números

r = 1 #Int
rr = 2.2 #Float
rrr = 3j #Complexo

print(type(r))
print(type(rr))
print(type(rrr))

#Strings de várias linhas

p = '''Ola, isso aqui é um teste
feito em python.'''

print("\n")
print(p)

#Desmembrando uma string

print("\n")
for x in "banana":
    print(x)

#Testando se algo está na string

print("\n")
pp = "O sol está nascendo no horizonte"
print("horizonte" in pp)

print("\n")
if "sol" in pp:
    print("'Sol' está presente")