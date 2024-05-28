# inicialização do programa
print('='*40)
print('     GERÊNCIADOR DE DESCARTE DE RSU     ')
print('='*40)
operacao = rsu = deposito = deppapl = depplast = depvidr = depmet = depoutr = depmatorg = 0
# inicio do loop
while operacao != 3:
    print('')
    # Escolher a operação desejada
    if operacao == 0:
        operacao = int(input('''Selecione a operação desejada: \n[1]Entrada de resíduo \n[2]Esvaziar depósito 
[3]Sair do programa \nSua escolha: '''))

    # Enquanto uma operação válida não for digitada, o programa vai continuar perguntando
    while operacao != 1 and operacao != 2 and operacao != 3:
        operacao = int(input('''Selecione a operação desejada: \n[1]Entrada de resíduo \n[2]Esvaziar depósito 
[3]Sair do programa \nSua escolha: '''))

    # operações
    while operacao == 1: #Entrada de Resíduos
        print('')
        print('== ENTRADA DE RESÍDUO ==') #Escolher o resíduo que será depositado
        rsu = int(input('''Qual resíduo você irá depositar? \n[1] Matéria Orgânica (Restos de comida) 
[2] Papel e Papelão (Jornais, revistas, caixas e embalagens) \n[3] Plásticos (Garrafas, frascos, embalagens, etc)
[4] Vidros (Garrafas, frascos, copos, etc) \n[5] Metais (Latas) \n[6] Outros (Roupas, óleos, eletrônicos) \n[7] Sair 
Sua escolha: '''))
        while rsu != 1 and rsu != 2 and rsu!= 3 and rsu != 4 and rsu != 5 and rsu != 6 and rsu != 7:
            rsu = int(input('''Qual resíduo você irá depositar? \n[1] Matéria Orgânica (Restos de comida) 
[2] Papel e Papelão (Jornais, revistas, caixas e embalagens) \n[3] Plásticos (Garrafas, frascos, embalagens, etc)
[4] Vidros (Garrafas, frascos, copos, etc) \n[5] Metais (Latas) \n[6] Outros (Roupas, óleos, eletrônicos) 
Sua escolha: '''))
            
        if rsu == 1: #Depositar Matéria Orgânica
            print('')
            print('== Matéria Orgânica ==')
            matorg = float(input('Digite a quantidade de Matéria Orgãnica em Kg: '))
            soma = depmatorg + matorg
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.'''            
            if soma > 250: 
                print('')
                print(f'''Esse depósito já possui {depmatorg}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                depmatorg += matorg
                print(f'Você acrescentou {matorg}Kg ao depósito de matéria Orgânica.')
                print(f'Depósito de matéria orgânica possui {depmatorg}Kg de resíduos.')

        elif rsu == 2: #Depositar Papel e Papelão
            print('')
            print('== Papel e Papelão ==')
            papl = float(input('Digite a quantidade de Papel e Papelão em Kg: '))
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.''' 
            soma = deppapl + papl
            if soma > 250:
                print('')
                print(f'''Esse depósito já possui {deppapl}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                deppapl += papl
                print(f'Você acrescentou {papl}Kg ao depósito de papel e papelão.')
                print(f'Depósito de papel e papelão possui {deppapl}Kg de resíduos.')
        
        elif rsu == 3: #Depositar Pláticos
            print('')
            print('== Plásticos ==')
            plast = float(input('Digite a quantidade de Plásticos em Kg: '))
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.''' 
            soma = depplast + plast
            if soma > 250:
                print('')
                print(f'''Esse depósito já possui {depplast}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                depplast += plast
                print(f'Você acrescentou {plast}Kg ao depósito de plásticos.')
                print(f'Depósito de plásticos possui {depplast}Kg de resíduos.')
        
        elif rsu == 4: #Depositar Vidros
            print('')
            print('== Vidros ==')
            vidr = float(input('Digite a quantidade de Vidros em Kg: '))
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.''' 
            soma = depvidr + vidr
            if soma > 250:
                print('')
                print(f'''Esse depósito já possui {depvidr}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                depvidr += vidr
                print(f'Você acrescentou {vidr}Kg ao depósito de vidros.')
                print(f'Depósito de vidros possui {depvidr}Kg de resíduos.')

        elif rsu == 5: #Depositar Metais
            print('')
            print('== Metais ==')
            met = float(input('Digite a quantidade de Metais em Kg: '))
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.''' 
            soma = depmet + met
            if soma > 250:
                print('')
                print(f'''Esse depósito já possui {depmet}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                depmet += met
                print(f'Você acrescentou {met}Kg ao depósito de metais.')
                print(f'Depósito de metais possui {depmet}Kg de resíduos.')
        
        elif rsu == 6: #Depositar Outros
            print('')
            print('== Outros ==')
            outr = float(input('Digite a quantidade de Outros em Kg: '))
            '''A capacidade max de cada depósito é 250kg. O programa vai verificar se o depósito vai ultrapassar
            o max. Caso isso aconteça o valor não será atualizado e vai sugerir esvaziar o depósito.''' 
            soma = depoutr + outr
            if soma > 250:
                print('')
                print(f'''Esse depósito já possui {depoutr}Kg e não suporta {soma}Kg de resíduo. 
Sua capacidade é de 250kg.''')
                print('Sugestão: Esvaziar o depósito.')
            else:
                print('')
                depoutr += outr
                print(f'Você acrescentou {outr}Kg ao depósito de outros.')
                print(f'Depósito de outros possui {depoutr}Kg de resíduos.')
        
        elif rsu == 7: #Sair dessa operação
            sair = ' '
            print('')
            while sair not in 'SN':
                sair = str(input('Deseja sair desta operação? [S/N] ')).strip().upper()[0]
            if sair == 'S': #Retornar para o menu (escolher as operações)   
                operacao = 0 

    while operacao == 2: #Esvaziar Depósitos
        print('')
        print('== ESVAZIAR DEPÓSITO ==') #Escolher o depósito que será esvaziado 
        deposito = int(input('''Qual depósito você irá esvaziar? \n[1] Matéria Orgânica \n[2] Papel e Papelão 
[3] Plásticos \n[4] Vidros \n[5] Metais \n[6] Outros \n[7] Sair \nSua escolha: '''))
        while deposito != 1 and rsu != 2 and rsu!= 3 and rsu != 4 and rsu != 5 and rsu != 6 and rsu != 7:
           deposito = int(input('''Qual depósito você irá esvaziar? \n[1] Matéria Orgânica \n[2] Papel e Papelão 
[3] Plásticos \n[4] Vidros \n[5] Metais \n[6] Outros \n[7] Sair \nSua escolha: '''))

        if deposito == 1: #Esvaziar matéria orgânica
            print('')
            print('== Depósito de Matéria Orgânica ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Matéria Orgânica? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Matéria Orgânica foi esvaziado com {depmatorg}Kg de resíduos.')
                depmatorg = 0
        
        elif deposito == 2: #Esvaziar papel e papelão
            print('')
            print('== Depósito de Papel e Papelão ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Papel e Papelão? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Papel e Papelão foi esvaziado com {deppapl}Kg de resíduos.')
                deppapl = 0

        elif deposito == 3: #Esvaziar plásticos
            print('')
            print('== Depósito de Plásticos ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Plásticos? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Plásticos foi esvaziado com {depplast}Kg de resíduos.')
                depplast = 0

        elif deposito == 4: #Esvaziar vidros
            print('')
            print('== Depósito de Vidros ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Vidros? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Vidros foi esvaziado com {depvidr}Kg de resíduos.')
                depvidr = 0

        elif deposito == 5: #Esvaziar metais
            print('')
            print('== Depósito de Metais ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Metais? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Metais foi esvaziado com {depmet}Kg de resíduos.')
                depmet = 0

        elif deposito == 6: #Esvaziar outros
            print('')
            print('== Depósito de Outros ==')
            confirmar = ' ' #Confirmar que quer esvaziar esse depósito
            while confirmar not in 'SN':
                confirmar = str(input('Quer esvaziar o depósito de Outros? [S/N] ')).strip().upper()[0]
            if confirmar == 'S':
                print(f'Depósito de Outros foi esvaziado com {depoutr}Kg de resíduos.')
                depoutr = 0

        elif deposito == 7: #Sair dessa operação
            sair = ' '
            print('')
            while sair not in 'SN':
                sair = str(input('Deseja sair desta operação? [S/N] ')).strip().upper()[0]
            if sair == 'S': #Retornar para o menu (escolher as operações)   
                operacao = 0

    while operacao == 3: #Finalizar o Programa
        print('')
        print('== SAIR DO PROGRAMA ==')
        confirmar = ' '  #Finalizar o programa ou trocar a operação
        while confirmar not in 'SN':
            confirmar = str(input('Você tem certeza que deseja sair? [S/N] ')).strip().upper()[0]
        if confirmar == 'N':
            print('')
            operacao = 0
        else:
            break

print('')
print('='*29)
print('     PROGRAMA FINALIZADO     ')
print('='*29)