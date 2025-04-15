class Problema:
    def __init__(self, titulo, descricao, solucao, evitar, imagem, tag, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.solucao = solucao
        self.evitar = evitar
        self.imagem = imagem
        self.tag = tag
