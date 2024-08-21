class ComparadorValores:

    def ingresar_valores(self):
        # Solicita al usuario que ingrese dos valores
        self.valor1 = float(input("Ingrese el primer valor: "))
        self.valor2 = float(input("Ingrese el segundo valor: "))

    def determinar_mayor(self):
        # Compara los dos valores y determina cuál es el mayor
        if self.valor1 > self.valor2:
            return self.valor1
        else:
            return self.valor2

    def mostrar_mayor(self, mayor):
        # Muestra el valor mayor
        print(f"El mayor es: {mayor}")

comparador = ComparadorValores()
comparador.ingresar_valores()
mayor = comparador.determinar_mayor()
comparador.mostrar_mayor(mayor)
