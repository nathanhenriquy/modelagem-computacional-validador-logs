# linguagem recursiva

alfabeto = ['OPEN', 'COMMIT', 'CLOSE']

def extrair_palavras(texto: str) -> list[str]:
    texto = texto.upper()
    return texto.split()
