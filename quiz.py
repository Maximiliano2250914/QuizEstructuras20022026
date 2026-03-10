contClientes = 0
cent = "k"; cent2 = 4; cent2_1 = 0; cent2_2 = 0
# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaNombres:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicioNombre(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza

            self.cabeza = nuevo_nodo

# CLase Listas enlazada simple
class ListaCedulas:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicioCedula(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza

            self.cabeza = nuevo_nodo

    def encontrarCedula(self, cedulaNecesitada):
        actual = self.cabeza

        while actual is not None:
            if actual.data == cedulaNecesitada:
                print("Encontrado")
                return True
            actual = actual.siguiente

        print("No encontrado")
        return False


class ListaHabitacionesDisponibles:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicioHabitacionesDisponibles(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza

            self.cabeza = nuevo_nodo


class ListaOrdenLlegada:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicioOrdenLlegada(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza

            self.cabeza = nuevo_nodo

    def encontrarOrdenLlegada(self, ordenNecesitado):
        actual = self.cabeza

        while actual is not None:
            if actual.data == ordenNecesitado:
                print("Encontrado")
                return True
            actual = actual.siguiente

        print("No encontrado")
        return False 


class ListaHabitacionesOcupadas:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicioHabitacionesOcupadas(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza

            self.cabeza = nuevo_nodo

listaNombres = ListaNombres()
listaCedulas = ListaCedulas()
listaHabitacionesDisponibles = ListaHabitacionesDisponibles()
listaHabitacionesOcupadas = ListaHabitacionesOcupadas()
listaOrdenLlegada = ListaOrdenLlegada()

while cent != "n":
    cent = input("Va a anadir cliente? (s/n): ")
    if cent == "n":
        break
    nombreCliente = input("Ingrese el nombre del cliente:")
    listaNombres.agregarInicioNombre(nombreCliente)

    cedulaCliente = int(input("Ingrese la cedula del cliente: "))
    listaCedulas.agregarInicioCedula(cedulaCliente)

    contClientes += 1
    listaOrdenLlegada.agregarInicioOrdenLlegada(contClientes)
    numHabitacion = int(input("Ingrese la habitacion que se le dara al cliente: "))
    listaHabitacionesOcupadas.agregarInicioHabitacionesOcupadas(numHabitacion)
    
    cent2 = 4
    cent2_1 = 0
    cent2_2 = 0

    while cent2 != 3:
        print("1. Consultas vigentes por huesped")
        print("2. Consulta de habitaciones")
        print("3. Salir")
        cent2 = int(input("Ingrese el numero deseado: "))
        
        if cent2 == 3:
            break

        if cent2 == 1:
            while cent2_1 != 3:
                print("1. Individual")
                print("2. Total")
                print("3. Salir")
                cent2_1 = int(input("Ingrese el numero deseado: "))
                
                if cent2_1 == 3:
                    break

                if cent2_1 == 2:
                    cual = input("Buscar cedula (c) u orden de llegada (o)?: ")
                    if cual == "c":
                        cedulaCliente = int(input("Ingrese la cedula que busca: "))
                        listaCedulas.encontrarCedula(cedulaCliente)
                    if cual == "o":
                        ordenCliente = int(input("Ingrese el numero del cliente segur orden de llegada inverso (1 es el ultimo, 2 el penultimo, etc): "))
                        listaOrdenLlegada.encontrarOrdenLlegada(ordenCliente)

                if cent2_1 == 1:
                    cedulaCliente = int(input("Ingrese la cedula que busca: "))
                    listaCedulas.encontrarCedula(cedulaCliente)
                    ordenCliente = int(input("Ingrese el numero del cliente segur orden de llegada inverso (1 es el ultimo, 2 el penultimo, etc): "))
                    listaOrdenLlegada.encontrarOrdenLlegada(ordenCliente)

        if cent2 == 2:
            while cent2_2 != 3:
                print("1. Lista de habitaciones disponibles")
                print("2. Lista de habitaciones ocupadas")
                print("3. Salir")
                cent2_2 = int(input("Ingrese el numero deseado: "))
                
                if cent2_2 == 3:
                    break


                if cent2_2 == 1:
                    actual = listaHabitacionesDisponibles.cabeza
                    while actual:
                        print(actual.data)
                        actual = actual.siguiente

                if cent2_2 == 2:
                    actual = listaHabitacionesOcupadas.cabeza
                    while actual:
                        print(actual.data)
                        actual = actual.siguiente
				print(ListaHabitacionesOcupadas)
