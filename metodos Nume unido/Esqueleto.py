"""
    Este archivo se encarga de crear por asi decirlo la base de las demas interfacez
    Aqui creo los estilos y los incorporo a toda la aplicacion este archivo tiene un
    notebook con cada **Frame** que estos sera una clase que contendra cada metodo
    y lo datos que pidan.
"""


#Librerias
from tkinter import *
from tkinter import ttk
from tkinter.constants import END, TRUE, TOP
import tkinter.font as tkFont
from PIL import Image, ImageTk,ImageColor

import Configuracion as Conf
import BDColores as Bd

# Clase  importante  para no andar creando a cada rato los estilos si no que  desde aqui
# Se pedira  que  tipo de letra tendra o que  colores usara aqui se  puede  cambiar  los
# Tambien se inicializa los tipo de fuentes que son 3  una para titulo, botones y  label
# Colores de dia y noche si no gusta tanto los colores que predifini.
class EstilosRainbow():
    #Colores 
    Primario =  "#2B4352" 
    Secundario  = "#00876E"
    Terciario = "#00B488"

    Fondo = "#EBEBEB"
    FondoLetra = "#000000"
    letra = 0

    #Colores del boton sol/luna o modo claro y oscuro
    
    Color_claro = "#EBEBEB"
    Color_Oscuro = "#262627"

    #Color de letra: 
    Letra_p = ""
    Letra_s = ""
    Letra_t = ""

    def __init__(self):
        #Tipo de fuentes
        self.Letra = tkFont.Font(family='Century Gothic', size=20,weight="bold")
        self.Letra2 = tkFont.Font(family='Century Gothic', size=13,weight="bold")
        self.Letra3 = tkFont.Font(family='Century Gothic', size=10,weight="bold")
        #Recojo la ultima configuracion del usuario
        valor =  Bd.Devolver_Color()
        
        self.Fondo = valor[0][1]
        try:
            
            frase =  valor[0][0].split("-")
            self.Primario   = frase[0]
            self.Secundario = frase[1]
            self.Terciario  = frase[2]
            
             
        except:
            pass
        #self.CalcularLuminosidad(self.Color_Oscuro)

    #Funcion para saber si un color es claro o oscuro para cambiar el color de la letra
    #y no incomodidar al usuario al usar la app.
    def CalcularLuminosidad(self,color):

        #Calculamos la luminosidad de un color sumandolos y dividiendolo para tres
        try:
            Color_aux = int(color[1:3],16) + int(color[3:5],16) + int(color[5:7],16) 
            Color_aux /= 3
            
        except:
            
            Color_aux = 0

        #Si este es > 80  es claro si es menor  es oscuro
        
        if Color_aux > 80:
            #Retornamos negro
            return "#000000"
        else:
            #Retornamos blanco 
            return "#FFFFFF"

#Clase principal
class App(ttk.Frame):

    

    def __init__(self,master):
        super().__init__(master) # ?

        self.ventana = master
        self.Er = EstilosRainbow()

        self.Cambiar_Ventana()
        self.Crear_NoteBook()
        
        self.Logo_Unemi()
        self.Crear_Estilos()
        
        
        

    def Cambiar_Ventana(self):
        self.ventana.title("Metodos Numericos")
        self.ventana.geometry("800x600")
        self.ventana.resizable(width=False, height=False)
        self.ventana.config(background=self.Er.Primario)

    #Esta funcion es la que se encarga de cambiar todo los estilos que se
    #crearon especificamente en los colores de la app y fondos de las imagenes
    #Esto ayuda a no cambiar todo si no que se cambia por grupos de etiquetas
    #de tkinter la documentacion de ttk que es una mejora a tkinter 
    #Pueden leer la documentacion aqui : https://www.tcl.tk/man/tcl/TclCmd/contents.html

    def Crear_Estilos(self):
        Primario = self.Er.Primario
        Secundario = self.Er.Secundario
        Terciario =  self.Er.Terciario

        self.s = ttk.Style()
        self.ventana.config(background=Primario)
        self.canvas.config(background=self.Er.Fondo)


        if self.Er.Fondo == self.Er.Color_Oscuro:
            self.frame.place(x = 2000,y = 33)
            self.frameNegro.place(x = 20,y = 33)
            
        else:
            self.frame.place(x = 20,y = 33)
            self.frameNegro.place(x = 2000,y = 33)
            

        #Los estilos son diccionarios y se pueden cambiar sus atributos
        estilo = {         
                "TNotebook": {
                    "configure": {
                        "tabmargins": [0, 60, 2, 0],
                        "tabposition":'wn',
                        "background": self.Er.Fondo,
                        "bordercolor" : self.Er.Fondo,
                        
                        
                        
                    } 
                }, 

                "TNotebook.Tab": {
                    "configure": {
                        "padding": [5, 16],
                        "background": Terciario,
                        "width" :22,
                        "foreground":self.Er.CalcularLuminosidad(Terciario)
                        
                        
                    },
                    "map": {
                        "background": [("selected", Primario),("active", Secundario)],
                        "foreground": [("selected", self.Er.CalcularLuminosidad(Primario) ),("active", self.Er.CalcularLuminosidad(Secundario))]
                    }
                },
                "TButton": {
                    "configure": {
                        "relief":"raised",
                        "background":Terciario,
                        "font" : ('calibri', 11, 'bold'),
                        "anchor" : "center",
                        "foreground":self.Er.CalcularLuminosidad(Terciario),
                        "focuscolor":Terciario
                        
                    },
                    "map": {
                        "background": [("active", Secundario)],
                        "foreground": [("selected", self.Er.CalcularLuminosidad(Terciario)),("active", self.Er.CalcularLuminosidad(Secundario))],
                        "focuscolor": [("selected", "white"),("active", Secundario)],

                    }
                    
                    
                },
                "Tab":{
                    "configure": {
                        "focuscolor":Primario
                    }
                    
                        

                },
                "Treeview.Heading":{
                    "configure": {
                        "background":Terciario,
                        "font" : ('calibri', 11, 'bold'),
                        "foreground": self.Er.CalcularLuminosidad(Terciario),
                        
                        
                    }
                },
                "Treeview":{
                    "configure": {
                        "background":self.Er.Fondo,
                        "foreground": self.Er.CalcularLuminosidad(self.Er.Fondo),
                        "fieldbackground ":self.Er.Fondo
                        
                        
                    }
                },
                "TFrame":{
                   "configure": {
                        "background":self.Er.Fondo,
                        
                        
                    } 
                },
                "TLabel":{
                   "configure": {
                        "background":self.Er.Fondo,
                        "foreground":self.Er.CalcularLuminosidad(self.Er.Fondo)
                        
                        
                    } 
                },

                "TRadiobutton":{
                   "configure": {
                        "background":self.Er.Fondo,
                        "foreground":self.Er.CalcularLuminosidad(self.Er.Fondo),
                        "indicatorcolor":self.Er.Fondo
                        
                        
                        
                    } 
                },

                "Blue.Horizontal.TScale":{
                   "configure": {
                        "background":"blue",
                        "troughcolor":self.Er.Fondo,

                        

                    } 
                },
                "Red.Horizontal.TScale":{
                   "configure": {
                        "background":"red",
                        "troughcolor":self.Er.Fondo,


                    } 
                },
                "Green.Horizontal.TScale":{
                   "configure": {
                        "background":"green",
                        "troughcolor":self.Er.Fondo,

                    } 
                },

                "TCombobox":{
                   "configure": {
                        "background":Terciario,
                        "state":"readonly",
                        "arrowcolor": self.Er.CalcularLuminosidad(Terciario) ,
                        "arrowsize":20,
                        "selectforeground":"black",
                        "selectbackground ":"white"
                    } 
                },
                    
            }
        
        #Si existe el estilo da error y lo modifica o actualiza.
        try:
            self.s.theme_create( "MyStyle", parent="alt", settings= estilo)
        except:
            #Actualiza el fondo que tiene
            
            self.s.theme_settings( "MyStyle", settings= estilo)
           
        self.s.theme_use("MyStyle")
        

    #para darle ese estilo de poder elegir el metodo
    def Crear_NoteBook(self):

        self.notebook = ttk.Notebook(self.ventana,height = 555,width = 620)
        self.notebook.place(x = 17,y = 23)
        #self.notebook.grid(row = 5, column = 10)
        
        
        pestania1 = Conf.Metodo_Grafico(self.Er,self.notebook)
        pestania2 = Conf.Metodo_biseccion(self.Er,self.notebook)
        pestania3 = Conf.Metodo_Newton(self.Er,self.notebook)
        pestania4 = Conf.Metodo_Trapecio(self.Er,self.notebook)
        pestania5 = Conf.Metodo_Simpson(self.Er,self.notebook)
        pestania6 = Conf.Metodo_Euler(self.Er,self.notebook)
        pestania7 = Conf.Metodo_Taylor(self.Er,self.notebook)
        pestania8 = Conf.Metodo_Runge_Kutta(self.Er,self.notebook)
        pestania9 = Conf.Configuracion_Color(self,self.Er,self.notebook)
        pestania10 = Conf.Acerca_de(self,self.Er,self.notebook)

        self.notebook.add(pestania1,text = "      Metodo Grafico")
        self.notebook.add(pestania2,text = "      Metodo Biseccion")
        self.notebook.add(pestania3,text = "      Newton-Raphson")
        self.notebook.add(pestania4,text = "      Metodo del Trapecio")
        self.notebook.add(pestania5,text = "     Metodo de Simpson")
        self.notebook.add(pestania6,text = "     Metodo de Euler")
        self.notebook.add(pestania7,text = "    Metodo de Taylor")
        self.notebook.add(pestania8,text = "Metodo de Runge Kutta")
        self.notebook.add(pestania9,text = "         Configuracion     ")
        self.notebook.add(pestania10,text = "          Acerca de        ")

     #Para mostrar el logo de mi universidad :v
    def Logo_Unemi(self):
        blacklogo =  Image.open("Imagenes/LogoUnemi.png")
        blacklogo_re = blacklogo.resize((130, 50))
        self.logo = ImageTk.PhotoImage(blacklogo_re)


        Whitelogo =  Image.open("Imagenes/LogoUnemiWhite.png")
        Whitelogo_re = Whitelogo.resize((130, 50))
        self.logo_white = ImageTk.PhotoImage(Whitelogo_re)

        self.frame = Frame(self.ventana)
        self.frame.place(x = 20,y = 33)

        #Primer Canvas
        self.canvas = Canvas(self.frame, width=140, height=43,bg =  self.Er.Color_claro, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        self.canvas.create_image(70, 20, image=self.logo)

        #Segundo Canvas
        self.frameNegro = Frame(self.ventana)
        self.frameNegro.place(x = 2000,y = 33)

        self.canvasNegro = Canvas(self.frameNegro, width=140, height=43,bg =  self.Er.Color_Oscuro, bd=0, highlightthickness=0, relief='ridge')
        self.canvasNegro.pack()
        self.canvasNegro.create_image(70, 20, image=self.logo_white)
        
#Bucle de la app
def inicio():
    root = Tk()
    aplicacion = App(root)
    root.mainloop()
    

if __name__ == "__main__":
    
    inicio()
    