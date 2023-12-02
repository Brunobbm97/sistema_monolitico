class Equipe():
    def __init__(self, nome, dt_criacao, chefe_equipe, num_funcionarios, categoria, id=None):
        self.nome = nome
        self.dt_criacao = dt_criacao
        self.chefe_equipe = chefe_equipe
        self.num_funcionarios = num_funcionarios
        self.categoria = categoria
        self.id = id