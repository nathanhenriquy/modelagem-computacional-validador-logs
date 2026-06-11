# DFA: LOGIN+ AUTH REQUEST* LOGOUT
# Alfabeto: {LOGIN, AUTH, REQUEST, LOGOUT}
#
# Estados:
#   0 = inicial
#   1 = após LOGIN (aceita mais LOGIN)
#   2 = após AUTH  (aceita REQUEST ou LOGOUT)
#   3 = após REQUEST (aceita mais REQUEST ou LOGOUT)
#   4 = após LOGOUT (estado de aceitação — final)
#   5 = estado morto (dead state — rejeição definitiva)
import sys
from time import sleep

alfabeto = ['LOGIN', 'AUTH', 'REQUEST', 'LOGOUT']

ESTADO_INICIAL = 0
ESTADOS_FINAIS = {4}
ESTADO_MORTO = 5

TRANSICOES = {
    (0, 'LOGIN'):   1,
    (0, 'AUTH'):    5,
    (0, 'REQUEST'): 5,
    (0, 'LOGOUT'):  5,

    (1, 'LOGIN'):   5,
    (1, 'AUTH'):    2,
    (1, 'REQUEST'): 5,
    (1, 'LOGOUT'):  5,

    (2, 'LOGIN'):   5,
    (2, 'AUTH'):    5,
    (2, 'REQUEST'): 3,
    (2, 'LOGOUT'):  4,

    (3, 'LOGIN'):   5,
    (3, 'AUTH'):    5,
    (3, 'REQUEST'): 3,
    (3, 'LOGOUT'):  4,

    (4, 'LOGIN'):   5,
    (4, 'AUTH'):    5,
    (4, 'REQUEST'): 5,
    (4, 'LOGOUT'):  5,
}

NOMES_ESTADOS = {
    0: 'inicial',
    1: 'LOGIN',
    2: 'AUTH',
    3: 'REQUEST',
    4: 'LOGOUT (aceito)',
    5: 'morto (rejeitado)',
}

def extrair_palavras(texto: str) -> list[str]:
    return texto.upper().split()


def dfa(entrada: list[str]) -> str:
    estado = ESTADO_INICIAL
    passos = 0

    for palavra in entrada:
        if palavra not in alfabeto:
            print(f"Simbolo {palavra} não existente")
            return "Linguagem não aceita"
        
        proximo = TRANSICOES.get((estado, palavra), ESTADO_MORTO)
        print(f"(q{estado} [{NOMES_ESTADOS[estado]}], {palavra}) > q{proximo} [{NOMES_ESTADOS[proximo]}]")
        estado = proximo
        passos += 1

        if estado == ESTADO_MORTO:
            break

    aceita = estado in ESTADOS_FINAIS

    print(f"\nPassos executados: {passos}")

    return "Linguagem aceita" if aceita else "Linguagem não aceita"


def main_regular():
    if len(sys.argv) > 1:
        entrada = ' '.join(sys.argv[1:])
        print(f"\nEntrada: {entrada}\n")
        resultado = dfa(extrair_palavras(entrada))
        print(f"Resultado: {resultado}")
        return

    with open('testes/testes_regular.txt', 'r') as entradas:
        linha = 1
        n_entrada = 1

        for entrada in entradas:
            if linha % 2 != 0:
                print(f"\nEntrada {n_entrada}:\n")

                resultado = dfa(extrair_palavras(entrada))
                print(f"Resultado: {resultado}")

                n_entrada += 1

            elif linha % 2 == 0:
                if entrada.strip() == '1':
                    print("Esperado: Linguaguem aceita\n\n")
                elif entrada.strip() == '0':
                    print("Esperado: Linguaguem não aceita\n\n")

                sleep(0.5)

            linha += 1
            


if '__main__' == __name__:
    main_regular()
