class Cubo:
    def __init__(self, lado):
        
        self.lado = lado

    def calcular_volumen(self):
        
        return self.lado ** 3

    def mostrar_volumen(self):
        
        volumen = self.calcular_volumen()
        print(f"El volumen del cubo es: {volumen}")


lado = float(input("Introduce la longitud del lado del cubo: "))

# Verificar que la longitud sea positiva
if lado <= 0:
    print("Error: La longitud del lado debe ser un número positivo.")
else:
    # Crear una instancia de la clase Cubo
    cubo = Cubo(lado)
    # Mostrar el volumen del cubo
    cubo.mostrar_volumen()
