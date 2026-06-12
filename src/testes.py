import sys
from pathlib import Path
from time import sleep

HERE = Path(__file__).parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from regular import dfa
from livre_contexto import pda
from recursiva import maquina_turing

TESTES_DIR = ROOT / 'testes'


def extrair_palavras(texto: str) -> list[str]:
    return texto.upper().split()


def rodar_suite(titulo: str, arquivo: Path, validador, retorna_passos: bool):
    print(f"\n{'=' * 60}")
    print(f"  {titulo}")
    print(f"{'=' * 60}")

    linhas = arquivo.read_text(encoding='utf-8').splitlines()

    n = 1
    i = 0
    while i < len(linhas):
        entrada_txt = linhas[i].strip()
        esperado_txt = linhas[i + 1].strip() if i + 1 < len(linhas) else ''
        i += 2

        if not entrada_txt:
            continue

        print(f"\nEntrada {n}: {entrada_txt}\n")
        palavras = extrair_palavras(entrada_txt)

        if retorna_passos:
            resultado, passos = validador(palavras)
            print(f"\nResultado: {resultado}")
            print(f"Passos executados: {passos}")
        else:
            resultado = validador(palavras)

        esperado = 'Linguagem aceita' if esperado_txt == '1' else 'Linguagem não aceita'
        print(f"Esperado: {esperado}")

        n += 1
        sleep(0.5)


def main():
    rodar_suite(
        "DFA — Linguagem Regular (LOGIN AUTH REQUEST* LOGOUT)",
        TESTES_DIR / 'testes_regular.txt',
        dfa,
        retorna_passos=False,
    )

    rodar_suite(
        "PDA — Linguagem Livre de Contexto (BEGIN/END aninhados)",
        TESTES_DIR / 'testes_livre_contexto.txt',
        pda,
        retorna_passos=True,
    )

    rodar_suite(
        "Máquina de Turing — Linguagem Recursiva (OPEN^n COMMIT^n CLOSE^n)",
        TESTES_DIR / 'testes_recursiva.txt',
        maquina_turing,
        retorna_passos=True,
    )


if __name__ == '__main__':
    main()
