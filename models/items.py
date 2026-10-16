class Item:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "valor": self.valor,
            "tipo": self.__class__.__name__
        }

class Arma(Item):
    def __init__(self, nombre, dano, durabilidad = 3):
        super().__init__(nombre, valor = dano)
        self.dano = dano
        self.durabilidad = durabilidad

    def usar(self):
        if self.durabilidad > 0:
            self.durabilidad -= 1
            return self.dano
        return 0

    def esta_rota(self):
        return self.durabilidad <= 0
            

    def to_dict(self):
        data = super().to_dict()
        data.update({
                     "dano": self.dano, 
                     "durabilidad": self.durabilidad
                    })
        return data

class Pocion(Item):
    def __init__(self, nombre, curacion = 25):
        super().__init__(nombre, valor = curacion)
        self.curacion = curacion

    def to_dict(self):
        data = super().to_dict()
        data.update({
                        "curacion": self.curacion
                    })
        return data