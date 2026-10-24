# Lembrete de Pagamentos Automático

Serviço em Python executado em background para alertar sobre o vencimento de contas. Desenvolvido para facilitar a gestão financeira de usuários idosos, garantindo que os dados permaneçam 100% offline e protegidos.

## Funcionalidades
* Leitura de dados estáticos a partir de uma planilha Excel local.
* Filtragem automática de datas de vencimento cruzadas com o relógio do sistema.
* Alertas visuais e sonoros nativos no Windows usando a biblioteca Plyer.
* Execução silenciosa via Agendador de Tarefas do Windows (sem abrir o terminal).

## Tecnologias e Dependências
* Python 3.x
* `pandas`: Processamento e filtro dos dados.
* `openpyxl`: Motor de leitura para arquivos `.xlsx`.
* `plyer`: Integração com as notificações nativas do sistema operacional.

## Como Usar
1. Clone o repositório: `git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git`
2. Instale as dependências: `pip install pandas openpyxl plyer`
3. Crie um arquivo chamado `contas.xlsx` na mesma pasta do script contendo as colunas **CONTA**, **VENCIMENTO** (formato data) e **STATUS**.
4. Teste manualmente executando: `python nome_do_seu_arquivo.py`

## Automação
Para o programa rodar sozinho diariamente no Windows:
1. Abra o **Agendador de Tarefas** e crie uma Tarefa Básica.
2. Defina o gatilho para "Ao iniciar a sessão" ou diariamente em um horário específico.
3. Na ação "Iniciar um programa", digite `pythonw` (para execução invisível).
4. Nos argumentos, digite o nome do script (ex: `app.py`).
5. Em "Iniciar em", cole o caminho completo da pasta do projeto.