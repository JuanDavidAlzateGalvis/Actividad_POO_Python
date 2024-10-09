class CuentaBancaria:
    
    def __init__(self, numeroCuenta, tipoCuenta, saldoCuenta):
        self._numeroCuenta = numeroCuenta
        self._tipoCuenta = tipoCuenta
        self._saldoCuenta = saldoCuenta

    @property
    def numeroCuenta(self):
        return self._numeroCuenta

    @property
    def tipoCuenta(self):
        return self._tipoCuenta
    
    @property
    def saldoCuenta(self):
        return self._saldoCuenta

    @numeroCuenta.setter
    def numeroCuenta(self, numeroCuenta):
        self._numeroCuenta = numeroCuenta

    @tipoCuenta.setter
    def tipoCuenta(self, tipoCuenta):
        self._tipoCuenta = tipoCuenta 
        
    @saldoCuenta.setter
    def saldoCuenta(self, saldoCuenta):
        self._saldoCuenta = saldoCuenta
        
    def mostrar_detalles(self):
        print(f"Numero de la cuenta: {self._numeroCuenta}")
        print(f"Tipo de la cuenta: {self._tipoCuenta}")
        print(f"El saldo actual de la cuenta es: {self._saldoCuenta}")