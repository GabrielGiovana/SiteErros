import psycopg2
import Bd_Classes

bancoDeDados = None # Inicializa a variável global

def conexao():
    global bancoDeDados
    if bancoDeDados is None or bancoDeDados.closed:
        bancoDeDados = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="tubarao007",
            database="Teste"
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

    problemas = []
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

def get_problema_by_id(problema_id):
    meuCursor = conexao()
    sql = '''SELECT id, titulo, descricao, solucao, evitar, tag FROM problemas WHERE id = %s'''
    meuCursor.execute(sql, (problema_id,))
    resultado = meuCursor.fetchone()
    meuCursor.close()

    if resultado:
        problema = Bd_Classes.Problema(
            id=resultado[0],
            titulo=resultado[1],
            descricao=resultado[2],
            solucao=resultado[3],
            evitar=resultado[4],
            tag=resultado[5]
        )
       
    return problema