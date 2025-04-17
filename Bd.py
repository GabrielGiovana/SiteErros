import psycopg2
import Bd_Classes

def conexao():
    global bancoDeDados
    bancoDeDados = psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        user="postgres",
        password="postgree00",
        database="erros"
    )
    return bancoDeDados.cursor()

def inserirProblema(problema):
    meuCursor = conexao()
    sql = """
        INSERT INTO problemas (titulo, descricao, solucao, evitar,tag)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        problema.titulo,
        problema.descricao,
        problema.solucao,
        problema.evitar,
        problema.tag
    )

    meuCursor.execute(sql, valores)
    bancoDeDados.commit()
    meuCursor.close()

def problema():
    meuCursor = conexao()
    sql = '''select * from problemas'''
    meuCursor.execute(sql)
    resultados = meuCursor.fetchall()
    meuCursor.close()

    problemas = [

    ]

    for linha in resultados:
        lista_problema = Bd_Classes.Problema(
            id=linha[0],
            titulo=linha[1],
            descricao=linha[2],
            solucao=linha[3],
            evitar=linha[4],
            tag=linha[5]
        )
        problemas.append(lista_problema)
    
    return problemas

