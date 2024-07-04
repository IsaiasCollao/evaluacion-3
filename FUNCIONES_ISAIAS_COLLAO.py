import random
def registrar_cobro(lista_pacientes):
    print("\tINGRESO DE DATOS")
    dinternado = random.randrange(1,10)
    dinternado *=  90000
    npacciente = input("Ingrese el nombre del paciente: ")
    apaciente = input("Ingrese el apellido del paciente:")
    dpaciente = input("Ingrese la direccion del paciente: ")
    ipaciente = int(input("Ingrese el monto a pagar por insumos del paciente: "))
    bonificacion = (dinternado + ipaciente) * 0.70
    tpagar = (dinternado + ipaciente) - bonificacion

    paciente = {"Nombre paciente": npacciente, "Apellido paciente":apaciente, "Direccion paciente":dpaciente, "Hospitalziacion": dinternado, "Insumos":ipaciente, "Bonificacion":bonificacion, "Total a pagar":tpagar}

    lista_pacientes.append(paciente)

def listar_cobros(lista_pacientes):
    print("\tREGISTRO DE COBROS")
    print("PACIENTE\tDIRECCION\tHOSPITALIZACION\tINSUMOS\tBONIFICACION\tTOTAL A PAGAR")

    for paciente in lista_pacientes:

        print(f"{paciente['Nombre paciente']} {paciente['Apellido paciente']}\t{paciente['Direccion paciente']}\t{paciente['Hospitalziacion']}\t{paciente['Insumos']}\t{paciente['Bonificacion']}\t{paciente['Total a pagar']}")

def sector_despacho():
    sectores = ["CENTRO","NORTE","SUR"]
    print("\tSELECCION SECTOR")
    subopc = 0
    while subopc != 4:
        print("1.-SECTOR CENTRO")
        print("2.-SECTOR NORTE")
        print("3.-SECTOR SUR")
        print("4.-SALIR")
        subopc = int(input("Seleccione una opcion: "))
        if subopc == 1:
            print(f"Ha seleccionado la zona {sectores[0]}")
            break
        if subopc == 2:
            print(f"Ha seleccionado la zona {sectores[1]}")
            break
        if subopc == 3:
            print(f"Ha seleccionado la zona {sectores[2]}")
            break
        if subopc == 4:
            pass
