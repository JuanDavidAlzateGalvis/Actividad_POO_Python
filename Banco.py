class Banco:
    
    def __init__(self, nombre, pais, numeroSucursales, numeroClientes):
        self._nombre = nombre
        self._pais = pais
        self._numeroSucursales = numeroSucursales
        self._numeroClientes = numeroClientes
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def pais(self):
        return self._pais

    @property
    def numeroSucursales(self):
        return self._numeroSucursales
    
    @property
    def numeroClientes(self):
        return self._numeroClientes
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @numeroSucursales.setter
    def numeroSucursales(self, numeroSucursales):
        self._numeroSucursales = numeroSucursales 
        
    @numeroClientes.setter
    def numeroClientes(self, numeroClientes):
        self._numeroClientes = numeroClientes
        
    def mostrar_detalles(self):
        print(f"El nombre del banco es: {self._nombre}")
        print(f"El pais donde se encuentra el banco es: {self._pais}")
        print(f"El numero de sucursales que tiene el banco es de: {self._numeroSucursales}")
        print(f"El numero de clientes del banco son: {self._numeroClientes}")