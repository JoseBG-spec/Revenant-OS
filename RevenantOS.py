def asignarValoresProceso():
       global proceso,TE,procesoMs
       proceso = ["B", "D", "F", "H", "J","L","N","O","A","C","E","G","I","K","M","P","Ñ"]
       procesoMs=[0,0,0,0,1500,1500,1500,1500,3000,3000,3000,3000,3000,4000,4000,4000,8000]
       TE=[300,100,500,700,300,3000,50,600,400,50,1000,10,450,100,80,800,500]
       #print(len(proceso))
       #print(len(TE))

def asignarTCC(index,vacio,micro,tiempoInicial):
    global TCC,TF,TI,tiempoCambio,procesoMs

    #print("TF",TF)
    if(vacio==True):
        TCC[index]=0

    elif(index>0):
        #TCC[index]=tiempoCambio
        if microProcesadores[micro][len(microProcesadores[micro])-1].get("TF")>procesoMs[index]:
            #TI[index]=TF[index-1]
            TCC[index]=tiempoCambio
        if microProcesadores[micro][len(microProcesadores[micro])-1].get("TF")<procesoMs[index] or tiempoInicial!=0:
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
    if TE[index]>=tiempoQuantum:
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

    elif(vacio==True):
        TI[index]=0

    elif index>0 and tiempoInicial==0:
        TI[index]=microProcesadores[micro][len(microProcesadores[micro])-1].get("TF")
        #TI[index]=TF[index-1]

def asignarTF(index):
    global TF,TI,TT
    TF[index]=TI[index]+TT[index]

def asignarMicro(index):
    global microProcesadores,procesoMs
    micro=0;
    valoresFinales=[]
    tiempoInicial=0
    tiempoInicialCond=False

    for y in microProcesadores:
        if y:
            if(y[len(y)-1].get("TF")<procesoMs[index]):
                tiempoInicial=procesoMs[index]
                micro=microProcesadores.index(y)
                tiempoInicialCond=True
                return micro, False,tiempoInicial,tiempoInicialCond
                break


    for x in microProcesadores:
        if not x:
            micro=microProcesadores.index(x)

            return micro, True,0,tiempoInicialCond
            break
        else:
            valoresFinales.append(x[len(x)-1].get("TF"))

    micro=valoresFinales.index(min(valoresFinales))


    '''if(max(valoresFinales)<procesoMs[index] and min(valoresFinales)<procesoMs[index]):
        tiempoInicial=procesoMs[index]
        micro=0

    elif min(valoresFinales)<procesoMs[index]:
        tiempoInicial=procesoMs[index]'''


    #print(valoresFinales)
    #print(min(valoresFinales))

    return micro, False,tiempoInicial,tiempoInicialCond

def asignarPorMicro():
    procesos,TCC,TE,TVC,TB,TT,TI,TF=[],[],[],[],[],[],[],[]
    dicccccc=[]
    for micros in microProcesadores:
        procesos,TCC,TE,TVC,TB,TT,TI,TF=[],[],[],[],[],[],[],[]
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
        #print(dict)
        dicccccc.append(dict)


    return dicccccc

def asignarPorMicroTkinter():
    inx=1
    dicGUI.clear()
    tempDic=[[] for _ in range(18)]
    for micros in microProcesadores:
        tempDic[0]=["Proceso","TCC","TE","TVC","TB","TT","TI","TF"]
        for x in micros:
            for y in x:
                tempDic[inx].append(x.get(y))
            inx+=1
        tempDic2 = [x for x in tempDic if x != []]
        #print(tempDic2)
        dicGUI.append(tempDic2)
        tempDic=[[] for _ in range(18)]
        inx=1
def agregarEspacioEnBlanco(tiempoInicial,micro):
    dictPerProcess1 = {"Proceso": 'Vacio',
           "TCC": '',
           "TE": '',
           "TVC": '',
            "TB": '',
            "TT": '',
            "TI": microProcesadores[micro][len(microProcesadores[micro])-1].get("TF"),
            "TF": tiempoInicial
                          }
    return dictPerProcess1

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import math as math


proceso=[0 for _ in range(17)]
procesoMs=[0 for _ in range(17)]
TCC= [0 for _ in range(17)]
TE=[0 for _ in range(17)]
TVC=[0 for _ in range(17)]
TB=[0 for _ in range(17)]
TT=[0 for _ in range(17)]
TI=[0 for _ in range(17)]
TF=[0 for _ in range(17)]
noProcesadores=0
tiempoQuantum=0
tiempoBloqueo=0
tiempoCambio=0
dicGUI=[]


'''print("¿Cuantos microrocesadores son?:")
noProcesadores=int(input())
print("Tiempo duración de cada Quantum:")
tiempoQuantum=int(input())
print("Tiempo de bloqueo:")
tiempoBloqueo=int(input())
print("Tiempo de cambio:")
tiempoCambio=int(input())'''
microProcesadores=[]
def iniciarProceso():
    global microProcesadores
    microProcesadores.clear()
    microProcesadores=[[] for y in range(noProcesadores)]

    index=0
    asignarValoresProceso()
    for proc in proceso:
        microAsignado,vacio,tiempoInicial,cambiodeTiempoInicial = asignarMicro(index)
        if(cambiodeTiempoInicial==True):
            tabla = agregarEspacioEnBlanco(tiempoInicial,microAsignado)
            microProcesadores[microAsignado].append(tabla)
        #print(microAsignado,vacio)
        asignarTCC(index,vacio,microAsignado,tiempoInicial)
        #print(proceso[index])
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

    asignarPorMicroTkinter()
brics=[]

#actualDic=asignarPorMicro()
#print(actualDic)
#for p in actualDic:
    #brics.append(pd.DataFrame(p))

#for i in brics:
    #print(i)
    #print("------------------------------------------------------------------------------------------")
#print("----------------")
#print(TCC)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''                                                              GUI                                                                                          '''
class Table:

    def __init__(self,root):
        x=0
        columns=0
        tabla=0
        for p in dicGUI:
            xp=x+1
            tabla=tabla+1
            total_rows = len(p)
            total_columns = len(p[0])
            for i in range(xp,total_rows+xp):
                for j in range(total_columns):

                    self.e = Entry(root, width=dimensionX//(total_columns*13), fg='black', font=('URW Gothic L',14,'bold'))

                    if i!=xp:
                        self.e.grid(row=i, column=j)
                        x=i
                    else:
                        self.k = Entry(root, width=dimensionX//(total_columns*13), fg='green', font=('URW Gothic L',14,'bold'))
                        self.k.grid(row=i, column=total_columns+1,padx=0,pady=10)
                        self.k.insert(END, "Micro "+str(tabla))
                        self.e = Entry(root, width=dimensionX//(total_columns*13), fg='blue', font=('URW Gothic L',14,'bold'))
                        self.e.grid(row=i, column=j,padx=0,pady=10)
                        #print("yay")

                    self.e.insert(END, p[i-xp][j])
        #print(x)


def createTable():
    borrar()
    iniciarProceso()
    w= Frame(tab2)
    #w.pack(side=LEFT,fill=Y)
    canvas = Canvas(w)
    canvas.config(width=950, height=800)

    s=Scrollbar(w,orient="vertical",command=canvas.yview)
    #s.pack(side=RIGHT,fill=Y)

    scrollable_frame = ttk.Frame(canvas,width=950, height=800)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=s.set)

    t=(Table(scrollable_frame))

    w.pack()
    canvas.pack(side="left", fill="both", expand=True)
    s.pack(side="right", fill="y")


def checarDatos():
    global noProcesadores,tiempoQuantum,tiempoBloqueo,tiempoCambio
    if entry1.get().isnumeric()==True and entry2.get().isnumeric()==True and entry3.get().isnumeric()==True and entry4.get().isnumeric()==True:
        noProcesadores=int(entry1.get())
        tiempoQuantum=int(entry2.get())
        tiempoBloqueo=int(entry3.get())
        tiempoCambio=int(entry4.get())
        createTable()

    else:
        messagebox.showinfo('Advertencia','Favor de llenar todos los campos con datos númericos')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')

def borrar():
    global tab2
    tab2.destroy()
    #tab_control.forget(tab2)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Tabla(s)')
    #s=Scrollbar(tab2)
    #s.pack(side=RIGHT,fill=Y)
#GUI
dimensionX,dimensionY=1000,800
t=0
root = Tk()
root.title("Microprocesadores")
root.geometry('1000x800')
s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L','17','bold') )
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
w= Frame(tab2)
#s=Scrollbar(tab2)
#s.config( command = w.winfo_height())


lbl = Label(tab1, text="Ingresa el numero de microprocesadores", font=('URW Gothic L',14,'bold'))
lbl.pack(side=TOP)
entry1=Entry(tab1, font=('URW Gothic L',14,'bold'))
entry1.pack(side=TOP)
entry1.focus()
lb2 = Label(tab1, text="Ingresa la duración de cada Quantum", font=('URW Gothic L',14,'bold'))
lb2.pack(side=TOP)
entry2=Entry(tab1, font=('URW Gothic L',14,'bold'))
entry2.pack(side=TOP)
lb3 = Label(tab1, text="Ingresa el tiempo de bloqueo", font=('URW Gothic L',14,'bold'))
lb3.pack(side=TOP)
entry3=Entry(tab1, font=('URW Gothic L',14,'bold'))
entry3.pack(side=TOP)
lb4 = Label(tab1, text="Ingresa el tiempo de cambio", font=('URW Gothic L',14,'bold'))
lb4.pack(side=TOP)
entry4=Entry(tab1, font=('URW Gothic L',14,'bold'))
entry4.pack(side=TOP)
btn = Button(tab1, text="Crear Tabla",font=('URW Gothic L',14,'bold'),command=checarDatos)
btn.pack(side=TOP)
btn2 = Button(tab1, text="Borrar Tabla",font=('URW Gothic L',14,'bold'),command=borrar)
btn2.pack(side=TOP)

tab_control.add(tab1, text='Datos Generales')
tab_control.add(tab2, text='Tabla(s)')

tab_control.pack(expand=1, fill='both')



#s.pack(side=RIGHT,fill= Y)


root.mainloop()

