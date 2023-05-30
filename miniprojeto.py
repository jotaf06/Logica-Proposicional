import sympy

# Função que transforma uma sentença em outra logicamente equivalente
def transform(sentenca):
    nova_sentenca = sympy.simplify_logic(sentenca)
    return nova_sentenca

# Função que simplifica uma sentença até sua forma irredutível
def simplify(sentence):
    # Remove espaços em branco extras
    sentence = sentence.replace(" ", "")
    
    # Simplifica a sentença
    simplified = sentence.replace("(¬¬", "").replace("¬¬)", "")
    
    # Verifica se a sentença já está na sua forma mais irredutível
    if simplified == sentence:
        return "A sentença já está na forma mais irredutível."
    
    return simplified


# Exemplo de uso
sentenca = "(p & r) | (p & r)"
print("Sentença original: ", sentenca)
sentenca_equivalente = transform(sentenca)
print("Sentença logicamente equivalente simplificada: ", sentenca_equivalente)
