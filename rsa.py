import random
from sympy import isprime, randprime

# Está função gera um número primo aleatório de um determinado comprimento.
## length = é o tamanho do número primo em bits. 
def gerando_numeros_primos_aleatoriamente(length):
    return randprime(2**(length-1), 2**length)

# Está função gera um par de chaves (publica e privada).
## "p" e "q" são números primos gerados aleatoriamente. 
## "n" é o produto de "p" e "q".
## "phi" é o totiente de Euler de "n".
## "e" é o expoente privado calculado como o inverso modular de e em relação a phi.

def gerando_par_de_chaves(length):
    p = gerando_numeros_primos_aleatoriamente(length)
    q = gerando_numeros_primos_aleatoriamente(length)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Exponente público comum
    d = pow(e, -1, phi)
    
    return ((e, n), (d, n))

# Está função criptografa uma mensagem de texto plano usando a chave pública.
## Cada caractere da mensagem é elevado à potência "e" e tomado o módulo "n".
def criptografando(chave_publica, texto_simples):
    e, n = chave_publica
    return [pow(ord(char), e, n) for char in texto_simples]

# Está função descripta uma mensagem cifrada usando a chave privada.
## Cada caractere cifrado é elevado à potência "d" e tomado o módulo "n"
def desencriptando(chave_privada, texto_cifrado):
    d, n = chave_privada
    return ''.join([chr(pow(char, d, n)) for char in texto_cifrado])

# "chave_publica" e "chave_privada" são geradas com um comprimento de 8 bits para simplificação
# Geração de chaves
chave_publica, chave_privada = gerando_par_de_chaves(8)  # Tamanho de chave pequeno para simplificação

# Mensagem
texto_puro = "Professor Wewerton, implementacao realizada com sucesso"

# Criptografia
mensagem_criptografada = criptografando(chave_publica, texto_puro)
print(f"Mensagem criptografada: {mensagem_criptografada}")

# Descriptografia
mensagem_desencriptografada = desencriptando(chave_privada, mensagem_criptografada)
print(f"Mensagem descriptografada: {mensagem_desencriptografada}")
