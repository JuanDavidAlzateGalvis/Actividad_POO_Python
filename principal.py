from Banco import Banco
from Cliente import Cliente
from CuentaBancaria import CuentaBancaria


def main():

    banco = Banco("Banco de la moneda", "Argentina", 5, 56500000000)
    cliente = Cliente("Angie Alzate", "24", "Corriente")
    cuentaBancaria = CuentaBancaria("1004359875", "Corriente", 300000000)

    print("Codigo: 7502410040")
    print("Juan David Alzate Galvis")
    print("***********************")
    
    print("")
    print("Informacion del banco:")
    banco.mostrar_detalles()
    print("\nInformacion del cliente:")
    cliente.mostrar_detalles()
    print("\nInformacion de la cuenta bancaria:")
    cuentaBancaria.mostrar_detalles()
    
if __name__ == "__main__":
    main()