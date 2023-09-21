## SCRIPT PARA INSERIR DADOS NO POSTGRESQL

import psycopg2
import csv

#Configurar banco de dados postgresql
dbname = 'banco_de_dados'
user = 'seu_usuario'
password = 'sua_senha'
host = 'localhost'  
port = '5432'  
table_name = 'nome_tabela'

caminho_csv = 'crypto_coins.csv'

try:
    # acessa o banco de dados
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Abre o arquivo CSV e insere os dados na tabela
    with open(caminho_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            # Arredonda o valor da coluna "Valor_acao"
            valor_acao_arredondado = round(float(row[9]), 2)
            
            # Executando sql para receber os argumentos de values da tabela 
            cursor.execute(
                f"INSERT INTO {table_name} (Id, Nome, Simbolo, Data, Alto, Baixo, Aberto, Fechado, Volume, Valor_acao) "
                f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (int(row[0]), row[1], row[2], row[3], float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), valor_acao_arredondado)
            )

    # Confirma a inserção dos dados
    conn.commit()

    print("Dados inseridos com sucesso!")

except (Exception, psycopg2.Error) as error:
    print(f"Erro ao inserir dados no PostgreSQL: {error}")

finally:
    # Fecha a conexão com o banco de dados
    if 'conn' in locals():
        cursor.close()
        conn.close()
