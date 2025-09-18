'''
def soma_um(numero):
    return numero + 1

f1 = soma_um
print(f1(1))

'''
# 2 - Definindo funções dentro de outras funções
'''
def soma_um(numero):
    def adiciona_um(numero):
        return numero + 1
    return adiciona_um(numero=numero)

print(soma_um(4))
'''

#3 - Definindo funções dentro de outras funções
'''
def soma_um(numero):
    return numero + 1

def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)

print(function_call(soma_um))

'''

#4 - Funções retornando outras funções
'''
def funcao_ola():
    def diga_oi():
        return "Hi"
    return diga_oi

hello = funcao_ola()
print(hello())

'''
# Decorator


def decorador_maiusculo(function):
    def wrapper():
        func = function()
        cria_maiusculo = func.upper()
        return cria_maiusculo
    return wrapper

# def diga_oi():
#     return 'Hello there'

# funcao_decorada = decorador_maiusculo(diga_oi)
# print(funcao_decorada())

# Usando o decorador
'''
@decorador_maiusculo
def diga_oi():
    return 'Hello there'

print(diga_oi())

'''