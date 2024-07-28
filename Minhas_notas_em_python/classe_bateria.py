class Bateria:
    """Uma tentativa simples de modelar uma bateria para carro elétrico."""
    
    def __init__(self, tamanho=60):
        """Inicializa os atributos da bateria."""
        self.tamanho = tamanho

    def descrever_bateria(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f'Esse carro tem uma bateria de {self.tamanho} kWh.')

    def calcular_distancia(self):
        """Exibe frase sobre a distancia que o carro pode percorrer com essa bateria."""
        distancia = 0
        if self.tamanho == 60:
            distancia = 200
        elif self.tamanho == 70:
            distancia = 240
        elif self.tamanho == 85:
            distancia = 270
        mensagem = f'Esse carro pode percorrer aproximadamente {distancia} km com uma carga.'
        print(mensagem)

    def upgrade_battery(self):
        """Verifica a capacidade da bateria e define para 85 se for diferente."""
        if self.tamanho != 85:
            self.tamanho = 85
            print("Bateria atualizada para 85 kWh.")
        else:
            print("A bateria já está atualizada.")


