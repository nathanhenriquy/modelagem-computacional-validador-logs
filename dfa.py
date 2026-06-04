# linguagem regular

alfabeto = ['LOGIN', 'AUTH', 'REQUEST', 'LOGOUT']


def extrair_palavras(texto: str) -> list[str]:
    texto = texto.upper()
    return texto.split()


def dfa(entrada):
    estado = 0

    for palavra in entrada:
        # estado inicial
        if estado == 0:
            if palavra == 'LOGIN':
                estado = 1
                print(f"Palavra: {palavra} - Estado: {estado}")

            elif palavra not in alfabeto:
                print("Simbolo não existente")

            else:
                estado = 0
                print(f"Palavra: {palavra} - Estado: {estado}")

        # LOGIN
        elif estado == 1:
            if palavra == 'LOGIN':
                estado = 1
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'AUTH':
                estado = 2
                print(f"Palavra: {palavra} - Estado: {estado}")

            elif palavra not in alfabeto:
                print("Simbolo não existente")

            else:
                estado = 0
                print(f"Palavra: {palavra} - Estado: {estado}")
        
        # AUTH
        elif estado == 2:
            if palavra == 'LOGIN':
                estado = 1
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'AUTH':
                estado = 2
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'REQUEST':
                estado = 3
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'LOGOUT':
                estado = 4
                print(f"Palavra: {palavra} - Estado: {estado}")
                return "Linguagem Aceita"

            elif palavra not in alfabeto:
                print("Simbolo não existente")

            else:
                estado = 0
                print(f"Palavra: {palavra} - Estado: {estado}")

        elif estado == 3:
            if palavra == 'LOGIN':
                estado = 1
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'AUTH':
                estado = 0
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'REQUEST':
                estado = 3
                print(f"Palavra: {palavra} - Estado: {estado}")
            elif palavra == 'LOGOUT':
                estado = 4
                print(f"Palavra: {palavra} - Estado: {estado}")
                return "Linguagem Aceita"

            elif palavra not in alfabeto:
                print("Simbolo não existente")

            else:
                estado = 0
                print(f"Palavra: {palavra} - Estado: {estado}")
        
        elif estado == 4:
            return "Linguagem Aceita"
    
    if estado != 4:
        return "Linguagem não Aceita"


def main():
    entrada = extrair_palavras(input("Insira uma string: "))

    print(dfa(entrada))


if '__main__' == __name__:
    main()
