#Anddrea Paniagua 18733
#Esteban del Valle 18221
#Este programa funciona con simpy para realizar simulaciones
import simpy
import random
import math
import statistics

#numero de instrucciones
random.seed(10) #para generar siempre los random como se deses recurso: https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
ram= 100
cpu= int(input("Ingrese la cantidad de procesadores"))
cantProcesos= int(input("Ingrese la cantidad de procesos"))
intervaloProcesos= int(input("Ingrese el intervalo"))
instrucciones= int(input("Ingrese la cantidad de instrucciones"))
tiempoIO= 1
tiempo= []

class Componentes:
       def __init__(self,env): #siempre en class se define init recurso:file:///C:/Users/Andrea%20Paniagua/Downloads/Python%20Crash%20Course.pdf%20(%20PDFDrive.com%20).pdf
            self.RAM=simpy.Container(env,init=ram)
            self.CPU= simpy.Resource(env,init=ram)

class Proceso:
       def __init__(self, id, env,componnetes):
           self.env=env
           self.instruccion=random.randint(1,19)
           self.ramMin=random.randint(1,10)
           self.id=id
           self.terminated=False
           self.componentes=componentes
           self.primerTiempo=primerTiempo
           self.finalTiempo=finalTiempo
           self.todoTiempo=todoTiempo
           self.proceso=rnv.Proceso(self.procesos(env,componentes))

       def procesos(self,env,componentes):
           self.primerTiempo=env.ya
           print("El proceso: %s: Se ha creado en : %d" %(self.id, self.primerTiempo))
           with componentes.RAM.get(self.ramMin)as ram:
               
                yield ram

                #ram
                print("El proceso es: %s: La ram es: %d (wait)"% (self.id, env.ya))
                op=0

                while not self.terminated:
                    with componentes.CPU.request() as request:
                        print("El proceso es: %s : La espera del CPU es de: %d (wait)"% (self.id, env.ya))
                        yield request

                        for i in range (instruccion):
                            if self.instruccion>  0:
                                self.instruccion -=1
                                op=random.randint(1,2)

                        yield env.timeout(1)

                        if op==1:
                            print("El proceso es de: %s: El In Out es %d"% (self.id, env.ya))
                            yield env.timeout(ioTime)

                        if self.instruccion==0:
                            self.terminated= True

                    print("El proceso es: %s : finalizo en: %d (Estado: Terminated)" %(self.id, env.ya))
                    componentes.RAM.put(self.minRam)

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
desviacion = statistics.stdev(tiempo) 
tiempoProm = statistics.mean(tiempo)         

print (", La desviacion Estandar: ", desviacion, ",El tiempo promedio es:  ", tiempoProm, )
    
                    
       
