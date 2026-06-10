# PDA — Reconhecedor de blocos BEGIN/END aninhados
# Linguagem: { BEGIN^n END^n | n >= 1 }

ESTADOS       = {'q_lendo', 'q_rej'}
ALFABETO      = {'BEGIN', 'END'}
ALFABETO_PILHA = {'B'}
ESTADO_INICIAL = 'q_lendo'
ESTADOS_FINAIS = {'q_lendo'}
MARCADOR       = 'B'

# Tabela de transição: (estado, símbolo, topo_pilha) → (novo_estado, ação_pilha)
# topo_pilha : None = pilha vazia | MARCADOR = marcador no topo
# ação_pilha : 'push' empilha MARCADOR | 'pop' desempilha | None sem alteração
TRANSICOES: dict[tuple, tuple] = {
    ('q_lendo', 'BEGIN', None):     ('q_lendo', 'push'),
    ('q_lendo', 'BEGIN', MARCADOR): ('q_lendo', 'push'),
    ('q_lendo', 'END',   MARCADOR): ('q_lendo', 'pop'),
    ('q_lendo', 'END',   None):     ('q_rej',   None),
}


def extrair_palavras(texto: str) -> list[str]:
    return texto.upper().split()


def pda(entrada: list[str]) -> str:
    if not entrada:
        return "Linguagem não Aceita - entrada vazia"

    estado = ESTADO_INICIAL
    pilha: list[str] = []

    for simbolo in entrada:
        if simbolo not in ALFABETO:
            print(f"  '{simbolo}' > símbolo fora do alfabeto")
            return "Linguagem não Aceita"

        topo = pilha[-1] if pilha else None
        transicao = TRANSICOES.get((estado, simbolo, topo))

        if transicao is None:
            print(f"  {simbolo} > transição não definida: ({estado}, {simbolo}, {topo or '∅'})")
            return "Linguagem não Aceita"

        estado, acao = transicao

        if acao == 'push':
            pilha.append(MARCADOR)
            print(f"  {simbolo:<6} > empilha    | pilha: {pilha}")
        elif acao == 'pop':
            pilha.pop()
            print(f"  {simbolo:<6} > desempilha | pilha: {pilha}")
        else:
            print(f"  {simbolo:<6} > pilha vazia! END sem BEGIN correspondente")

        if estado not in ESTADOS_FINAIS:
            return "Linguagem não Aceita"

    if not pilha:
        return "Linguagem Aceita"

    print(f"  Fim da entrada com pilha não vazia: {len(pilha)} BEGIN(s) sem END")
    return "Linguagem não Aceita"


def main():
    entrada = extrair_palavras(input("Insira uma string: "))
    print()
    resultado = pda(entrada)
    print(f"\n> {resultado}")


if __name__ == '__main__':
    main()
