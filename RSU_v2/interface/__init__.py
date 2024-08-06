def leiaInt(msg):
    """
    --> Pede um número inteiro e checa se realmente é um inteiro ou se algo foi digitado.
    :param msg: mensagem do input 
    :return: retorna o valor absoluto do número inteiro. Caso o usuário não digite nada, retorna 0
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return abs(n)


def leiaFloat(msg):
    """
    --> Pede um número real e checa se realmente é um real ou se algo foi digitado.
    :param msg: mensagem do input 
    :return: retorna o valor absoluto do número real. Caso o usuário não digite nada, retorna 0
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return abs(n)


def linha(tam = 42):
    """
    --> Faz uma linha.
    :param tam: define o tamanho da linha, 42 por padrão 
    :return: sem retorno
    """
    return '-' * tam


def cabeçalho(txt):
    """
    --> Faz um cabeçalho centralizado nas linhas.
    :param txt: texto do cabeçalho
    :return: sem retorno
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    --> Faz um menu com os itens de uma lista.
    :param lista: lista de itens que serão as opções do menu
    :return: retorna a opção selecionada
    """
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


