from RSU_v2.interface import *
from RSU_v2.arquivo import *
from time import sleep

# Definindo os nomes dos arquivos
arqMatOrg = 'materiaorganica.txt'
arqPapPap = 'papelpapelao.txt'
arqPlast = 'plastico.txt'
arqVidr = 'vidro.txt'
arqMet = 'metal.txt'
arquivos = [arqMatOrg, arqPapPap, arqPlast, arqVidr, arqMet]

# Definindo os valores máximos de cada depósito
limMatOrg = limPapPap = limPlast = limVidr = limMet = 20

# Craindo os arquivos
for n in arquivos:
    if not arquivoExiste(n):
        criarArquivo(n)
    
# Inicialização do programa
cabeçalho('GERÊNCIADOR DE DESCARTE DE RSU')

# Inicio do loop
sleep(1)
while True:
    aviso(arquivos)
    cabeçalho('MENU PRINCIPAL')
    resposta = menu(['Entrada de Resíduo', 'Ver Depósitos', 'Esvaziar Depósito', 'Sair do Programa'])
    if resposta == 4:
        # Opção de sair do programa
        cabeçalho('FINALIZANDO O PROGRAMA')
        break
    elif resposta not in [1, 2, 3]:
        # Tratamento para opções inválidas
         print('\033[31mERO! Digite uma opção válida!\033[m')
    else:
        while resposta == 1:
            # Opção de dar entrada nos resíduos
            aviso(arquivos)
            cabeçalho('ENTRADA DE RESÍDUO')
            sleep(1)
            print('Qual resíduo será depositado?')
            residuo = menu(['Matéria Orgânica', 'Papel e Papelão', 'Plástico', 'Vidro', 'Metal', 'Sair'])
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
                # Saindo dessa operação
                break
            else:
                # Digitou uma opção errada
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        
        while resposta == 2:
            # Opção de ver os depósitos
            aviso(arquivos)
            cabeçalho('VER DEPÓSITOS')
            print('Para continuar, basta fechar todos os gráficos.')
            visualizar(arquivos, limMatOrg)
            break
        while resposta == 3:
            # Opção de zerar algum depósito
            aviso(arquivos)
            cabeçalho('ESVAZIAR DEPÓSITO')
            sleep(1)
            print('Qual depósito será esvaziado?')
            deposito = menu(['Matéria Orgânica', 'Papel e Papelão', 'Plástico', 'Vidro', 'Metal', 'Sair'])
            if deposito == 1:
                # Esvaziando Matéria Orgânica
                esvaziar(arqMatOrg)
                # Matriz com os dados das empresas 
                destino = [['Nome', 'Lixo321', 'CompostagemLTDA'], ['CNPJ', '1234', '5678'], ['Telefone', 'Num1', 'Num2'],
                            ['Site', 'www.Siteaqui.com.br', 'Não possui site']]
                sleep(1)
                # Exibir as empresas ao usuário 
                exibir('Sugestão de empresas para coleta de Matéria Orgânica.',destino)
            elif deposito == 2:
                # Esvaziar Papel e Papelão
                esvaziar(arqPapPap)
                # Matriz com os dados das empresas 
                destino = [['Nome', 'Planeta Limpo Recicláveis'], ['CNPJ', '06.151.824/0001-49'], 
                           ['Telefone', '(81) 996960348'], ['Site', 'https://www.planetalimpo.net/']]
                sleep(1)
                # Exibir as empresas ao usuário 
                exibir('Sugestão de empresas para coleta de Papel e Papelão.',destino)
            elif deposito == 3:
                # Esvaziar Plástico
                esvaziar(arqPlast)
                # Matriz com os dados das empresas 
                destino = [['Nome', 'Cooperativa Ecovida Palha de Arroz'], ['CNPJ', '?'], 
                           ['Telefone', '(81) 999415021'], ['Site', 'https://www.instagram.com/palhadearroz/']]
                sleep(1)
                # Exibir as empresas ao usuário 
                exibir('Sugestão de empresas para coleta de Plástico.',destino)
            elif deposito == 4:
                # Esvaziar Vidro
                esvaziar(arqVidr)
                # Matriz com os dados das empresas 
                destino = [['Nome', 'Empresa 1', 'Empresa 2'], ['CNPJ', '1234', '5678'], ['Telefone', 'Num1', 'Num2'],
                            ['Site', 'Site aqui', 'Não possui site']]
                sleep(1)
                # Exibir as empresas ao usuário 
                exibir('Sugestão de empresas para coleta de Vidro.',destino)
            elif deposito == 5:
                # Esvaziar Metal
                esvaziar(arqMet)
                # Matriz com os dados das empresas 
                destino = [['Nome', 'Cooperativa Ecovida Palha de Arroz'], ['CNPJ', '?'], 
                           ['Telefone', '(81) 999415021'], ['Site', 'https://www.instagram.com/palhadearroz/']]
                sleep(1)
                # Exibir as empresas ao usuário 
                exibir('Sugestão de empresas para coleta de Metal.',destino)
            elif deposito == 6:
                # Saindo dessa operação
                break
            else:
                # Digitou uma opção errada
                print('\033[31mERRO! Digite uma opção válida!\033[m')    
        sleep(1)
