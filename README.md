# Conte Lixo
## O Conte Lixo é um gerenciador de descarte de resíduo sólido urbano. Ele apresenta um sistema de depósito separado por tipos de resíduo onde o usuário pode adicionar uma quantidade ou esvaziar. Visando a reciclagem e a reutilização, o sistema faz recomendações de destinos para esses resíduos.

<h4 aling="center">
    Projeto em desenvolvimento...
</h4>

### Features
- [x] Depósito de resíduos
- [x] Recomendação de destinos
- [x] Visualização gráfica
- [x] Alertas de capacidade
- [ ] Cadastro de destinos
- [ ] Configuração personalizada
- [ ] Atualização em tempo real
- [ ] Comunicação com os destinos

### Tecnologias
-[Python](https://www.python.org/)
-[VSCode](https://code.visualstudio.com/)

### Organização
- Foi utilizado a função sleep da biblioteca time para adicionar uma sensação de terminal mais interativo.
- As bibliotecas matplotlib.pyplot e numpy foram utilizadas para plotar os gráficos. (Necessária para funcionar corretamente).
- Dois módulos foram construídos, o interface.py para armazenar as funções que mexem apenas na interface do programa, e o arquivo.py para armazenar as funções que manipulam os arquivos do programa. 

### Funcionamento
O programa inicia com um menu apresentando quatro opções.
- [1] Entrada de Resíduo
- [2] Ver Depósitos
- [3] Esvaziar Depósito
- [4] Sair
<h4 aling="center">
    A opção 1 leva para a funcionalidade de depositar resíduo, o usuário seleciona uma categoria (matéria orgânica, papel e papelão, plástico, vidro, metal) e insere a quantidade que será descartada (em kg). Caso esse valor ultrapasse o limite do depósito (20kg) o programa gera uma alerta e o valor não é atualizado. Caso o valor chegue na metade do limite, o programa vai gerar alertas para avisar sobre a capacidade do depósito.
</h4>
<h4 aling="center">
    A opção 2 leva para a funcionalidade de representação gráfica, o usuário poderá visualizar um gráfico de setores para cada categoria, mostrando o percentual livre e o ocupado.
</h4>
<h4 aling="center">
    A opção 3 leva para a funcionalidade de esvaziar um depósito e recomendação de destino, assim que um depósito é esvaziado, o sistema lista as alternativas de destino para aquele tipo de resíduo, informando nome da empresa, CNPJ, telefone e site.
</h4>
<h4 aling="center">
    A opção 4 encerra o programa.
    Todos os dados de depósito são armazenados em arquivos txt.
</h4>

### Autor
- Feito por João Pedro de Lima.
- Projeto desenvolvido durante a disciplina de Projeto Interdisciplinar para Sistemas de Informação 1. 
