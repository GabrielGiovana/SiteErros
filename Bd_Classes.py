class Problema:
    def __init__(self, titulo, descricao, solucao, evitar,tag, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.solucao = solucao
        self.evitar = evitar
        self.tag = tag


