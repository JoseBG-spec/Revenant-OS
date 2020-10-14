noProcesadores=0
proceso=[0 for _ in range(17)]
procesoMs=[0 for _ in range(17)]
TCC= [0 for _ in range(17)]
TE=[0 for _ in range(17)]
TVC=[0 for _ in range(17)]
TB=[0 for _ in range(17)]
TT=[0 for _ in range(17)]
TI=[0 for _ in range(17)]
TF=[0 for _ in range(17)]
tiempoQuantum=0
tiempoBloqueo=0
tiempoCambio=0

def asignarValoresProceso():
       global proceso,TE,procesoMs
       proceso = ["B", "D", "F", "H", "J","L","N","O","A","C","E","G","I","K","M","P","Ñ"]
       procesoMs=[0,0,0,0,1500,1500,1500,1500,3000,3000,3000,3000,3000,4000,4000,4000,8000]
       TE=[300,100,500,700,300,3000,50,600,400,50,1000,10,450,100,80,800,500]
       #print(len(proceso))
       #print(len(TE))

def asignarTCC(index,vacio):
    global TCC,TF,TI,tiempoCambio,procesoMs

    #print("TF",TF)
    if(vacio==True):
        TCC[index]=0

    elif(index>0):
        #TCC[index]=tiempoCambio
        if TF[index-1]>procesoMs[index]:
            #TI[index]=TF[index-1]
            TCC[index]=tiempoCambio
        if TF[index-1]<procesoMs[index]:
            #TI[index]=procesoMs[index]
            TCC[index]=0

def asignarTiempoBloqueo(index):
    global TE,TB,tiempoBloqueo

    #TB=[20,20,30,40,20,50,20,30,20,20,50,20,30,20,20,40,30]

    if 1<=TE[index]<=400:
        TB[index]=2*tiempoBloqueo
    elif 401<=TE[index]<=600:
        TB[index]=3*tiempoBloqueo
    elif 601<=TE[index]<=800:
        TB[index]=4*tiempoBloqueo
    elif 801<=TE[index]<=10000:
        TB[index]=5*tiempoBloqueo

def asignarTVC(index):
    global TVC,TE,tiempoQuantum,tiempoBloqueo
    x=0
    if TE[index]>tiempoQuantum:
        x=TE[index]/tiempoQuantum
        x=math.ceil(x)
        x-=1
        TVC[index]=x*tiempoBloqueo
    elif TE[index]<tiempoQuantum:
        TVC[index]=0

def asignarTT(index):
    global TCC,TE,TVC,TB,TT
    TT[index]=TCC[index]+TE[index]+TVC[index]+TB[index]

def asignarTI(index,vacio,micro,tiempoInicial):
    global TI,TF,microProcesadores
    if(tiempoInicial!=0):
        TI[index]=tiempoInicial
    if(vacio==True):
        TI[index]=0
    elif index>0:
        TI[index]=microProcesadores[micro][len(microProcesadores[micro])-1].get("TF")
        #TI[index]=TF[index-1]

def asignarTF(index):
    global TF,TI,TT
    TF[index]=TI[index]+TT[index]

def asignarMicro(index):
    global microProcesadores,procesoMs
    micro=0;
    valoresFinales=[]
    for x in microProcesadores:
        if not x:
            micro=microProcesadores.index(x)
            return micro, True,0
            break
        else:
            valoresFinales.append(x[len(x)-1].get("TF"))
    micro=valoresFinales.index(min(valoresFinales))
    tiempoInicial=0
    print(valoresFinales)
    print(min(valoresFinales))
    if(min(valoresFinales)<procesoMs[index]):
        tiempoInicial=procesoMs[index]

    return micro, False,tiempoInicial

def asignarPorMicro():
    procesos,TCC,TE,TVC,TB,TT,TI,TF=[],[],[],[],[],[],[],[]
    dicccccc=[]
    for micros in microProcesadores:
        for x in micros:
             procesos.append(x.get("Proceso"))
             TCC.append(x.get("TCC"))
             TE.append(x.get("TE"))
             TVC.append(x.get("TVC"))
             TB.append(x.get("TB"))
             TT.append(x.get("TT"))
             TI.append(x.get("TI"))
             TF.append(x.get("TF"))
        dict = {"Proceso": procesos,
       "TCC": TCC,
       "TE": TE,
       "TVC": TVC,
        "TB": TB,
        "TT": TT,
        "TI": TI,
        "TF": TF}
        print(dict)
        dicccccc.append(dict)


    return dicccccc





from tkinter import *
import pandas as pd
import math as math


'''class Table:

    def __init__(self,root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()'''

print("¿Cuantos microrocesadores son?:")
noProcesadores=int(input())
print("Tiempo duración de cada Quantum:")
tiempoQuantum=int(input())
print("Tiempo de bloqueo:")
tiempoBloqueo=int(input())
print("Tiempo de cambio:")
tiempoCambio=int(input())

microProcesadores=[[] for y in range(noProcesadores)]

index=0
asignarValoresProceso()
for proc in proceso:

    microAsignado,vacio,tiempoInicial = asignarMicro(index)
    print(microAsignado,vacio)
    asignarTCC(index,vacio)
    asignarTI(index,vacio,microAsignado,tiempoInicial)
    asignarTVC(index)
    asignarTiempoBloqueo(index)
    asignarTT(index)
    asignarTF(index)

    dictPerProcess = {"Proceso": proceso[index],
       "TCC": TCC[index],
       "TE": TE[index],
       "TVC": TVC[index],
        "TB": TB[index],
        "TT": TT[index],
        "TI": TI[index],
        "TF": TF[index]
                      }

    microProcesadores[microAsignado].append(dictPerProcess)
    #print("TCC",index,TCC)
    index+=1

actualDic=asignarPorMicro()

brics=[]
for p in actualDic:
    brics.append(pd.DataFrame(p))

for i in brics:
    print(i)
    print("------------------------------------------------------------------------------------------")
#print("----------------")
#print(TCC)

