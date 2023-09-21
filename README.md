#  Projeto Cryptalytics - Análise Exploratória de Criptomoedas
## Análise exploratória relacionada à série histórica dos valores de criptomoedas

# Descrição do Projeto
O projeto Cryptalytics é um projeto integrador que engloba todas as ferramentas e conhecimentos adquiridos ao longo do curso. Ele visa realizar uma análise exploratória histórica dos valores de criptomoedas, fornecendo insights valiosos para uma corretora financeira diante da crescente demanda por investimentos em criptomoedas. As criptomoedas são ativos digitais descentralizados baseados em criptografia e operam em redes blockchain, oferecendo transações seguras e transparentes, sem a necessidade de intermediários como bancos. Dada a sua natureza altamente volátil, entender seu comportamento ao longo do tempo é fundamental para orientar os investidores.

---

# O Desafio da Corretora Financeira
Os executivos da empresa estavam preocupados com a crescente demanda por investimentos em criptomoedas. A volatilidade desses ativos estava causando preocupações entre os investidores, e a empresa necessitava de uma estratégia sólida para orientar seus clientes.

Foi nesse momento que o **Cryptalytics** entrou em cena. Um squad de analistas de dados especializados em criptomoedas, eles foram escalados para realizar uma análise exploratória da série histórica dos valores das principais criptomoedas do mercado. As criptomoedas selecionadas para análise são Polkadot, Ethereum, Cosmos, EOS, XRP, BinanceCoin, USDCoin, Chainlink, Bitcoin e Aave.

---

# A Jornada Começa
O squad **Cryptalytics** se reuniu. Nós tinhamos um desafio pela frente: compreender as tendências, padrões e comportamentos das criptomoedas ao longo do tempo.

Começamos mergulhando nas histórias por trás das moedas. Polkadot, uma plataforma de interoperabilidade; Ethereum, uma pioneira na tecnologia de contratos inteligentes; Cosmos, com sua visão de "internet dos blockchains"; EOS, conhecida por sua escalabilidade; XRP, focada em pagamentos internacionais; BinanceCoin, a moeda nativa da maior exchange do mundo; USDCoin, uma stablecoin; Chainlink, fornecendo dados confiáveis para contratos inteligentes; Bitcoin, o pioneiro; e Aave, revolucionando o mercado de empréstimos.

---
# Perguntas a serem Respondidas
O projeto visa responder às seguintes perguntas:

1. Como se comportaram os valores para todas as criptomoedas? Os valores tiveram uma tendência de queda ou de aumento?
2. Quais são os valores médios para todas as criptomoedas?
3. Em quais anos houve maiores quedas e valorizações?
4. Existe alguma tendência de aumento ou queda dos valores pelo dia da semana?
5. Qual moeda se mostra mais interessante em relação à valorização pela análise da série histórica?
6. Qual moeda se mostra menos interessante em relação à valorização pela análise da série histórica?
7. Existe correlação entre os valores para todas as criptomoedas?
8. Qual é a média da capitalização de mercado (market cap) das criptomoedas durante o período analisado? Existe alguma criptomoeda que se destaca significativamente em termos de capitalização de mercado?
9. Qual é a criptomoeda com a maior variação percentual de preço em um único dia durante o período analisado?

---

# Estrutura do Repositório
O repositório está organizado da seguinte maneira:

* Arquivos Crypto: Pasta que contém os arquivos tabelas com os dados de cada moeda.

* images: Pasta que contém imagens ultilizados ao longo do projeto (capturas de tela das visualizações criadas no Tableau, Power bi, looker)

* pdf_resumo_criptos: Pasta que contém resumo da hístoria de cada moeda utilizada para análise.

* Projeto_Cryptomoedas.ipynb : Pasta que contém análise exploratória feita pelo Colab.

  ---

  # Ferramentas Utilizadas

- Ambiente de Desenvolvimento e comunicação : Discord
- Limpeza de Dados - Realização da limpeza dos dados para prepará-los para análise : Colab.
- Análise Exploratória: Utilização de técnicas de análise exploratória de dados para extrair insights.
- Banco de Dados: Importação dos arquivos resultantes para um banco de dados : PgAdmin
- Visualização de Dados: Conexão do banco de dados com ferramentas de visualização de dados como Tableau, Power Bi ou Looker. (cada membro usou a ferramenta de sua preferência) 
- Seleção de Criptomoedas: Polkadot, Ethereum, Cosmos, EOS, XRP, BinanceCoin, USDCoin, Chainlink, Bitcoin e Aave.
- Visualização de Resultados: Geração de gráficos para a apresentação dos resultados.
- Storytelling: Apresentação envolvente para comunicar os resultados de forma eficaz.
  

# Instruções

1- Baixar o repositório: Isso significa fazer o download de um conjunto de arquivos, que contém o código e os recursos necessários.

2- Instalar as bibliotecas: Isso envolve adicionar as bibliotecas necessárias ao seu ambiente de desenvolvimento.

**Para instalação** :
- pip install numpy
- pip install pandas
- pip install matplotlib
- pip install seaborn

**Para importação**:
- import pandas as pd
- import numpy as np
- import seaborn as sns
- import matplotlib.pyplot as plt

3- Abrir a pasta usando seu Colab: Se você estiver usando o Google Colab, você precisa abrir a pasta (Relatório_Cryptalytics.ipynb).
[Google Colab]([https://colab.research.google.com/](https://colab.research.google.com/github/mathuscm/Criptomoedas-m5/blob/main/Relat%C3%B3rio_Cryptalytics.ipynb)).

4- Clicar em "Ambiente de Execução": No Google Colab, isso se refere a selecionar o tipo de ambiente de execução.

5- Executar tudo: Isso significa executar todos os scripts ou códigos em seu ambiente de desenvolvimento para garantir que todos os processos sejam executados.

6- Para criar visualizações: Para criar gráficos ou visualizações dos dados, você normalmente precisa usar uma biblioteca de visualização, como o Matplotlib ou o Seaborn em Python.

7- Entre no arquivo de script SQL: Isso implica abrir um arquivo que contém comandos SQL, que são usados para interagir com um banco de dados (ArquivosCrypto).

8- Criar um banco de dados no pgAdmin: PgAdmin é uma ferramenta de gerenciamento de banco de dados para PostgreSQL. Isso significa que você deve usar o PgAdmin para criar um banco de dados onde seus dados serão armazenados.

9- Executar o arquivo de criação de tabelas: Esse arquivo SQL contém comandos para criar tabelas no banco de dados, definindo a estrutura dos dados que você deseja armazenar.

10- Executar o arquivo de inserção de dados: Após criar as tabelas, você deve executar um arquivo SQL que insere os dados desejados nessas tabelas.

11- Abra o Power BI: O Power BI é uma ferramenta de visualização de dados da Microsoft.

12- Conecte o Power BI ao banco de dados: Você precisa configurar uma conexão entre o Power BI e o banco de dados PostgreSQL que você criou anteriormente.

13- Assim pode fazer novas visualizações: Agora, com o Power BI conectado ao seu banco de dados, você pode criar gráficos e relatórios interativos com base nos dados armazenados no banco de dados.

---
# Analistas deste projeto 

- Juliana Gomes (Pessoa Gestora de Gente e Engajamento)<a href="https://www.linkedin.com/in/julianapvh/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">

- Aline Braga (Gestora de conhecimento)<a href="https://www.linkedin.com/in/alinebozollan/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">

- Matheus Cordaro (Colaborador ||)<a href="https://www.linkedin.com/in/mscordaro/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">

- Luis Gustavo Amaral ( Co-facilitador)<a href="https://www.linkedin.com/in/luisamaral2506/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">

- Cristhian Monteiro (Colaborador)<a href="https://www.linkedin.com/in/cristhian-monteiro/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">




