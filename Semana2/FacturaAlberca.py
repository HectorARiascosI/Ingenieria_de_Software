class CalculadoraPagoAgua:
    
    def calcular_pago(self, precio_por_metro_cubico, volumen_alberca):
        # Calcula el total a pagar
        return precio_por_metro_cubico * volumen_alberca

    def ingresar_valores(self):
        # Solicita al usuario el precio por metro cúbico y el volumen
        precio_por_metro_cubico = float(input("Ingressar el precio por metro cúbico de agua ----> "))
        volumen_alberca = float(input("Ingresar el volumen de la alberca en metros cúbicos ----> "))
        return precio_por_metro_cubico, volumen_alberca

    def mostrar_pago(self, total_a_pagar):
        # Muestra el monto total a pagar
        print(f"El monto total a pagar es ----> {total_a_pagar:.2f}")

# Crear una instancia de la clase CalculadoraPagoAgua
calculadora = CalculadoraPagoAgua()
precio, volumen = calculadora.ingresar_valores()
total = calculadora.calcular_pago(precio, volumen)
calculadora.mostrar_pago(total)
