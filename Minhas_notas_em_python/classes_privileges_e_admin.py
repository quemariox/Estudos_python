from classe_usuario import Usuario

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