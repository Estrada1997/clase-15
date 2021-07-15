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

def perfecto(self, numero):
    contador, acu = 1, 0
    for contador in range(1, num):
        rec = num % contador
        if rec == 0 :
            acu = acu + contador
    if acu == num:
        print("{} Es perfecto".format(numero))
    else:
        print("{} No es perfecto".format(numero))

ejer
ejer.perfecto(6)