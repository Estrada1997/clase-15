class Logica:
    def __init__(self, lista=None):
        self.__lista = lista # no presenta por pantalla / privado 
    #   self. dato = 0  este si presenta por pantalla / no privado

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, value):
        self.__lista = value

    def par_Imp(self, numero):
        rec = numero % 2
        if rec ==0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
        
    def perfecto(self, numero):
        pass
#print(ejer.__lsta)#no mepermite imprimir xk es privado
#para imprimir por pantalla (@property)
#ejer = Logica([2, 4, 6])
#num = int(input("Ingrese numero: "))
#ejer.par_Imp(num)

class Ejercicio(Logica):
    def __init__(self, lista, numeros):
        super().__init__(lista)
        self.dato = numeros
    
    def sumar(self, n1, n2):       #polimorfino
        return n1 + n2             #cuando hay varios tipos de metodo 
                                    # pero deben de tener el mimo nombre 
    def par_Imp(self, numero):
        super().par_Imp(numero)
        return numero % 2

ejer = Ejercicio([1, 3, 5], 20)
if (ejer.par_Imp(6) == 0:
    print("Par")
else:
    print("Impar")
print(ejer.lista)
#print(ejer.sumar(4, 8))
