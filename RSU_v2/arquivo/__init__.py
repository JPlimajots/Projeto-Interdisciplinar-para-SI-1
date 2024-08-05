from RSU_v2.interface import *
from time import sleep


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
        a = open(nome,'at')
        a.write('0')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


'''def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('RESÍDUOS DESCARTADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} kg')
    finally:
        a.close()'''


def entrada(arq, quantidade, máximo):
    try:
        a = open(arq, 'rt')
        dado = a.readline()
        a.close
        a = open(arq, 'wt')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            soma = quantidade + float(dado)
            if soma <= máximo:
                a.write(str(soma))
            else:
                a.write(str(dado))          
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            if soma <= máximo:
                print(f'Novo registro adicionado.')
            else:
                print('Depósito não suporta a adição dessa quantidade de resíduo.')
            a.close()


def esvaziar(arq):
    try:
        a = open(arq, 'rt')
        dado = a.readline()
        a.close
        a = open(arq, 'wt')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            soma = float(dado) - float(dado)
            a.write(str(soma))
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print('Depósito esvaziado com sucesso.')
            a.close()


def aviso(arqs):
    try:
        for n in arqs:
            sleep(0.5)
            a = open(n, 'rt')
            dado = a.readline()
            a.close
            if 100 <= float(dado) < 150:
                print(f'\033[33mO depósito {str(n).upper()[0:-4]} ultrapassou 50% de sua capacidade máxima.\033[m')
            elif 150 <= float(dado) < 200:
                print(f'\033[32mO depósito {str(n).upper()[0:-4]} ultrapassou 75% de sua capacidade máxima.\033[m')
            elif float(dado) == 200:
                print(f'\033[31mO depósito {str(n).upper()[0:-4]} está cheio.\033[m')
        sleep(1)
    except:
        print('Houve um ERRO na abertura dos arquivos!')



'''def residuo(opções):
    while True:
        escolha = menu(opções)
        if escolha == 1:
            print('Quantos kg de Matéria Orgânica?')
        elif escolha == 2:
            print('Pap e pap')
        elif escolha == 3:
            print('Plast')
        elif escolha == 4:
            print('Vidro')
        elif escolha == 5:
            print('Metal')
        elif escolha == 6:
            print('Outros')
        elif escolha == 7:
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')'''