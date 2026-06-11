# PDA — Reconhecedor de blocos BEGIN/END aninhados

import sys
from time import sleep

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
    passos = 0

    if not entrada:
        return "Linguagem não Aceita - entrada vazia", passos

    estado = ESTADO_INICIAL
    pilha: list[str] = []
    

    for simbolo in entrada:
        if simbolo not in ALFABETO:
            print(f"  '{simbolo}' > símbolo fora do alfabeto")
            return "Linguagem não Aceita", passos

        topo = pilha[-1] if pilha else None
        transicao = TRANSICOES.get((estado, simbolo, topo))

        if transicao is None:
            print(f"  {simbolo} > transição não definida: ({estado}, {simbolo}, {topo or '∅'})")
            return "Linguagem não Aceita", passos

        estado, acao = transicao

        passos += 1

        if acao == 'push':
            pilha.append(MARCADOR)
            print(f"  {simbolo:<6} > empilha    | pilha: {pilha}")
        elif acao == 'pop':
            pilha.pop()
            print(f"  {simbolo:<6} > desempilha | pilha: {pilha}")
        else:
            print(f"  {simbolo:<6} > pilha vazia! END sem BEGIN correspondente")

        if estado not in ESTADOS_FINAIS:
            return "Linguagem não Aceita", passos

    if not pilha:
        return "Linguagem Aceita", passos

    print(f"  Fim da entrada com pilha não vazia: {len(pilha)} BEGIN(s) sem END")
    return "Linguagem não Aceita", passos


def main_llc():
    if len(sys.argv) > 1:
        entrada = ' '.join(sys.argv[1:])
        print(f"\nEntrada: {entrada}\n")
        resultado, passos = pda(extrair_palavras(entrada))
        print(f"\nResultado: {resultado}")
        print(f"Passos executados: {passos}")
        return

    with open('testes/testes_livre_contexto.txt', 'r') as entradas:
        linha = 1
        n_entrada = 1

        for entrada in entradas:
            if linha % 2 != 0:
                print(f"\nEntrada {n_entrada}:\n")

                resultado, passos = pda(extrair_palavras(entrada))

                print(f"\nResultado: {resultado}")
                print(f"Passos executados: {passos}")

                n_entrada += 1

            elif linha % 2 == 0:
                if entrada.strip() == '1':
                    print("Esperado: Linguaguem aceita\n\n")
                elif entrada.strip() == '0':
                    print("Esperado: Linguaguem não aceita\n\n")

                sleep(0.5)

            linha += 1


if __name__ == '__main__':
    main_llc()
