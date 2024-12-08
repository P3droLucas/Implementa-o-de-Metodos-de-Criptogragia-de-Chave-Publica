import random

# Está função gera uma chave privada aleatória entre 2 e prime-2
## prime =  é um número primo pequeno usado para simplificação

def gerando_chave_privada(prime):
    return random.randint(2, prime - 2)

# Está função gera uma chave pública usando a fórmula /text{base}^{/text{private_key}}/mod/text{prime}
## base =  é um número base pequeno usado para simplificação
### As barras dos comentários estão todas invertidas.
def gerando_chave_publica(prime, base, chave_privada):
    return pow(base, chave_privada, prime)

# Está função gera o segredo compartilhado usando a fórmula /text{public_key}^{/text{private_key}}/mod/text{prime}.
## As barras dos comentários estão todas inveridas.
def gerando_segredo_compartilhado(prime, chave_publica, chave_privada):
    return pow(chave_publica, chave_privada, prime)

# Parâmetros simplificados
prime = 23  # Número primo pequeno para simplificação
base = 5    # Base

# Chaves privadas
## São geradas aleatoriamente.
chave_privada_A = gerando_chave_privada(prime)
chave_privada_B = gerando_chave_privada(prime)

# Chaves públicas
## São calculadas a partir das chaves privadas
chave_publica_A = gerando_chave_publica(prime, base, chave_privada_A)
chave_publica_B = gerando_chave_publica(prime, base, chave_privada_B)

# Segredo compartilhado
## segredo_compartilhado_A e segredo_compartilhado_B são calculados e devem ser iguais se o algoritmo estiver correto. 
segredo_compartilhado_A = gerando_segredo_compartilhado(prime, chave_publica_B, chave_privada_A)
segredo_compartilhado_B = gerando_segredo_compartilhado(prime, chave_publica_A, chave_privada_B)

print(f"O segredo compartilhado A: {segredo_compartilhado_A}")
print(f"O segredo compartilhado B: {segredo_compartilhado_B}")

