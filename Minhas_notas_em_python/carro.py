class Carro:
    """Uma tentativa simples de representar um carro."""
    def __init__(self, montadora, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.hodometro = 0

    def apresentar_descricao(self):
        """Devolve um nome descritivo formatado de modo elegante"""
        descricao = f"{self.ano} {self.montadora} {self.modelo}"
        return descricao

    def ler_hodometro(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print(f'Este carro tem {self.hodometro} km')

    def atualizar_hodometro(self, kilometragem):
        """Define o valor de leitura do hodômetro com o valor especificado e 
        rejeita alteração caso seja uma tentativa de voltar o hodômetro."""
        if kilometragem >= self.hodometro:
            self.hodometro = kilometragem
        else:
            print('Pare de tentar trapacear!')

    def incrementar_hodometro(self, incremento):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        if incremento >= 0:
            self.hodometro += incremento
        else:
            print('Pare de tentar trapacear!')

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

class CarroEletrico(Carro):
    """Modela aspectos de carros específicos, veículos elétricos."""
    def __init__(self, montadora, modelo, ano, tamanho=60):
        """Inicializa os atributos da classe-pai e da classe-filha."""
        super().__init__(montadora, modelo, ano)
        self.bateria = Bateria(tamanho)
