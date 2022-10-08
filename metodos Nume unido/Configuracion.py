"""
    Este archivo se encarga de contener cada interfaz de los distintos metodos de la  aplicacion
    Cada clase hereda las caracterisiticas de ttk.Frame y asi mismo les paso los estilos como Er
    que guarda los colores a usar.

    Casi todas las clases son lo mismo los datos que piden los  botones y una tabla para  mostrar 
    los Resultados, los valores ingresados se recogen al  llamar a calcular y se lo  envia a  las 
    funciones guardadas en Metodos.py.
"""

from binascii import Error
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import random
import time
import threading
import Metodos as mt
import BDColores as Bd

#Es la imagen del pollito
imagen_p = ""

class Metodo_Grafico(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()
        

    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 230)
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 230)

        #RadioBotones :v

        self.variable = StringVar()
        self.variable.set(2) #Lo colocamos en No

        self.radiobutton1 = ttk.Radiobutton(self,text=" Si ", variable=self.variable, command = self.Mostrar_Intervalos, value=1)
        self.radiobutton1.place(x=140,y=150)
        self.radiobutton2 = ttk.Radiobutton(self,text=" No ", variable=self.variable, command = self.Ocultar_Intervalos, value=2)
        self.radiobutton2.place(x=180,y=150)


    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 67,font= self.Er.Letra3)
        self.entryFormula.place(x = 140, y = 105)
        self.entryCantidadP = Entry(self,text="",fg="black",bg="white",width = 7 ,font= self.Er.Letra3 ,justify='center')
        self.entryCantidadP.place(x = 140, y = 185)
        #Intervalos dinamicos
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        
    
    def Crear_Label(self):

        label = ttk.Label(self, text ="Metodo Gráfico",         font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y=20)
        label = ttk.Label(self, text ="Tabla de contenido",     font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=265)

        label = ttk.Label(self, text ="Formula             :",  font =  self.Er.Letra3, width = 16 ).place(x = 20, y=106)
        label = ttk.Label(self, text ="Intervalo            :", font =  self.Er.Letra3, width = 16 ).place(x = 20, y=146)
        label = ttk.Label(self, text ="Cant. de Puntos :",      font =  self.Er.Letra3, width = 16 ).place(x=20, y=186)
        
        

        #Intervalos dinamicos
        self.labelIA = ttk.Label(self, text ="Intervalo a :",font =  self.Er.Letra3, width = 15 )
        self.labelIB = ttk.Label(self, text ="Intervalo b :",font =  self.Er.Letra3, width = 15 )
        
    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=11, columns=('y'))
        self.table.place(x=8, y=300)

        
        self.table.heading('#0',text="X",anchor = CENTER)
        self.table.column('#0',width=300, anchor=CENTER)
        self.table.heading('y',text="Y",anchor = CENTER)
        self.table.column('y',width=300, anchor=CENTER)
    

    def Mostrar_Intervalos(self):
        
        #Lo colocamos en el lugar debido
        self.labelIA.place(x = 275, y=150)
        self.labelIB.place(x = 455, y=150)
        self.entryInterA.place(x = 360, y = 150)
        self.entryInterB.place(x = 540, y = 150)
    
    def Ocultar_Intervalos(self):
        
        #Limpiamos los entry y los mandamos al tercer cielo
        
        self.labelIA.place(x = 220, y=945)
        self.labelIB.place(x = 420, y=945)
        self.entryInterA.place(x = 320, y = 945)
        self.entryInterB.place(x = 520, y = 945)

        #Limpiar 
        self.entryInterA.delete(0, 'end')
        self.entryInterB.delete(0, 'end')


    def Calcular_M(self):
        
        formu =  self.entryFormula.get() 
        ina = -100
        inb = 100
        cant = self.entryCantidadP.get()

        if self.variable.get() == '1':
            
            ina = self.entryInterA.get()
            inb = self.entryInterB.get()

            try:
                ina =  eval(ina)
                inb =  eval(inb)
            except:
                ina =  -100
                inb =  100
                print("Error a")
        
        
        val_x , val_y = mt.Metodo_Grafico(formu,ina,inb,int(cant))
        
        self.Actualizar_tabla(val_x,val_y)
        mt.Graficar("Metodo Gráfico",formu,ina , inb,int(cant))
        

    
    def Actualizar_tabla(self,x,y):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 

        try:
            
            
            for fila in range(len(x)):
                
                self.table.insert("",'end',text= round(x[fila],2), values=(round(y[fila],2)))
        except:
            print("error")
            pass
    
    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.entryCantidadP.delete(0,END)

class Configuracion_Color(ttk.Frame):
    
    

    def __init__(self,Padre,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Pd = Padre

        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_Combobox()
        self.Crear_tabla_Color()
        
    
    def Crear_Label(self):
        #Titulo
        ttk.Label(self, text ="Configuracion",font =  self.Er.Letra, width = 42 , anchor = "center").place(x = 0, y=20)
        #Subtitulos
        ttk.Label(self, text ="Creador de Colores",font =  self.Er.Letra3, width = 28 , anchor = "nw").place(x = 20, y=80)
        ttk.Label(self, text ="Color",font =  self.Er.Letra3, width = 26 , anchor = "nw").place(x = 350, y=80)
        
        ttk.Label(self, text ="Colores de la Interfaz",font =  self.Er.Letra3, width = 28 , anchor = "nw").place(x = 20, y=210)
        ttk.Label(self, text ="Color #1 :",font =  self.Er.Letra3, width = 10 , anchor = "nw").place(x = 20, y=242)
        ttk.Label(self, text ="Color #2 :",font =  self.Er.Letra3, width = 10 , anchor = "nw").place(x = 20, y=272)
        ttk.Label(self, text ="Color #3 :",font =  self.Er.Letra3, width = 10 , anchor = "nw").place(x = 20, y=302)

        ttk.Label(self, text ="Colores Guardados:",font =  self.Er.Letra3, width = 26 , anchor = "nw").place(x = 20, y=357)


        self.LabelColor1 = ttk.Label(self, text ="",font =  self.Er.Letra2, width = 6 , anchor = "nw",background  = self.Er.Primario,borderwidth = 2,relief="ridge")
        self.LabelColor1.place(x = 120, y=240)
        self.LabelColor2 = ttk.Label(self, text ="",font =  self.Er.Letra2, width = 6 , anchor = "nw",background  = self.Er.Secundario,borderwidth = 2,relief="ridge")
        self.LabelColor2.place(x = 120, y=270)
        self.LabelColor3 = ttk.Label(self, text ="",font =  self.Er.Letra2, width = 6 , anchor = "nw",background  = self.Er.Terciario,borderwidth = 2,relief="ridge")
        self.LabelColor3.place(x = 120, y=300)



        self.Cuadro_Color = ttk.Label(self, text ="\n\n\n\n", width = 30 ,background="#FFFFFF",borderwidth = 2,relief="ridge")
        self.Cuadro_Color.place(x = 350, y=105)
        

    def Crear_Combobox(self):
        self.combo = ttk.Combobox(self,width = 39,height = 100,state="readonly")
        self.combo.place(x = 20, y =385)

        self.combo.bind("<<ComboboxSelected>>",lambda x: self.Combo_Seleccion())
        self.Actualizar_Combo_box()
        

    def Crear_Entry(self):
        self.rojo_F = Entry(self,text="",bg="white",width=5,font=self.Er.Letra3,justify='center')
        self.rojo_F.place(x=230,y=105)

        self.azul_F = Entry(self,text="",bg="white",width=5,font=self.Er.Letra3,justify='center')
        self.azul_F.place(x=230,y=135)

        self.verde_F = Entry(self,text="",bg="white",width=5,font=self.Er.Letra3,justify='center')
        self.verde_F.place(x=230,y=165)
        
        self.Name_c = Entry(self,text="",bg="white",width=26,font=self.Er.Letra3,justify='center')
        self.Name_c.place(x=350,y=385)

        self.rojo_F.insert(0,250)
        self.azul_F.insert(0,250)
        self.verde_F.insert(0,250)

        self.rojo_F.bind ("<KeyRelease>",lambda x: self.click(self.sred,self.rojo_F))
        self.verde_F.bind("<KeyRelease>",lambda x: self.click(self.sgreen,self.verde_F))
        self.azul_F.bind ("<KeyRelease>",lambda x: self.click(self.sblue,self.azul_F))

    
    def Crear_Botones(self):

        image = Image.open("Imagenes/IconoLuna.png")
        sol =  Image.open("Imagenes/IconoSol.png")
        
        
        resize_image = image.resize((45, 45))
        sol_re = sol.resize((45, 45))
        

        self.imge = ImageTk.PhotoImage(resize_image)
        self.sole = ImageTk.PhotoImage(sol_re)
        
        self.BotonSol = Button(self, text = '1', image = self.sole,background = self.Er.Color_Oscuro ,command = self.Cambiar_Icono_Boton,borderwidth = 0)
        self.BotonSol.place(x=1000,y = 20)
        self.BotonLuna = Button(self, text = '2', image = self.imge,background = self.Er.Color_claro ,command = self.Cambiar_Icono_Boton,borderwidth = 0)
        self.BotonLuna.place(x=1000,y = 20)

        if self.Er.Fondo == self.Er.Color_Oscuro:
            
            self.BotonSol.place(x=555,y = 20)
        else:
            
            self.BotonLuna.place(x=555,y = 20)

        #catch
        self.BotonColor1 = ttk.Button(self, text = 'catch',width =7, command =  lambda : self.Atrapar_Color(self.LabelColor1))
        self.BotonColor1.place(x=215,y=240)
        self.BotonColor2 = ttk.Button(self, text = 'catch',width =7, command =  lambda : self.Atrapar_Color(self.LabelColor2))
        self.BotonColor2.place(x=215,y=270)
        self.BotonColor3 = ttk.Button(self, text = 'catch',width =7, command =  lambda : self.Atrapar_Color(self.LabelColor3))
        self.BotonColor3.place(x=215,y=300)

        #Guardar
        self.BotonAplicar = ttk.Button(self, text = 'Aplicar',width =20,command =  self.Aplicar_Cambios)
        self.BotonAplicar.place(x=370,y=240)
        self.BotonGuardar = ttk.Button(self, text = 'Guardar',width =20,command =  self.Guardar_Color)
        self.BotonGuardar.place(x=370,y=415)
        self.BotonRandom = ttk.Button(self, text = 'Random',width =20,command =  self.Randomizar)
        self.BotonRandom.place(x=370,y=270)

        self.BotonEliminar = ttk.Button(self, text = 'Eliminar',width =20,command =  self.Eliminar_Lista)
        self.BotonEliminar.place(x=70,y=415)



    def formularios(self,auxiliar,num):
        
        try:
            num = int(num)
            auxiliar.delete(0,END)
            auxiliar.insert(0,num)
        except:
            print("Error entry")
            pass
        
        self.click()
    
    def click(self,Escala = None,Caja = None):
        i,j,k = 0,0,0


        if Escala != None:
            try:
                valor = int(Caja.get())
                Escala.set(valor)
                i=int(valor)

                if i > 250 : i = 250
                if i < 0 :  i = 0
            except:
                Escala.set(0)
                Caja.insert(0,0)
        
        try:
            i = int(self.rojo_F.get())
            j = int(self.azul_F.get())
            k = int(self.verde_F.get())
        
        except:
        
            self.rojo_F.insert(0,0)
            self.azul_F.insert(0,0)
            self.verde_F.insert(0,0)
            pass
    
        color_c='#%02x%02x%02x' % (i, k, j)
        self.Cuadro_Color["background"] =  color_c

    def Crear_tabla_Color(self):
        self.sred = ttk.Scale(self, from_=0, to=250, length=200,orient=HORIZONTAL,value = 250,style="Red.Horizontal.TScale")
        self.sred["command"] = lambda x: self.formularios(self.rojo_F,self.sred.get())
        self.sred.place(x=20,y =105)

        self.sblue = ttk.Scale(self, from_=0, to=250, length=200,orient=HORIZONTAL,value = 250,style = "Blue.Horizontal.TScale")
        self.sblue["command"] = lambda x: self.formularios(self.azul_F,self.sblue.get())
        self.sblue.place(x=20,y =135)

        self.sgreen = ttk.Scale(self, from_=0, to=250, length=200,orient=HORIZONTAL,value = 250,style = "Green.Horizontal.TScale")
        self.sgreen["command"] = lambda x: self.formularios(self.verde_F,self.sgreen.get())
        self.sgreen.place(x=20,y =165)

    #funcion que cambia el tema de dia a noche.
    def Cambiar_Icono_Boton(self):
        global imagen_p

        #Esta en light
        if self.Er.Fondo == self.Er.Color_claro:
            
            #Cambia a dark
            self.Er.Fondo = self.Er.Color_Oscuro
            self.Er.FondoLetra = "white"

            self.BotonSol.place(x=555,y = 20)
            self.BotonLuna.place(x=1000,y = 20)
            
            
        else:
            #Cambia light
            self.Er.Fondo = self.Er.Color_claro
            self.Er.FondoLetra = "black"

            self.BotonSol.place(x=1000,y = 20)
            self.BotonLuna.place(x=555,y = 20)

        
        imagen_p["background"] = self.Er.Fondo

        Bd.Guardar_Color(str(self.Er.Primario)+"-"+str(self.Er.Secundario)+"-"+str(self.Er.Terciario),str(self.Er.Fondo))
        self.Pd.Crear_Estilos()
    
    def Atrapar_Color(self,Cuadro):
        i,j,k =  self.rojo_F.get(),self.azul_F.get(),self.verde_F.get()
        color = self.Cuadro_Color["background"]
        Cuadro["background"] = color
        
    
    def Aplicar_Cambios(self):
        self.Er.Primario   = str(self.LabelColor1["background"])
        self.Er.Secundario = str(self.LabelColor2["background"])
        self.Er.Terciario  = str(self.LabelColor3["background"])
        

        Bd.Guardar_Color(str(self.Er.Primario)+"-"+str(self.Er.Secundario)+"-"+str(self.Er.Terciario),str(self.Er.Fondo))
        self.Pd.Crear_Estilos()

    def Actualizar_Combo_box(self):
        lista = []
        

        datos = Bd.Retornar_Todo()
        

        for i in datos:
            lista.append(i[1])
        self.combo["values"] = lista
    
    def Guardar_Color(self):
        a  = self.LabelColor1["background"]
        b = self.LabelColor2["background"]
        c  = self.LabelColor3["background"]
        Nombre  = self.Name_c.get()
        self.Name_c.delete(0,END)

        if Nombre == "":
            Nombre = "Sin Nombre "
        trio =  str(a) + "-" + str(b)  + "-" +str(c)  
        Bd.Insertar_Color(Nombre,trio)
        self.Actualizar_Combo_box()
    
    def Combo_Seleccion(self):
        frase = self.combo.get()
        
        frase = Bd.Retornar_Todo("where Nombre = '{}'".format(frase))
        
        frase =  frase[0][2].split("-")
        
        self.Er.Primario   = frase[0]
        self.Er.Secundario = frase[1]
        self.Er.Terciario  = frase[2]

        self.LabelColor1["background"] = frase[0]
        self.LabelColor2["background"] = frase[1]
        self.LabelColor3["background"] = frase[2]
        

        Bd.Guardar_Color(str(self.Er.Primario)+"-"+str(self.Er.Secundario)+"-"+str(self.Er.Terciario),str(self.Er.Fondo))
        self.Pd.Crear_Estilos()
        self.Actualizar_Combo_box()


    def Randomizar(self):
        frase = []
        for x in range(3):
            i,j,k = random.randint(0,250),random.randint(0,250),random.randint(0,250)
            color_c='#%02x%02x%02x' % (i, k, j)
            frase.append(color_c)
        
        self.Er.Primario   = frase[0]
        self.Er.Secundario = frase[1]
        self.Er.Terciario  = frase[2]

        self.LabelColor1["background"] = frase[0]
        self.LabelColor2["background"] = frase[1]
        self.LabelColor3["background"] = frase[2]
        self.Pd.Crear_Estilos()

    def Eliminar_Lista(self):
        frase = self.combo.get()
        
        frase = Bd.Retornar_Todo("where Nombre = '{}'".format(frase))
        
        if frase != []:
            
            if frase[0][0] > 3:
                Bd.Eliminar_Color(frase[0][1])

        self.Actualizar_Combo_box()
                
class Metodo_biseccion(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()

    def Crear_Label(self):

        
        label   = ttk.Label(self, text ="Metodo de la Biseccion",         font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y=20)
        label   = ttk.Label(self, text ="Formula      :",  font =  self.Er.Letra3, width = 16 ).place(x = 20, y=106)
        labelIA = ttk.Label(self, text ="Intervalo a  :",font =  self.Er.Letra3, width = 15 ).place(x = 20, y=146)
        labelIB = ttk.Label(self, text ="Intervalo b  :",font =  self.Er.Letra3, width = 15 ).place(x = 220, y=146)
        label   = ttk.Label(self, text ="Max Error Permitido :",      font =  self.Er.Letra3, width = 20 ).place(x=20, y=186)
        label  = ttk.Label(self, text ="Tabla de contenido",     font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=265)

    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 230)
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 230)
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 70,font= self.Er.Letra3)
        self.entryFormula.place(x = 120, y = 105)
        self.entryErrorMax = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.entryErrorMax.place(x = 165, y = 185)
        
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterA.place(x = 120, y = 146)
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB.place(x = 320, y = 146)

    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.entryErrorMax.delete(0,END)
        pass

    def Calcular_M(self):
        Form = self.entryFormula.get()
        Ia = self.entryInterA.get()
        Ib = self.entryInterB.get()
        Error = self.entryErrorMax.get()

        error , x ,y = 0,0,0

        try:
            error , x ,y = mt.metodo_biseccion(Form,float(Ia),float(Ib),float(eval(Error)))

            self.Actualizar_tabla(error,x,y)
            
            
        except:
            print("Error de ingresar datos")
            pass
        mt.Graficar("Metodo de la biseccion",Form,float(Ia),float(Ib))
        


    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=11, columns=('x','y','Error'))
        self.table.place(x=8, y=300)

        
        self.table.heading('#0',text="Pasos",anchor = CENTER)
        self.table.column('#0',width=150, anchor=CENTER)
        self.table.heading('x',text="X",anchor = CENTER)
        self.table.column('x',width=150, anchor=CENTER)
        self.table.heading('y',text="F(x)",anchor = CENTER)
        self.table.column('y',width=150, anchor=CENTER)
        self.table.heading('Error',text="|x(i) - x(i-1)|",anchor = CENTER)
        self.table.column('Error',width=150, anchor=CENTER)
        
    
    def Actualizar_tabla(self,error,x,y):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 

        try:
            
            
            for fila in range(len(error)):
                
                self.table.insert("",'end',text= fila, values=(round(x[fila],10),round(y[fila],10),round(error[fila],10)))
        except:
            print("error")
            pass

class Metodo_Euler(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()
    

    def Crear_Label(self):
        label   = ttk.Label(self, text ="Metodo de Euler",    font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y = 20)
        label   = ttk.Label(self, text ="F(x)'  :",           font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 106)
        labelIA = ttk.Label(self, text ="x(0)   :",           font =  self.Er.Letra3, width = 20 ).place(x = 20, y= 146)
        labelIB = ttk.Label(self, text ="x final               :", font =  self.Er.Letra3, width = 20 ).place(x = 180, y = 146)
        label   = ttk.Label(self, text ="y(0)  :",            font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 186)
        label   = ttk.Label(self, text ="Cant. de Pasos :",   font =  self.Er.Letra3, width = 20 ).place(x = 180, y = 186)

        label  = ttk.Label(self, text ="Tabla de contenido",    font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=285)#20
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 77,font= self.Er.Letra3)
        self.entryFormula.place(x = 70, y = 105)

        self.x0 = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.x0.place(x = 70, y = 185)
        self.CantidadPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.CantidadPasos.place(x = 295, y = 185)
        
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterA.place(x = 70, y = 146)
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB.place(x = 295, y = 146)


    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 240) #10
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 240)
    
    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=10, columns=('y'))
        self.table.place(x=8, y=320)

        
        self.table.heading('#0',text="x",anchor = CENTER)
        self.table.column('#0',width=300, anchor=CENTER)
        self.table.heading('y',text="F(x)",anchor = CENTER)
        self.table.column('y',width=300, anchor=CENTER)
    
    def Actualizar_tabla(self,x,y):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 

        try:
            
            
            for fila in range(len(x)):
                
                self.table.insert("",'end',text= round(x[fila],10), values=(round(y[fila][0],10)))
        except:
            print("error")
            pass
    def Calcular_M(self):
        Form = self.entryFormula.get()
        Ia = self.entryInterA.get()
        Ib = self.entryInterB.get()
        Cantidad = self.CantidadPasos.get()
        X0 = self.x0.get()

        x,y = 0,0

        
        x ,y = mt.Metodo_Euler([float(Ia),float(Ib)],[float(X0)],Form,int(Cantidad))

        self.Actualizar_tabla(x,y)
        mt.Graficar_Euler("Metodo de Euler",Form,x,y)
    
    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.CantidadPasos.delete(0,END)
        self.x0.delete(0,END)
        
class Metodo_Newton(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()
    
    def Crear_Label(self):
        label   = ttk.Label(self, text ="Metodo de Newton-Raphson",    font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y = 20)
        label   = ttk.Label(self, text ="Funcion  :",           font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 106)
        label   = ttk.Label(self, text ="X(0)  \t:",            font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 146)
        label   = ttk.Label(self, text ="Max. Error Permitido :",   font =  self.Er.Letra3, width = 20 ).place(x = 180, y = 146)

        label  = ttk.Label(self, text ="Tabla de contenido",    font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=285)
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 72,font= self.Er.Letra3)
        self.entryFormula.place(x = 90, y = 105)

        self.x0 = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.x0.place(x = 90, y = 146)
        self.CantidadPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.CantidadPasos.place(x = 330, y = 146)
    
    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command= self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 230)
        self.Borrar = ttk.Button(self, text="Limpiar",command= self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 230)

    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=10, columns=('x','y','error'))
        self.table.place(x=8, y=320)

        
        self.table.heading('#0',text="Pasos",anchor = CENTER)
        self.table.column('#0',width=150, anchor=CENTER)
        self.table.heading('x',text="X",anchor = CENTER)
        self.table.column('x',width=150, anchor=CENTER)
        self.table.heading('y',text="F(x)",anchor = CENTER)
        self.table.column('y',width=150, anchor=CENTER)
        self.table.heading('error',text="|x(i) - x(i-1)|",anchor = CENTER)
        self.table.column('error',width=150, anchor=CENTER)
    
    def Actualizar_tabla(self,tabla):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 


        contador = 0
        try:
            for fila in tabla:
                
                self.table.insert("",'end',text= contador, values=(round(fila[0],10),round(fila[1],10),round(fila[2],10)))
                contador += 1
        except:
            print("Error Tabla")
        
    def Calcular_M(self):
        Form = self.entryFormula.get()
        Cantidad = self.CantidadPasos.get()
        X0 = self.x0.get()

        
        tabla  =""

        try:
            tabla = mt.Metodo_Newton(Form,float(X0),float(Cantidad))
            #print(tabla)
            self.Actualizar_tabla(tabla)
            
        except:
            print("Error formula")

        rango_a  = float(X0)
        rango_b =  rango_a
        
        if rango_a < 0:
            rango_b *= -1
        else:
            rango_a *= -1


        mt.Dibujar_Lineas(tabla)
        mt.Graficar("Metodo de Newton-Raphson",Form,rango_a,rango_b)
    
    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.CantidadPasos.delete(0,END)
        self.x0.delete(0,END)
        
class Metodo_Taylor(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()
    
    def Crear_Label(self):
        label   = ttk.Label(self, text ="Metodo de Taylor",    font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y = 20)
        
        label   = ttk.Label(self, text ="Formula :",  font =  self.Er.Letra3, width = 16 ).place(x = 20, y=106)
        labelIA = ttk.Label(self, text ="Punto inicial           :",font =  self.Er.Letra3, width = 20 ).place(x = 20, y=146)
        labelIB = ttk.Label(self, text ="Iteraciones  :",font =  self.Er.Letra3, width = 15 ).place(x = 240, y=146) 
        #label   = ttk.Label(self, text ="Variable a utilizar :",      font =  self.Er.Letra3, width = 20 ).place(x=20, y=186)

        label  = ttk.Label(self, text ="Tabla de contenido",    font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=285)#20
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 74,font= self.Er.Letra3)
        self.entryFormula.place(x = 90, y = 105)

        self.x0 = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.x0.place(x = 160, y = 146)

        self.CantidadPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.CantidadPasos.place(x = 335, y = 146)
        
        #self.Simbolo= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        #self.Simbolo.place(x = 160, y = 185)
    
    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 240) #10
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 240)
    
    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=10, columns=('der','f(x)','termino'))
        self.table.place(x=8, y=320)

        
        self.table.heading('#0',text="Paso",anchor = CENTER)
        self.table.column('#0',width=50, anchor=CENTER)
        self.table.heading('der',text="F'n",anchor = CENTER)
        self.table.column('der',width=250, anchor=CENTER)
        self.table.heading('f(x)',text="F'n(x0)",anchor = CENTER)
        self.table.column('f(x)',width=50, anchor=CENTER)
        self.table.heading('termino',text="Termino",anchor = CENTER)
        self.table.column('termino',width=250, anchor=CENTER)
    
    def Actualizar_tabla(self,tabla):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 

        try:
            
            for fila in tabla:
                
                self.table.insert("",'end',text= fila[0], values=(fila[1],fila[2],fila[3]))
        except:
            print(tabla)
            print("error")
            pass
    
    def Calcular_M(self):
        Form = self.entryFormula.get()
        
        Cantidad = self.CantidadPasos.get()
        X0 = self.x0.get()

        x,y = 0,0

        
        x ,y = mt.Metodo_Taylor(Form,float(X0),int(Cantidad))

        self.Actualizar_tabla(y)
        mt.graficar_Taylor(Form,x,float(X0))
    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.CantidadPasos.delete(0,END)
        self.x0.delete(0,END)

class Metodo_Trapecio(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()

    def Crear_Label(self):

        
        label   = ttk.Label(self, text ="Metodo del Trapecio",         font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y=20)
        label   = ttk.Label(self, text ="Formula      :",  font =  self.Er.Letra3, width = 16 ).place(x = 20, y=106)
        labelIA = ttk.Label(self, text ="Intervalo a  :",font =  self.Er.Letra3, width = 15 ).place(x = 20, y=146)
        labelIB = ttk.Label(self, text ="Intervalo b  :",font =  self.Er.Letra3, width = 15 ).place(x = 220, y=146)
        label   = ttk.Label(self, text ="Cantidad de pasos :",      font =  self.Er.Letra3, width = 20 ).place(x=20, y=186)
        label  = ttk.Label(self, text ="Tabla de contenido",     font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=265)

    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 230)
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 230)
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 70,font= self.Er.Letra3)
        self.entryFormula.place(x = 120, y = 105)
        self.entryCantPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.entryCantPasos.place(x = 165, y = 185)
        
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterA.place(x = 120, y = 146)
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB.place(x = 320, y = 146)

    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.entryCantPasos.delete(0,END)
        pass

    def Calcular_M(self):
        Form = self.entryFormula.get()
        Ia = self.entryInterA.get()
        Ib = self.entryInterB.get()
        Pasos = self.entryCantPasos.get()

        error , x ,y = 0,0,0

        try:
            error,x,y  = mt.Metodo_Trapecio(Form,float(Ia),float(Ib),eval(Pasos))
            
            
            self.Actualizar_tabla(x,y)
            
            
        except:
            print("Error de ingresar datos")
            pass
        mt.Graficar_Trapecios(Form,float(Ia),float(Ib),eval(Pasos),error)
        


    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=11, columns=('x','y'))
        self.table.place(x=8, y=300)

        
        self.table.heading('#0',text="Pasos",anchor = CENTER)
        self.table.column('#0',width=200, anchor=CENTER)
        self.table.heading('x',text="Xi",anchor = CENTER)
        self.table.column('x',width=200, anchor=CENTER)
        self.table.heading('y',text="Fi",anchor = CENTER)
        self.table.column('y',width=200, anchor=CENTER)
       
        
    
    def Actualizar_tabla(self,x,y):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        

        try:
            for fila in range(len(x)):
                
                self.table.insert("",'end',text= fila, values=(round(x[fila],4),round(y[fila],4)))
            pass
        except:
            print("error")
            pass
    
class Metodo_Simpson(ttk.Frame):
    
    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()

    def Crear_Label(self):

        
        label   = ttk.Label(self, text ="Metodo  Simpson",         font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y=20)
        label   = ttk.Label(self, text ="Formula      :",  font =  self.Er.Letra3, width = 16 ).place(x = 20, y=106)
        labelIA = ttk.Label(self, text ="Intervalo a  :",font =  self.Er.Letra3, width = 15 ).place(x = 20, y=146)
        labelIB = ttk.Label(self, text ="Intervalo b  :",font =  self.Er.Letra3, width = 15 ).place(x = 220, y=146)
        label   = ttk.Label(self, text ="Cantidad de muestras :",      font =  self.Er.Letra3, width = 22 ).place(x=20, y=186)
        label  = ttk.Label(self, text ="Tabla de contenido",     font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=265)

    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 230)
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 230)
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 70,font= self.Er.Letra3)
        self.entryFormula.place(x = 120, y = 105)
        self.entryCantPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.entryCantPasos.place(x = 185, y = 185)
        
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterA.place(x = 120, y = 146)
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB.place(x = 320, y = 146)

    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.entryCantPasos.delete(0,END)
        pass

    def Calcular_M(self):
        Form = self.entryFormula.get()
        Ia = self.entryInterA.get()
        Ib = self.entryInterB.get()
        Pasos = self.entryCantPasos.get()

        error , x ,y = 0,0,0

        try:
            error,x,y = mt.simpson_simplex(Form,float(Ia),float(Ib),eval(Pasos))
            
            
            self.Actualizar_tabla(x,y)
            
            
        except:
            print("Error de ingresar datos")
            pass
        mt.Graficar_Simpson(Form,float(Ia),float(Ib),eval(Pasos),error)
        


    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=11, columns=('x','y'))
        self.table.place(x=8, y=300)

        
        self.table.heading('#0',text="Pasos",anchor = CENTER)
        self.table.column('#0',width=200, anchor=CENTER)
        self.table.heading('x',text="Xi",anchor = CENTER)
        self.table.column('x',width=200, anchor=CENTER)
        self.table.heading('y',text="Fi",anchor = CENTER)
        self.table.column('y',width=200, anchor=CENTER)
       
        
    
    def Actualizar_tabla(self,x,y):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 

        try:
            for fila in range(len(x)):
                
                self.table.insert("",'end',text= fila, values=(round(x[fila],4),round(y[fila],4)))
            pass
        except:
            print("error")
            pass
 
class Metodo_Runge_Kutta(ttk.Frame):

    def __init__(self,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Crear_Label()
        self.Crear_Botones()
        self.Crear_Entry()
        self.Crear_tabla()
        self.Crear_Combobox()
    

    def Crear_Label(self):
        label   = ttk.Label(self, text ="Metodo de Runge-Kutta",    font =  self.Er.Letra,  width = 42 , anchor = CENTER).place(x = 0, y = 20)
        label   = ttk.Label(self, text ="F(x)'  :",           font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 106)
        labelIA = ttk.Label(self, text ="x(0)   :",           font =  self.Er.Letra3, width = 20 ).place(x = 20, y= 146)
        labelIB = ttk.Label(self, text ="x final               :", font =  self.Er.Letra3, width = 20 ).place(x = 180, y = 146)
        label   = ttk.Label(self, text ="y(0)  :",            font =  self.Er.Letra3, width = 20 ).place(x = 20, y = 186)
        label   = ttk.Label(self, text ="Cant. de Pasos :",   font =  self.Er.Letra3, width = 20 ).place(x = 180, y = 186)
        label   = ttk.Label(self, text ="Orden          :",   font =  self.Er.Letra3, width = 20 ).place(x = 390, y = 186)

        label  = ttk.Label(self, text ="Tabla de contenido",    font =  self.Er.Letra2, width = 60,  anchor = CENTER).place(x=8, y=285)#20
    
    def Crear_Entry(self):
        self.entryFormula   = Entry(self,text="",fg="black",bg="white",width = 77,font= self.Er.Letra3)
        self.entryFormula.place(x = 70, y = 105)

        self.x0 = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.x0.place(x = 70, y = 185)
        self.CantidadPasos = Entry(self,text="",fg="black",bg="white",width = 10 ,font= self.Er.Letra3 ,justify='center')
        self.CantidadPasos.place(x = 295, y = 185)
        
        self.entryInterA= Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterA.place(x = 70, y = 146)
        self.entryInterB = Entry(self,text="",fg="black",bg="white",width=10,font= self.Er.Letra3,justify='center')
        self.entryInterB.place(x = 295, y = 146)


    def Crear_Combobox(self):
        self.combo = ttk.Combobox(self,width = 10,height = 100,state="readonly" ,justify= "center", values = ["2","3","4"])
        self.combo.set("2")
        self.combo.place(x = 455, y =186)

        
        

    def Crear_Botones(self):
        #Botoenes
        self.Calcular = ttk.Button(self, text="Calcular",command=self.Calcular_M, width = 15)
        self.Calcular.place(x =160, y = 240) #10
        self.Borrar = ttk.Button(self, text="Limpiar",command=self.Limpiar, width = 15)
        self.Borrar.place(x = 340, y = 240)
    
    def Crear_tabla(self):
        self.table = ttk.Treeview(self,height=10, columns=('y'))
        self.table.place(x=8, y=320)

        
        self.table.heading('#0',text="x",anchor = CENTER)
        self.table.column('#0',width=300, anchor=CENTER)
        self.table.heading('y',text="F(x)",anchor = CENTER)
        self.table.column('y',width=300, anchor=CENTER)
    
    def Actualizar_tabla(self,x):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        
        try:
            
            
            for fila in range(len(x)):
                self.table.insert("",'end',text= round(x[fila][0],10), values=(round(x[fila][1],10)))
                pass
        except:
            print("error")
            pass

    def Calcular_M(self):
        Form = self.entryFormula.get()
        Ia = self.entryInterA.get()
        Ib = self.entryInterB.get()
        Cantidad = self.CantidadPasos.get()
        X0 = self.x0.get()
        orden =  int(self.combo.get())
        x = 0

        print([float(Ia),float(Ib)],[float(X0)],Form,int(Cantidad))
        x = mt.Metodo_runge_kutta(orden,Form,float(Ia),float(Ib),int(Cantidad),float(X0))

        self.Actualizar_tabla(x)

        aux_x, aux_y = [],[]
        for i in range(len(x[0])):
            aux_x.append(x[i][0])
            aux_y.append(x[i][1])
    
    def Limpiar(self):
        registros=self.table.get_children()

        for elemento in registros:
            self.table.delete(elemento) 
        
        self.entryFormula.delete(0,END)
        self.entryInterA.delete(0, END)
        self.entryInterB.delete(0, END)
        self.CantidadPasos.delete(0,END)
        self.x0.delete(0,END)

class Acerca_de(ttk.Frame):
    
    def __init__(self,Padre,Ere, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.Er = Ere
        self.Pd = Padre

        self.Crear_Label()
        self.Stiker_Pollo()
        self.Crear_Botones()
    def Crear_Label(self):
        label = ttk.Label(self, text ="Acerca de este proyecto",font =  self.Er.Letra,  width = 42).place(x = 10, y=30)
        texto ="""

            Proyecto creado por Elias Flores Pérez centrado en la materia de métodos numéricos 
            de 4to semestre de la Universidad estatal de Milagro el Código este hecho en Python 
            y una pequeña base de datos en SQLite para guardar los temas.

            Un  agradecimiento a  Melanie,  Joseph y  a  al  Ingeniero  JAVIER CASTILLO HEREDIA
            El  Código  estará  en  mi  GitHub por si  quieren  revisarlo , modificarlo  o  mejorarlo
            también  esta una explicación en  YouTube  del funcionamiento  de esta  aplicación.

        """
       


        label = ttk.Label(self, text =texto,font =  self.Er.Letra3,  width = 90).place(x = -40, y=70)
        
    def Crear_Botones(self):
        self.GitHub = ttk.Button(self, text="Github", width = 15)
        self.GitHub.place(x =160, y = 250)
        self.Youtube = ttk.Button(self, text="Video", width = 15)
        self.Youtube.place(x = 340, y = 250)
        

    def Stiker_Pollo(self):
        global imagen_p
        pollito =  Image.open("Imagenes/Temp.png")
        pollito_re = pollito.resize((50, 50))
        self.pollite = ImageTk.PhotoImage(pollito_re)
        
        self.BotonPollo = Button(self, text = '1', image =self.pollite,background = self.Er.Color_Oscuro ,command = self.Piar,borderwidth = 0)
        imagen_p = self.BotonPollo
        self.BotonPollo.place(x=570,y = 510)
    
    def Piar(self):
        print("pio")
        
        