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