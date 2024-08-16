class Leche:
    
    def __init__(self, litrosProducidos=0, precioPorLitro=0):
        self.litrosProducidos = litrosProducidos
        self.precioPorLitro = precioPorLitro
        
    
    def IngresarDatos(self):
        self.litrosProducidos = float(input("Ingrese la cantidad de litros producidos --> "))
        self.precioPorLitro = float(input("Ingrese el precio por litro --> "))
        return
       
    def ConversionLitroAGalon(self):
        galonesProducidos = self.litrosProducidos / 3.785
        self.galonesProducidos = galonesProducidos
        return 
    def Precio(self):
        self.precioTotal = self.litrosProducidos * self.precioPorLitro
        self.precioPorGalon = self.precioTotal / self.galonesProducidos
        return 
    
    def MostrarTotal(self):
        print("El total de litros producidos es: ", self.litrosProducidos)
        print(f"El total de galones producidos es: {self.galonesProducidos:.2f}")
        print(f"El precio total por los galones es: {self.precioTotal:.0f}")
        return
    
    #----------------------------------------------------------------

leche=Leche()
leche.IngresarDatos()
leche.ConversionLitroAGalon() 
leche.Precio()
leche.MostrarTotal()

