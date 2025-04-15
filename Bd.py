import psycopg2
import Bd_Classes  

def conexao():
    global bancoDeDados
    bancoDeDados = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="tubarao007",
        database="Teste"
    )
    return bancoDeDados.cursor()

def inserirProblema(problema):
    meuCursor = conexao()
    sql = """
        INSERT INTO problemas (titulo, descricao, solucao, evitar, imagem, tag)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        problema.titulo,
        problema.descricao,
        problema.solucao,
        problema.evitar,
        problema.imagem,
        problema.tag
    )

    meuCursor.execute(sql, valores)
    bancoDeDados.commit()
    meuCursor.close()


def problema():
    meuCursor = conexao()
    meuCursor.execute("SELECT * FROM problemas")
    resultados = meuCursor.fetchall()
    meuCursor.close()

    problemas = []

    for linha in resultados:
        problema = Bd_Classes.Problema(
            id=linha[0],
            titulo=linha[1],
            descricao=linha[2],
            solucao=linha[3],
            evitar=linha[4],
            imagem=linha[5],
            tag=linha[6]
        )
        problemas.append(problema)
    
    return problemas

