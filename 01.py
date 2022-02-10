#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:17:46 2022

@author: artutaraperegmail.com
"""
#se corresponde con la propuesta 1. tenemos 8 programas ejecutandose a la vez con la función task. No entran dos a la vez en la seccion critica pero si se ejecutan a la vez,
#esto es lo conseguimos con el turn. cuando es turn 1 se mete en la secc critica del primero y los otros 7 en la seccion no critica.
#hay 8 procesos que se ejecutan 100 veces 800 veces en total.
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8 #Hay 8 procesos
def task(common, tid, turn):
    a = 0
    for i in range(100): #numero de veces que iteras 
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        while turn.value!=tid:
           pass
        print(f'{tid}−{i}: Critical section') #la sección crítica es lo que hace el programa que en este caso es aumentar contador
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        turn.value = (tid + 1) % N
def main():
    lp = []
    common = Value('i', 0) #variables compartidas las paso por argumento
    turn = Value('i', 0) #variables compartidas las paso por argumento
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, turn))) #creo una lista con los 8 procesos.
    print (f"Valor inicial del contador {common.value}")
    for p in lp: #En este punto empiezan a ejecutarse los 8 a la vez
        p.start() #Barra vertical que separa los procesos
    for p in lp:
        p.join()  #Esperar a que acaben todos
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
   main()