class Pulgaditas:
    # No hay atributos en el constructor porque se inicializan en los métodos

    def metros_a_pulgadas(self, metros):
        # Convierte metros a pulgadas
        pulgadas = metros / 0.0254
        return pulgadas

    def ingresar_valor(self):
        # Solicita al usuario que ingrese un valor en metros
        self.entrada = input("Ingresarr la medida de la tela en metros ---->  ")
        return self.entrada

    def valor_correcto_ingresado(self):
        # Verifica si la entrada es un número válido
        if self.entrada.replace('.', '', 1).isdigit():
            metros = float(self.entrada)
            
            # Verifica si la medida es positiva
            if metros >= 0:
                pulgadas = self.metros_a_pulgadas(metros)
                print(f"La medida de la tela en pulgadas es: {pulgadas:.2f} pulgadas")
            else:
                print("Dato ingresado incorrecto, la medida debe ser un número positivo.")
        else:
            print("Error: Ingrese un número válido por favor.")

# Crear una instancia de la clase Pulgaditas
conversor = Pulgaditas()
conversor.ingresar_valor()
conversor.valor_correcto_ingresado()
