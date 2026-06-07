
# calculadora.py

  
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números.

    Se o segundo número for zero, o Python irá gerar um erro.
    """
    return a / b

def potencia(a, b):
    """Retorna a base elevada ao expoente."""
    return a ** b

def calcular_media(lista):
    """Retorna a média dos números de uma lista.
    Gera um erro se a lista estiver vazia.
    """
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia")
    
    return sum(lista) / len(lista)
