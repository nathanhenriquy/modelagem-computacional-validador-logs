# linguagem livre de contexto

alfabeto = ['BEGIN', 'END']

def extrair_palavras(texto: str) -> list[str]:
    texto = texto.upper()
    return texto.split()
