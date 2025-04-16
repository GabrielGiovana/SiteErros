class Problema:
    def __init__(self, titulo, descricao, solucao, evitar, imagem, tag, id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.solucao = solucao
        self.evitar = evitar
        self.imagem = imagem
        self.tag = tag



def problema_simulado():
    # Simulação dos resultados da consulta como uma lista de tuplas
    resultados_simulados = [
        (1, 
        'Erro de Conexão com o Banco de Dados',
         'O aplicativo não consegue se conectar ao servidor do banco de dados.',
         'Verificar as configurações de conexão, firewall e status do servidor.',
         'Monitorar a saúde do servidor e garantir configurações corretas.',
         'conexao_erro.png',
         1
         ),
        (2, 'Desempenho Lento da Aplicação', 'A aplicação está demorando muito para carregar e responder.',
         'Analisar logs, otimizar consultas e verificar uso de recursos do servidor.',
         'Realizar testes de performance regulares e otimizar o código.', 'desempenho_lento.jpg', 2),
        (3, 'Falha ao Salvar Dados do Usuário', 'O sistema não está conseguindo persistir as informações dos usuários.',
         'Verificar erros no banco de dados, permissões de escrita e integridade dos dados.',
         'Implementar rotinas de backup e validação de dados robustas.', 'erro_salvar.gif', 1),
        (4, 'Problema de Autenticação', 'Usuários não estão conseguindo fazer login no sistema.',
         'Verificar configurações de autenticação, logs de erro e status do servidor de autenticação.',
         'Utilizar métodos de autenticação seguros e testar o sistema regularmente.', None, 3)
    ]
    return resultados_simulados