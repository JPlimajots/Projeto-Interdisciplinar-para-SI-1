from RSU_v2.interface import *
from RSU_v2.arquivo import *
from time import sleep

# Definindo os nomes dos arquivos
arqMatOrg = 'materiaorganica.txt'
arqPapPap = 'papelpapelao.txt'
arqPlast = 'platico.txt'
arqVidr = 'vidro.txt'
arqMet = 'metal.txt'
arqOutr = 'outros.txt'
arquivos = [arqMatOrg, arqPapPap, arqPlast, arqVidr, arqMet, arqOutr]

# Definindo os valores máximos de cada depósito
limMatOrg = limPapPap = limPlast = limVidr = limMet = limOutr = 200

# Craindo os arquivos
for n in arquivos:
    if not arquivoExiste(n):
        criarArquivo(n)
    
# Inicialização do programa
cabeçalho('GERÊNCIADOR DE DESCARTE DE RSU')

# Inicio do loop
sleep(2)
while True:
    cabeçalho('MENU PRINCIPAL')
    resposta = menu(['Entrada de Resíduo', 'Ver Depósitos', 'Esvaziar Depósito', 'Sair do Programa'])
    while resposta == 1:
        # Opção de dar entrada nos resíduos
        cabeçalho('ENTRADA DE RESÍDUO')
        sleep(1)
        print('Qual resíduo será depositado?')
        residuo = menu(['Matéria Orgânica', 'Papel e Papelão', 'Plástico', 'Vidro', 'Metal', 'Outros', 'Sair'])
        if residuo == 1:
            # Depositando Mat. Org.
            quantidade = leiaFloat('Quantos kg de Matéria Orgânica? ')
            entrada(arqMatOrg, quantidade, limMatOrg)
        elif residuo == 2:
            # Depositando Papel e Papelão
            quantidade = leiaFloat('Quantos kg de Papel e Papelão? ')
            entrada(arqPapPap, quantidade, limPapPap)
        elif residuo == 3:
            # Depositando Plast
            quantidade = leiaFloat('Quantos kg de Plástico? ')
            entrada(arqPlast, quantidade, limPlast)
        elif residuo == 4:
            # Depositando vidr
            quantidade = leiaFloat('Quantos kg de Vidro? ')
            entrada(arqVidr, quantidade, limVidr)
        elif residuo == 5:
            # Depositando Metal
            quantidade = leiaFloat('Quantos kg de Metal? ')
            entrada(arqMet, quantidade, limMet)
        elif residuo == 6:
            #Depositando Outros
            quantidade = leiaFloat('Quantos kg de Outros? ')
            entrada(arqOutr, quantidade, limOutr)
        elif residuo == 7:
            # Saindo dessa operação
            break
        else:
            # Digitou uma opção errada
            print('\033[31mERRO! Digite uma opção válida!\033[m')
       
    while resposta == 2:
        # Opção de ver os depósitos
        cabeçalho('Opção 2')
    while resposta == 3:
        # Opção de zerar algum depósito
        cabeçalho('ESVAZIAR DEPÓSITO')
        sleep(1)
        print('Qual depósito será esvaziado?')
        deposito = menu(['Matéria Orgânica', 'Papel e Papelão', 'Plástico', 'Vidro', 'Metal', 'Outros', 'Sair'])
        if deposito == 1:
            # Esvaziando Matéria Orgânica
            esvaziar(arqMatOrg)
        elif deposito == 2:
            # Esvaziar Papel e Papelão
            esvaziar(arqPapPap)
        elif deposito == 3:
            # Esvaziar Plástico
            esvaziar(arqPlast)
        elif deposito == 4:
            # Esvaziar Vidro
            esvaziar(arqVidr)
        elif deposito == 5:
            # Esvaziar Metal
            esvaziar(arqMet)
        elif esvaziar == 6:
            # Esvaziar Outros
            esvaziar(arqOutr)
        elif deposito == 7:
            # Saindo dessa operação
            break
        else:
            # Digitou uma opção errada
            print('\033[31mERRO! Digite uma opção válida!\033[m')    
    if resposta == 4:
        # Opção de sair do programa
        break
    else:
        # Degitou uma opção errada
        print('\033[31mERO! Digite uma opção válida!\033[m')
    sleep(2)
