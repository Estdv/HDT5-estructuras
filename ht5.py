#Anddrea Paniagua 18733
#Esteban del Valle 18221
#Este programa funciona con simpy para realizar simulaciones
import simpy
import random
import math
#Main en el que se hacen los procesos
#referencia tsobre variables tomada de https://es.stackoverflow.com/questions/4034/cu%C3%A1l-es-la-diferencia-entre-usr-bin-python-y-usr-bin-env-python
def procesos(env, componentes): #env permite correr programas modificados
    env = simpy.Environment()
    componentes = Componentes(env)#RAM Y CPU
    env.procesos(procesos(env,componentes))#procesos
    env.run()
    for i in range(cantidadProcesos):
        tiempo = math.exp(1.0/intervaloProcesos)
        Proceso(i, env, componentes)
        print (env.timeout(tiempo))  # tiempo en crearse
#Resultados requeridos
#referencia https://docs.python.org/3/library/statistics.html
desviacion = statistics.stdev(procesoTiempo) 
tiempoProm = statistics.mean(procesoTiempo)         
 
print (", La desviacion Estandar: ", desviacion, ","El tiempo promedio es:  ", tiempoProm, )
