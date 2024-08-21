class Pulgaditas:
    
    # No hay atributos
    
    def MetrosAPulgadas(self,metros):
        self.metros = metros
        self.pulgadas=pulgadas
        pulgadas = metros / 0.0254
        return 
    
    def ingresarValor(self):
        
        self.entrada = entrada
        
        entrada = input("Ingrese la medida de la tela en metros ---->  ")
        return entrada
        
    #para verificar medidas positivas y no cadenas de letras o comas o puntos falsos
    

    
    def valorCorrectoIngresado(self):
        
        if self.entrada.replace('.', '', 1).isdigit():
            
            self.entradas = float(self.entrada)
            
            if self.metros >= 0 :
                
                self.pulgadas= conversor.MetrosAPulgadas(self.metros)
                
                print(f"La medida de la tela en pulgadas es: {self.pulgadas:.2f} pulgadas")
                
conversor = Pulgaditas()