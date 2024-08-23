from RSU_v2.interface import *
from time import sleep
import matplotlib.pyplot as plt
import numpy as np


def arquivoExiste(nome):
    """
    --> Faz uma verificação se um arquivo existe.
    :param nome: nome do arquivo
    :return: retorna False caso o arquivo não exista, retorna True caso o arquivo exista
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    --> Cria um arquivo.
    :param nome: nome do arquivo
    :return: sem retorno
    """
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
    """
    --> Recebe um valor e soma com o valor já existente dentro de um arquivo. Caso a soma não ultrapasse o valor limite,
    o arquivo é atualizdo. Caso a soma ultrapasse o valor limite, o arquivo continua inalterado.
    :param arq: nome do arquivo
    :param quantidade: valor que será somado 
    :param máximo: valor limite
    :return: sem retorno
    """
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
    """
    --> Busca o número dentro de um arquivo e raliza a soma pelo inverso do número.
    :param arq: nome do arquivo
    :return: sem retorno
    """
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


def aviso(arq):
    """
    --> Faz uma verificação dos números dentro de um arquivo e pode mostrar alguns avisos de acordo com o valor.
    :param arq: nome do arquivo 
    :return: sem retorno
    """
    try:
        for n in arq:
            sleep(0.2)
            a = open(n, 'rt')
            dado = a.readline()
            a.close
            if 100 <= float(dado) < 150:
                print(f'\033[33mO depósito {str(n).upper()[0:-4]} ultrapassou 50% de sua capacidade máxima.\033[m')
            elif 150 <= float(dado) < 200:
                print(f'\033[32mO depósito {str(n).upper()[0:-4]} ultrapassou 75% de sua capacidade máxima.\033[m')
            elif float(dado) == 200:
                print(f'\033[31mO depósito {str(n).upper()[0:-4]} está cheio.\033[m')
    except:
        print('Houve um ERRO na abertura dos arquivos!')



def visualizar(arq, limDeposito):
    """
    --> Faz uma verificação dos números dentro dos arquivos e do valor limite para cada depósito, transforma em
    percentual e mostra um gráfico de setores para cada arquivo.
    :param arq: nome do arquivo
    :param limDeposito: valor limite do depósito
    :return: sem retorno
    """
    i = 0
    try:
        for n in arq:
            a = open(n, 'rt')
            dado = a.readline()
            a.close
            perResiduo = (100 * float(dado)) / limDeposito
            perDeposito = ((limDeposito - float(dado)) * 100) / limDeposito
            y = np.array([perResiduo, perDeposito])
            if i == 0:
                mylabels = ['Matéria Orgânica', 'Disponível']
                mycolors = ['#D2691E', '#FFE4C4']
            elif i == 1:
                mylabels = ['Papel e Papelão', 'Disponível']
                mycolors = ['#0000FF', '#FFE4C4']
            elif i == 2:
                mylabels = ['Plástico', 'Disponível']
                mycolors = ['#FF0000', '#FFE4C4']
            elif i == 3:
                mylabels = ['Vidro', 'Disponível']
                mycolors = ['#006400', '#FFE4C4']      
            elif i == 4:
                mylabels = ['Metal', 'Disponível']
                mycolors = ['#FFFF00', '#FFE4C4']
            elif i == 5:
                mylabels = ['Outros', 'Disponível']
                mycolors = ['#808080', '#FFE4C4']
            myexplode = [0.02, 0]
            plt.figure(n)
            plt.pie(y, labels = mylabels, autopct='%1.1f%%', colors = mycolors, explode = myexplode)
            plt.legend()
            i += 1
        plt.show()
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