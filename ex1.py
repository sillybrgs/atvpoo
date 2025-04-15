import math

class FiguraGeometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

    def nome(self):
        return self.__class__.__name__

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FiguraGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

class TrianguloEquilatero(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def perimetro(self):
        return 3 * self.lado

# Programa principal
figuras = [
    Circulo(5),
    Retangulo(4, 6),
    TrianguloEquilatero(3)
]

for figura in figuras:
    print(f"{figura.nome()}: Área = {figura.area():.2f}, Perímetro = {figura.perimetro():.2f}")
