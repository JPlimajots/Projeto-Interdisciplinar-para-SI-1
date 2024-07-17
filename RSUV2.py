from RSU_v2.interface import *
from RSU_v2.arquivo import *
from time import sleep

arqMatOrg = 'materiaorganica.txt'
arqPapPap = 'papelpapelao.txt'
arqPlast = 'platico.txt'
arqVidr = 'vidro.txt'
arqMet = 'metal.txt'
arqOutr = 'outros.txt'
arquivos = [arqMatOrg, arqPapPap, arqPlast, arqVidr, arqMet, arqOutr]

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
            quantidade = float(input('Quantos kg de Matéria Orgânica? '))
            entrada(arqMatOrg, 0, quantidade)
        elif residuo == 2:
            # Depositando Papel e Papelão
            print('Pap e Pap')
        elif residuo == 3:
            # Depositando Plast
            print('Plast')
        elif residuo == 4:
            # Depositando vidr
            print('Vidr')
        elif residuo == 5:
            # Depositando Metal
            print('Metal')
        elif residuo == 6:
            #Depositando Outros
            print('Outros')
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
        cabeçalho('Opção 3')
    if resposta == 4:
        # Opção de sair do programa
        break
    else:
        # Degitou uma opção errada
        print('\033[31mERO! Digite uma opção válida!\033[m')
    sleep(2)
