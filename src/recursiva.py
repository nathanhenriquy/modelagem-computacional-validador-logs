# Máquina de Turing — Trio balanceado de eventos
# Linguagem: { OPEN^n COMMIT^n CLOSE^n | n >= 1 }
#
# Estratégia clássica (análoga ao reconhecedor de a^n b^n c^n):
# A cada passada da esquerda para a direita, marca-se UM OPEN (como X),
# depois UM COMMIT (como Y) e depois UM CLOSE (como Z). Em seguida a cabeça
# rebobina para a esquerda e repete. Quando não restam mais OPEN para marcar,
# faz-se uma varredura final verificando que sobraram apenas Y e Z (ou seja,
# as três quantidades eram iguais). Caso contrário, rejeita.
#
# Símbolos da fita: OPEN, COMMIT, CLOSE (entrada) ; X, Y, Z (marcados) ; _ (branco)
import sys
from time import sleep

VAZIO = '_'

ALFABETO_ENTRADA = {'OPEN', 'COMMIT', 'CLOSE'}
ALFABETO_FITA     = {'OPEN', 'COMMIT', 'CLOSE', 'X', 'Y', 'Z', VAZIO}

ESTADO_INICIAL = 'q0'
ESTADOS_FINAIS = {'q_aceita'}
ESTADO_REJEITA = 'q_rej'

# Tabela de transição:
# (estado, símbolo_lido) -> (novo_estado, símbolo_escrito, movimento)
# movimento: 'D' = direita | 'E' = esquerda
#
# q0 : no início de uma passada. Pula X já marcados; ao achar OPEN marca X e
#      passa a q1. Se em vez de OPEN encontrar Y (todos OPEN já marcados),
#      vai a q4 para a verificação final.
# q1 : anda à direita por OPEN e Y até o primeiro COMMIT; marca-o como Y -> q2.
# q2 : anda à direita por COMMIT e Z até o primeiro CLOSE; marca-o como Z -> q3.
# q3 : rebobina à esquerda até reencontrar um X (último marcado); então move
#      uma casa à direita e volta a q0 para a próxima passada.
# q4 : verificação final: só podem restar Y e Z; ao chegar no branco, aceita.
TRANSICOES: dict[tuple, tuple] = {
    # --- q0: localizar e marcar o próximo OPEN ---
    ('q0', 'X'):      ('q0', 'X', 'D'),
    ('q0', 'OPEN'):   ('q1', 'X', 'D'),
    ('q0', 'Y'):      ('q4', 'Y', 'D'),   # nenhum OPEN restante -> verificar

    # --- q1: andar até o primeiro COMMIT e marcá-lo ---
    ('q1', 'OPEN'):   ('q1', 'OPEN', 'D'),
    ('q1', 'Y'):      ('q1', 'Y', 'D'),
    ('q1', 'COMMIT'): ('q2', 'Y', 'D'),

    # --- q2: andar até o primeiro CLOSE e marcá-lo ---
    ('q2', 'COMMIT'): ('q2', 'COMMIT', 'D'),
    ('q2', 'Z'):      ('q2', 'Z', 'D'),
    ('q2', 'CLOSE'):  ('q3', 'Z', 'E'),

    # --- q3: rebobinar à esquerda até o último X marcado ---
    ('q3', 'OPEN'):   ('q3', 'OPEN', 'E'),
    ('q3', 'COMMIT'): ('q3', 'COMMIT', 'E'),
    ('q3', 'Y'):      ('q3', 'Y', 'E'),
    ('q3', 'Z'):      ('q3', 'Z', 'E'),
    ('q3', 'X'):      ('q0', 'X', 'D'),   # achou o X -> reinicia passada

    # --- q4: verificação final (só Y e Z podem restar) ---
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

        # Símbolo sob a cabeça (branco se fora da fita à direita)
        simbolo = fita[cabeca] if 0 <= cabeca < len(fita) else VAZIO

        transicao = TRANSICOES.get((estado, simbolo))
        if transicao is None:
            print(f"  ({estado}, {simbolo}) > transição não definida -> rejeita")
            estado = ESTADO_REJEITA
            break

        novo_estado, escrito, movimento = transicao

        passos += 1

        # Escreve na fita (expandindo à direita se necessário)
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
            # cabeça tentou passar do início: rejeita (situação inválida aqui)
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