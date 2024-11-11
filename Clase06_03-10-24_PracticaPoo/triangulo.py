#tipos: equilatero (3 lados iguales), isoseles (2 lados iguales) y escaleno (3 lados distintos)
class Triangulo:
    #============
    #atributos
    #============
    #Forma 1, inicializar atributos
    #lado1 = None
    #lado2 = None
    #lado3 = None

    #Forma 2, inicializar en el constructor
    # def __init__(self):
    # self.lado1 = None
    # self.lado2 = None
    # self.lado3 = None
    equilateroNombre = "Equilatero"
    isoscelesNombre = "Isosceles"
    EscalenoNombre = "Escaleno"
    Tipos = {
        1: equilateroNombre,
        2: isoscelesNombre,
        3: EscalenoNombre
    }

    def __init__(self, lado1, lado2, lado3):
        #print("estoy en el constructor")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    #============
    #Metodos
    #============

    def determinarTipo(self):
        lados = {self.lado1, self.lado2, self.lado3}
        print ("lados tipo:", lados.__class__.__name__)
        print ("lados:",lados)

        """ Forma 1
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isoseles"
        else:
            return "Escaleno"
        """

        """ Forma 2
        if len(lados) == 1:
            return "equilatero"
        elif len(lados) ==2:
            return "Isoceles"
        return "Escaleno"
        """
        #Forma 3 - la mas compacta -
        print(self.lado1, self.lado2, self.lado3)
        return self.Tipos[len({self.lado1,self.lado2,self.lado3})]

if __name__ == "__main__":
    t0 = Triangulo(3,4,5)
    print(t0.determinarTipo())
    t1 = Triangulo(3,3,5)
    print(t1.determinarTipo())
    t2 = Triangulo(3,3,3)
    print(t2.determinarTipo())
