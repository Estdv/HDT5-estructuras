#Anddrea Paniagua 18733
#Esteban del Valle 18221
#Adrea Paniagua 18733
#Esteban del Valle 18221
#Este programa funciona con simpy para realizar simulaciones
import simpy
import random
import math
import statistics

#numero de instrucciones
random.seed(10) #para generar siempre los random como se deses recurso: https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
ram= 100
cpu= int(input("Ingrese la cantidad de procesadores: "))
cantProcesos= int(input("Ingrese la cantidad de procesos: "))
intervaloProcesos= int(input("Ingrese el intervalo: "))
instrucciones= int(input("Ingrese la cantidad de instrucciones: "))
tiempoIO= 1
tiempo= [] #guardara los tiempos de los procesos
# paar definir clases, referencia file:///C:/Users/Andrea%20Paniagua/Downloads/Python%20Crash%20Course.pdf%20(%20PDFDrive.com%20).pdf
class Componentes:
       def __init__(self,env): #siempre en class se define init recurso:file:///C:/Users/Andrea%20Paniagua/Downloads/Python%20Crash%20Course.pdf%20(%20PDFDrive.com%20).pdf
            self.RAM=simpy.Container(env,init = ram, capacity = ram)
            self.CPU= simpy.Resource(env,capacity = cpu)
#clase de los objetos a utilizar
#cuando se libera el CPU se utiliza el proceso
class Proceso:
       def __init__(self, id, env,componentes): #instanciar los atributos a usar en python es .self
           self.env=env
           self.instruccion=random.randint(1,10) #cuando e CPU tiene menos de 3 se libera rapido
           self.ramMin=random.randint(1,10)
           self.id=id #para tomar un parametro ref: https://www.programiz.com/python-programming/methods/built-in/id
           self.terminated=False
           self.componentes=componentes
           self.primerTiempo=0
           self.finalTiempo=0
           self.todoTiempo=0
           self.proceso=env.process(self.procesos(env,componentes))
#funcion para ahorrar repetir passo cada vez ue necesita procesar algo
       def procesos(self,env,componentes): 
           self.primerTiempo=env.now #para iniciar tiempo https://simpy.readthedocs.io/en/latest/topical_guides/environments.html
           print(f"El proceso: ",self.id," Se ha creado en : ",self.primerTiempo,)
           with componentes.RAM.get(self.ramMin)as ram: #para utilizar los mismos componentes y ahorrar lineas ref: https://docs.python.org/3/reference/compound_stmts.html
            #yield para simpy
                yield ram

                #proceso de la ram
                print("El proceso es: ",self.id," La ram es: ",env.now,"Estado:Wait")
                op=0

                while not self.terminated:
                    with componentes.CPU.request() as request: #ref http://docs.python-requests.org/en/master/
                        print(f"El proceso es: ",self.id," La espera del CPU es de:",env.now,)
                        yield request
#para que cuando use instruccion lo mantenga siempre en el parametro deseado
                        for x in range (self.instruccion):
                            if self.instruccion>  0:
                                self.instruccion -=1
                                op=random.randint(1,2) # para que sea discreto https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randint.html
#el cpu debe esperar para otro proceso
                        yield env.timeout(1) 

                        if op==1:
                            print(f"El proceso es de: ",self.id," El In Out es: ",env.now,)
                            yield env.timeout(tiempoIO)

                        if self.instruccion==0:
                            self.terminated= True

                        print(f"El proceso es: ",self.id," ha finalizo en: ",env.now," Estado: Terminated " )
                        self.finalTiempo = env.now
                        self.todoTiempo = int(self.finalTiempo - self.primerTiempo)
                        tiempo.insert(self.id, self.todoTiempo)
                        

#Main en el que se hacen los procesos
#referencia tsobre variables tomada de https://es.stackoverflow.com/questions/4034/cu%C3%A1l-es-la-diferencia-entre-usr-bin-python-y-usr-bin-env-python
def procesos(env, componentes): #env permite correr programas modificados
    for x in range(cantProcesos):
        otroTiempo = math.exp(1.0/intervaloProcesos) #segun se indico en hoja
        Proceso(x, env, componentes)
        yield (env.timeout(otroTiempo))  # tiempo en crearse

def main(componentes):
         # Environment  # Componentes (RAM Y CPU)
       env.process(procesos(env, componentes))  # Se crean procesos
       env.run()
        
#Resultados requeridos
#referencia https://docs.python.org/3/library/statistics.html
env = simpy.Environment()
main(Componentes(env))
desviacion = statistics.stdev(tiempo) 
tiempoProm = statistics.mean(tiempo)         

print (", La desviacion Estandar: ", desviacion, ",El tiempo promedio es:  ", tiempoProm, )
    
                    
       
