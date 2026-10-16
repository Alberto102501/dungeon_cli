from models.items import Arma, Pocion 

class Perosnaje:
    def __init__(self, nombre, vida, vida_maxima):
        self.nombre = nombre
        self.vida = vida
        self.vida_maxima = vida_maxima

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0

    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima

class Jugador(Personaje):
    def __init__(self, nombre, vida=100, vida_maxima = 100):
        super().__init__(nombre, vida, vida_maxima)
        self.arma = None
        self.pociones = []

    def equipar_arma(self, nueva_arma):
        self.arma = nueva_arma

    def agregar_pocion(self, pocion):
        self.pociones.append(pocion)

    def usar_pocion(self):
        if not self.pociones:
            return False

        pocion = self.pociones.pop(0)
        self.curar(pocion.curacion)
        return True

    def calcular_ataque(self):
        if self.arma is None:
            return 6

        dano = self.arma.usar()
        if self.arma.esta_rota():
            print(f"{self.arma.nombre} esta rota")
            self.arma = None
        return dano

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "vida": self.vida,
            "vida_maxima": self.vida_maxima,
            "arma": self.arma.arma.to_dict() if self.arma else None,
            "pociones": [p.to_dict() for p in self.pociones]
        }

