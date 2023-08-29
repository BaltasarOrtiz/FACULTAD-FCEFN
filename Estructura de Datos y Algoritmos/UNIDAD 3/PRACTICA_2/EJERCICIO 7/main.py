from colaEncadenada import colaEncadenada, Paciente
import os
import random


if __name__ == '__main__':
    os.system("cls")

    colaTurno = colaEncadenada()
    #(Ginecología, Clínica médica, Oftalmología, Pediatría)
    lista = [colaEncadenada(),colaEncadenada(),colaEncadenada(),colaEncadenada()] 

    #datos de simulacion
    tiempoSimulacion = 30
    #datos del paciente
    tiempoAtencion = 2
    frecuencia = 1
    #datos del medico
    tiempoActualTurno = tiempoAtencion + 1

    #variables aux
    reloj = 0
    atendidos= 0
    tiempoEsperaAcumulado = 0

    #variables de especialidad
    reloj1 = 0
    reloj2 = 0
    reloj3 = 0
    reloj4 = 0

    while reloj <= tiempoSimulacion:
        numero1 = random.random()

        print("Reloj: [{}]".format(reloj))

        if numero1 <= (1/frecuencia): #se llega a la cola
            print("Llego paciente numero [{}]".format(reloj))
            #paciente = Paciente(input("Nombre: "),input("DNI: "),input("Especialidad: "))
            pacienteNuevo = Paciente("Juan", "12345678", "Ginecología", reloj)
            colaTurno.insertar(pacienteNuevo)
            
            
        if tiempoActualTurno == tiempoAtencion + 1: #turno desocupado
            if not colaTurno.vacia():
                pacienteSuprimido = colaTurno.suprimir() #obtengo el paciente de la cola de turnos
                
                if pacienteSuprimido.getEspecialidad() == "Ginecología": #type:ignore
                    pacienteSuprimido.setTiempoLlegada(reloj1) #type:ignore
                    lista[0].insertar(pacienteSuprimido)
                    
                    
                    if tiempoActualEspecialidad == tiempoAtencionEspecialidad+1:
                        if not lista[0].vacia():
                            tiempoEspera = reloj1 - lista[0].getTiempoLlegada() #type:ignore
                            atendidos +=1
                            tiempoEsperaAcumulado += tiempoEspera 
                            tiempoActualEspecialidad = tiempoAtencion

                    else: #especialidad ocupada
                        tiempoActualEspecialidad -= 1
                        if tiempoActualEspecialidad == 0:
                            tiempoActualEspecialidad = tiempoAtencionEspecialidad + 1
                    
                    reloj1+=1

                
            
                tiempoEspera = reloj - pacienteSuprimido.getTiempoLlegada() #type:ignore
                atendidos +=1
                tiempoEsperaAcumulado += tiempoEspera 

                print("Se atiende a Paciente numero [{}]: tiempo de espera [{}]".format(pacienteSuprimido.getTiempoLlegada(), tiempoEspera)) #type:ignore
                tiempoActualTurno = tiempoAtencion

        else: #turno ocupado
            tiempoActualTurno -= 1
            if tiempoActualTurno == 0:
                tiempoActualTurno = tiempoAtencion + 1
        
        reloj+=1
    
    print("\n------------------------------------------------------\n")
    print("Cantidad de clientes atendidos: ", atendidos)
    print("El tiempo promedio de espera de los clientes fue de: ", round(tiempoEsperaAcumulado/atendidos, 2))
    print("\n------------------------------------------------------\n")


    """ Realice un programa  que simule el comportamiento de un hospital, 
    donde los pacientes acuden a sacar turnos para los consultorios externos 
    en mesa de entradas  donde se toma la siguiente información: nombre, documento y especialidad 
    (Ginecología, Clínica médica, Oftalmología, Pediatría)  con un tiempo promedio de atención de 
    2 minutos. Considerando que la frecuencia de llegada de los pacientes al hospital es de 1 por minutos 
    

    Dependiendo de la especialidad se le indica el numero de  consultorio en que será atendido. 
    El tiempo promedio de atención del médico es de 20 min. 
    aproximadamente; que en cada especialidad se atiende un máximo de 10 pacientes y los turnos solamente se dan de  8 de la mañana.

     Se pide    a) calcular el tiempo promedio de espera en la cola de turnos.

                b) tiempo promedio de espera de los pacientes en cada especialidad.

                c) cantidad de personas que no pudieron obtener turnos.

    Nota: considere el tiempo de simulación de 4 horas"""