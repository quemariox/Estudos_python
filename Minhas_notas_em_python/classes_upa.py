class Usuario:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.tentativas_login = 0

    def descricao(self):
        print('\nNome:', self.nome.title(), '\nSobrenome:', self.sobrenome.title())

    def saudacao(self):
        print('\nSaudações, ó grandioso', self.nome.title(), self.sobrenome.title())

    def incrementa_tentativas_login(self):
        self.tentativas_login += 1

    def resetar_tentativas_login(self):
        self.tentativas_login = 0

class Privileges:
    def __init__(self):
        self.privilegios = ['deletar post', 'adicionar post', 'banir usuário']

    def show_privileges(self):
        print('Um usuário do tipo ADMIN tem os seguintes privilégios:')
        for privilegio in self.privilegios:
            print(f'- {privilegio}')

class Admin(Usuario):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.privilegios = Privileges()