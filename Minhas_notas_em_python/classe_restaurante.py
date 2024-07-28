class Restaurante():
    def __init__(self,nome,cozinha):
        self.nome = nome
        self.cozinha = cozinha
        self.num_clientes = 0 #adiciona o atributo "num_clientes"
    def descricao(self):
        print('O(a)',self.nome.title(),'é um restaurante com',self.cozinha)
    def abrir(self):
        print('O restaurante está aberto agora!')
    def fechar(self):
        print('O restaurante está fechado agora!')
    def alt_num_clientes(self, num): #método que incrementa o "num_clentes"
        self.num_clientes += num