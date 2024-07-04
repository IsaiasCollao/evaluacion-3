
from FUNCIONES_ISAIAS_COLLAO import registrar_cobro, listar_cobros, sector_despacho







def main():
    lista_pacientes = []
    opc = 0 
    print("\tSISTEMA HOSPITAL NACIONAL")
    while opc != 4:

        print("1.- Registrar cobro")
        print("2.- Listar cobros registrados")
        print("3.- Definir sector de despacho ")
        print("4.- Salir del programa")
        opc = int(input("Seleccione una opcion: "))

        if opc == 1:
            registrar_cobro(lista_pacientes)

        if opc == 2:
            listar_cobros(lista_pacientes)
            
        if opc == 3:
            sector_despacho()

        if opc == 4:
            print("Programa finalizado")
main()