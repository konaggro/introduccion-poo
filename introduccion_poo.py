# 1.- EXPLORACION TEORICA

# ¿Que es la Programacion Orientada a Objetos?
# Es un paradigma de programacion que se encarga de organizar los codigos en objetos que
# tienen atributos (propiedades) y metodos (comportamientos), estos permiten representar los elementos
# del mundo real de una manera mas natural. 

# ¿En que se diferencia de la Programacion Estructurada?
#   La programacion estructurada se basa en las funciones  y secuencias de instrucciones. En cambio
# la POOes la que organiza el codigo en objetos y clases. 

#Ejemplo de la vida real:
# Una mascota puede ser considerada como un ejemplo, 
# ya que el gato tiene atributos como su nombre, 
# edad, raza y metodos como comer, dormir, jugar y su comportamiento.


# 2.- DEFINICION DE UNA CLASE 

class Perro:

    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print ("¡Guau!")

mi_perro = Perro("Firulais", 3, "Labrador")
print(mi_perro.nombre)  # Imprime: Firulais
mi_perro.ladrar()  # Imprime: ¡Guau!


# 3.- DIFERENCIAS DE CONCEPTOS 

# Clase: Plantilla para crear objetos.
# Instancia: Un objeto creado a partir de una clase.
# Objeto: Es un elemento que posee las propiedades y comportamientos definidos en la clase.

# Atributo: Característica de un objeto(nombre, edad, raza).
# Estado: Valor actual de los atributos de un objeto.

# Método: Es la funcion dentro de la clase.  
# Comportamiento: Accion que realiza el objeto.


# 4.- PRINCIPIOS DE POO

class Perro:
    def __init__(self, nombre, edad, raza):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    def ladrar(self):
        print ("¡Guau!")    

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"
    
otro_perro = Perro("Max", 5, "Poodle")

print(otro_perro.mostrar_informacion())  

    #Abstraccion 
    # La abstraccion consiste en mostrar solo la informacion relevante. En este caso, por ejemplo,
    #usamos el metodo mostrar_informacion para interactuar con el objeto sin acceder a sus datos
    #de manera directa.
    
