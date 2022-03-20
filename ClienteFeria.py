from Cliente import Cliente

class ClienteFeria(Cliente):
    def __init__(self, cedula, comida):
        super().__init__(cedula)

        self.comida = comida

    def get_comida(self):
        return self.comida