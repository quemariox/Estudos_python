from classe_carro import Carro #a classe carro elétrico precisa 
                                #ter acesso à sua classe-pai
from classe_bateria import Bateria  #a classe carro elétrico precisa ter acesso 
                                    #à classe que é referenciada em um de seus atributos
class CarroEletrico(Carro):
    """Modela aspectos de carros específicos, veículos elétricos."""
    def __init__(self, montadora, modelo, ano, tamanho=60):
        """Inicializa os atributos da classe-pai e da classe-filha."""
        super().__init__(montadora, modelo, ano)
        self.bateria = Bateria(tamanho)