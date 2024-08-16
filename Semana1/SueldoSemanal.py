class Trabajador:
    
    def __init__(self):
        self.horasTrabajadas = 0
        self.pagoPorHora = 0
        self.sueldoSemanal = 0
        
    def IngresarDatos(self):
        self.horasTrabajadas = float(input("Ingrese el número de horas trabajadas en la semana --> "))
        self.pagoPorHora = float(input("Ingrese el pago por hora en COP --> "))
       
    def CalcularSueldo(self):
        self.sueldoSemanal = self.horasTrabajadas * self.pagoPorHora
    
    def MostrarSueldo(self):
        print(f"El sueldo semanal es: {self.sueldoSemanal:.2f}")


trabajador = Trabajador()
trabajador.IngresarDatos()
trabajador.CalcularSueldo()
trabajador.MostrarSueldo()
