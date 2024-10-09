class Cliente:
    
    def __init__(self, nombre, edad, tipoCuenta):
        self._nombre = nombre
        self._edad = edad
        self._tipoCuenta = tipoCuenta

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def tipoCuenta(self):
        return self._tipoCuenta

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @tipoCuenta.setter
    def tipoCuenta(self, tipoCuenta):
        self._tipoCuenta = tipoCuenta 
        
    def mostrar_detalles(self):
        print(f"El nombre del cliente es: {self._nombre}")
        print(f"La edad del cliente es: {self._edad}")
        print(f"Tipo de cuenta: {self._tipoCuenta}")