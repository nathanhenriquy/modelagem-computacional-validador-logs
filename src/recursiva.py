import sys
from time import sleep

VAZIO = '_'

ALFABETO_ENTRADA = {'OPEN', 'COMMIT', 'CLOSE'}
ALFABETO_FITA     = {'OPEN', 'COMMIT', 'CLOSE', 'X', 'Y', 'Z', VAZIO}

ESTADO_INICIAL = 'q0'
ESTADOS_FINAIS = {'q_aceita'}
ESTADO_REJEITA = 'q_rej'


TRANSICOES: dict[tuple, tuple] = {

    ('q0', 'X'):      ('q0', 'X', 'D'),
    ('q0', 'OPEN'):   ('q1', 'X', 'D'),
    ('q0', 'Y'):      ('q4', 'Y', 'D'),

    ('q1', 'OPEN'):   ('q1', 'OPEN', 'D'),
    ('q1', 'Y'):      ('q1', 'Y', 'D'),
    ('q1', 'COMMIT'): ('q2', 'Y', 'D'),

    ('q2', 'COMMIT'): ('q2', 'COMMIT', 'D'),
    ('q2', 'Z'):      ('q2', 'Z', 'D'),
    ('q2', 'CLOSE'):  ('q3', 'Z', 'E'),

    ('q3', 'OPEN'):   ('q3', 'OPEN', 'E'),
    ('q3', 'COMMIT'): ('q3', 'COMMIT', 'E'),
    ('q3', 'Y'):      ('q3', 'Y', 'E'),
    ('q3', 'Z'):      ('q3', 'Z', 'E'),
    ('q3', 'X'):      ('q0', 'X', 'D'),

    ('q4', 'Y'):      ('q4', 'Y', 'D'),
    ('q4', 'Z'):      ('q4', 'Z', 'D'),
    ('q4', VAZIO):    ('q_aceita', VAZIO, 'D'),
}


def extrair_palavras(texto: str) -> list[str]:
    return texto.upper().split()


def maquina_turing(entrada: list[str], max_passos: int = 100000) -> str:
    passos = 0
    if not entrada:
        return "Linguagem não Aceita - entrada vazia", passos

    for simbolo in entrada:
        if simbolo not in ALFABETO_ENTRADA:
            print(f"  '{simbolo}' > símbolo fora do alfabeto de entrada")
            return "Linguagem não Aceita", passos

    fita = list(entrada)
    cabeca = 0
    estado = ESTADO_INICIAL
    
    while estado not in ESTADOS_FINAIS and estado != ESTADO_REJEITA:
        if passos > max_passos:
            print("  Limite de passos excedido (provável loop)")
            return "Linguagem não Aceita", passos

        simbolo = fita[cabeca] if 0 <= cabeca < len(fita) else VAZIO

        transicao = TRANSICOES.get((estado, simbolo))
        if transicao is None:
            print(f"  ({estado}, {simbolo}) > transição não definida -> rejeita")
            estado = ESTADO_REJEITA
            break

        novo_estado, escrito, movimento = transicao

        passos += 1

        if 0 <= cabeca < len(fita):
            fita[cabeca] = escrito
        elif cabeca == len(fita):
            fita.append(escrito)

        print(f"  ({estado:<4}, {simbolo:<6}) -> ({novo_estado:<8}, "
              f"escreve {escrito:<6}, move {movimento}) | fita: {' '.join(fita)}")

        estado = novo_estado

        if movimento == 'D':
            cabeca += 1
        elif movimento == 'E':
            cabeca -= 1

        if cabeca < 0:
            print("  cabeça à esquerda do início -> rejeita")
            estado = ESTADO_REJEITA
            break


    resultado = "Linguagem Aceita" if estado in ESTADOS_FINAIS else "Linguagem não Aceita"
    return resultado, passos


def main_mt():
    if len(sys.argv) > 1:
        entrada = ' '.join(sys.argv[1:])
        print(f"\nEntrada: {entrada}\n")
        resultado, passos = maquina_turing(extrair_palavras(entrada))
        print(f"\nResultado: {resultado}")
        print(f"Passos executados: {passos}")
        return

    with open('testes/testes_recursiva.txt', 'r') as entradas:
        linha = 1
        n_entrada = 1

        for entrada in entradas:
            if linha % 2 != 0:
                print(f"\nEntrada {n_entrada}:\n")

                resultado, passos = maquina_turing(extrair_palavras(entrada))

                print(f"\nResultado: {resultado}")
                print(f"Passos executados: {passos}")

                n_entrada += 1

            elif linha % 2 == 0:
                if entrada.strip() == '1':
                    print("Esperado: Linguaguem aceita\n")
                elif entrada.strip() == '0':
                    print("Esperado: Linguaguem não aceita\n")

                sleep(0.5)

            linha += 1


if __name__ == '__main__':
    main_mt()