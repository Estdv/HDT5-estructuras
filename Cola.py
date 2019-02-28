#UVG Algoritmos y estructuras de datos
#Cola.py
#Autores: Luis Quezada 18028 & Esteban del Valle 18221
#Fecha: 1 de marzo 2019


def Enqueue(x, head, tail, cola[], procesos):
    if (((tail + 1)% proceos) == head):
        print("Cola llena")
        return
    
    elif (isEmpty(head, tail)):
        head = 0
        tail = 0

    else:
        tail = (tail + 1)%procesos
        
    cola[tail] = x
    

        
def Dequeue(head, tail, cola[], procesos):
    if (isEmpty(head, tail, procesos)):
        print("Cola vacia")
        return

    elif (head == tail):
        head = -1
        tail = -1

    else:
        del cola[head]
        head = (head + 1) % procesos




def front(cola, head):
    if(head >= 0):
        return cola[head]
    else:
        print("Cola vacia")



def isEmpty(head, tail):
    if((head == -1) and (tail == -1)):
        return True
    else:
        return False

