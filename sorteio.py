import pyodbc
import random

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-4D8MA0G\SQLEXPRESS;"
    "Database=SORTEIO_PY;"
)
conexao = pyodbc.connect(dados_conexao)
print ('Conexão bem sucedida')
cursor = conexao.cursor()
cursor2 = conexao.cursor()
cursor3 = conexao.cursor()
i=0
while i <= 1:
    print('-----------------------------------')
    print('--Opção A: Registrar participante--')
    print('--Opção B: Consultar tabela      --')
    print('--Opção C: Remover participante  --')
    print('--Opção D: Sortear               --')
    print('--Opção E: Sair                  --')              
    print('-----------------------------------')
    opcao = input('Digite sua opcao: ')
    if opcao in ['A', 'a']:
        nome_p = input('Nome do participante: ')
        numero_p = input('N° de telefone: ')
        comando = f"INSERT INTO PARTICIPANTE (NUM_PARTICIPANTE, NOME_PARTICIPANTE) VALUES ('{numero_p}','{nome_p}')"
        cursor.execute(comando)
        cursor.commit()
        print("\n" * 10)
        print(f'{nome_p} entrou pro sorteio! Seu numero: {numero_p}')
    elif opcao in ['B', 'b']:
        comando = "SELECT * FROM PARTICIPANTE ORDER BY  COD_PARTICIPANTE ASC"
        cursor.execute(comando)
        for row in cursor.fetchall():
            print (row)
    elif opcao in ['C', 'c']:
        codigo_p = input('Codigo do participante a ser removido: ')
        
        comando = f"SELECT * FROM PARTICIPANTE WHERE COD_PARTICIPANTE = {codigo_p}"
        cursor.execute(comando)
        for row in cursor.fetchall():
            print (row)

        sn = input('Esse eh o usuario a ser removido? ')
        if sn in ['Sim','sim','SIM']:
            comando = f"DELETE FROM PARTICIPANTE WHERE COD_PARTICIPANTE = {codigo_p}"
            cursor.execute(comando)
            cursor.commit()
            print("\n" * 10)
            print('Participante removido!')
        elif sn in ['Não', 'Nao', 'não', 'nao', 'NÃO', 'NAO']:
            print("\n" * 10)
            print(f'O participante de n°{codigo_p} NAO foi removido!')
        else:
            print("\n" * 10)
            print('Opcao invalida')
    elif opcao in ['D', 'd']:        
        comando1 = "SELECT MAX(COD_PARTICIPANTE) FROM PARTICIPANTE"
        cursor.execute(comando1)
        for row in cursor.fetchone():
            pass
        o = random.randint(1,row)
        print("\n" * 10)
        rowcopy = row
        row = None
        while row == None:
            o = random.randint(1,rowcopy)
            comando2 = f"SELECT ISNULL(COD_PARTICIPANTE, 0) AS 'Existe' FROM PARTICIPANTE WHERE COD_PARTICIPANTE = {o}"
            cursor2.execute(comando2)
            for row in cursor2.fetchall():
             pass
        print(f'O número sorteado foi: {o}!')
        comando3 = f"EXEC SP_NUMSORTEADO {o}"
        cursor.execute(comando3)
        for row in cursor.fetchall():
            print (row)         
    elif opcao in ['E', 'e']:
        print("\n" * 10)
        print("Programa encerrado.")
        exit()
    else:
        print("\n" * 10)
        print('Opçao invalida')
        exit() 
        