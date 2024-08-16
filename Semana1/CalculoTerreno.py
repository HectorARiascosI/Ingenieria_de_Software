class Terrenito:
    
    def __init__(self, ladoA=0, ladoB=0, ladoC=0):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.altura = 0
        self.area1 = 0
        self.area2 = 0
        self.areaTotal = 0
        
    def ingresar_datos(self):
        print("Por favor, ingrese las medidas del terreno.")
       
        self.ladoA = float(input("Ingrese las medidas del lado A (en metros): "))
        self.ladoB = float(input("Ingrese las medidas del lado B (en metros): "))
        self.ladoC = float(input("Ingrese las medidas del lado C (en metros): "))
             
    def CalcularAlturaTrianguloFormaB(self):
        self.altura = self.ladoA - self.ladoC
       
        
    def CalcularAreaTriangulo(self):
        self.area1 = (self.ladoB * self.altura) / 2
        return
        
    def CalcularAreaRectangulo(self):
        self.area2 = self.ladoB * self.ladoC
        return
        
    def CalcularAreaTotal(self):
        self.areaTotal = self.area1 + self.area2
        return
        
    def MostrarResultados(self):
        print(f"El área del terreno es = {self.areaTotal} metros cuadrados")
        return

# Crear una instancia de Terrenito
terreno = Terrenito()
terreno.ingresar_datos()
terreno.CalcularAlturaTrianguloFormaB()
terreno.CalcularAreaTriangulo()
terreno.CalcularAreaRectangulo()
terreno.CalcularAreaTotal()
terreno.MostrarResultados()
