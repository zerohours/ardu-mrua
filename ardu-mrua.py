 #! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk
pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade

# Importamos la libreria de matplot
# y seleccionamos matplotlib usando GTK
import matplotlib
matplotlib.use('GTK')

from matplotlib.figure import Figure
from matplotlib.axes import Subplot
from matplotlib.backends.backend_gtk import FigureCanvasGTK, NavigationToolbar

from numpy import arange
from numpy import sin
from numpy import pi

import time

# Creamos la clase de la ventana principal del programa
class MainWin:
    
    def __init__(self):
        # Le decimos a nuestro programa el nombre del archivo glade
        self.widgets = gtk.glade.XML("interface/interface.glade")
        
        # Creamos un pequeño diccionario que contiene las señales definidas en
        # glade y su respectivo método (o llamada)
        signals = { "on_buttonIniciar_clicked" : self.on_buttonIniciar_clicked,
                    "on_about_dialog_clicked" : self.on_about_dialog_clicked,
                    "on_exit_clicked" : gtk.main_quit, # al presionar el boton salir, sale de la aplicacion
                    "gtk_main_quit" : gtk.main_quit }  # 
        
        # Luego se auto-conectan las señales.
        self.widgets.signal_autoconnect(signals)
        # Nota: Otra forma de hacerlo es No crear el diccionario signals y
        # solo usar "self.widgets.signal_autoconnect(self)" -->Ojo con el self
        
        # Ahora obtenemos del archivo glade los widgets que vamos a utilizar        
        self.labelTiempo = self.widgets.get_widget("labelTime") #label de tiempo
        self.buttonIniciar = self.widgets.get_widget("buttonIniciar") #boton iniciar
        self.buttonSalir = self.widgets.get_widget("buttonSalir") #boton iniciar
        self.aboutDialog = self.widgets.get_widget("aboutDialog") #dialogo acerca de
        self.viewData = self.widgets.get_widget("viewData")
        
        self.lanzamientotext = "Lanzamiento"
        self.tiempotext = "Tiempo"
        self.distanciatext = "Distancia"
        self.velocidadtext = "Velócidad"
        self.aceleraciontext = "Aceleración"
        self.angulotext = "Ángulo"
        
        #Agrega todas las columnas de la lista a la vista de arbol
        self.AgregarListaAColumna(self.lanzamientotext, 0)
        self.AgregarListaAColumna(self.tiempotext, 1)
        self.AgregarListaAColumna(self.distanciatext, 2)
        self.AgregarListaAColumna(self.velocidadtext, 3)
        self.AgregarListaAColumna(self.aceleraciontext, 4)
        self.AgregarListaAColumna(self.angulotext, 5)
        
        #Crea la lista de modelo para usar con la vista de arbol
        self.wineList = gtk.ListStore(str, str, str, str, str, str)
        
        #Agregando el modelo a la vista de arbol
        self.viewData.set_model(self.wineList)
        
        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6,4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('X')
        self.axis.set_ylabel('Y')
        self.axis.set_title('Graph')
        self.axis.grid(True)
        
        #Creamos un array
        t = arange(0.0,3.0,0.01)
        #Graficamos una funcion con seno
        s = sin(2*pi*t)
        
        #Agregamos la funcion a la grafica
        self.axis.plot(t,s)
        
        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)
        self.canvas.show()
        self.graphview = self.widgets.get_widget("matplot")
        self.graphview.pack_start(self.canvas, True, True)

    # Se definen los métodos, en este caso señales como "destroy" ya fueron
    # definidas en el .glade, así solo se necesita definir "on_button1_clicked"
    def on_about_dialog_clicked(self, widget):
        self.aboutDialog.run()
        self.aboutDialog.hide_on_delete()

    def on_buttonIniciar_clicked(self, widget):
        for tmp in range(0, 6):
            min = tmp / 60
            sec = tmp % 60
            hour = 0
            if min > 60:
                #vamos por las horas
                hour = min / 60
                min = min % 60
            if hour == 0:
                #print str(min) + ":" + str(sec) + " s."
                printtiempo = str(min) + ":" + str(sec) + " s."
                self.labelTiempo.set_text( str(min) + ":" + str(sec) + " s." )
            else:
                #print str(hour) + ":" + str(min) + ":" + str(sec) + " s."
                printtiempo = str(hour) + ":" + str(min) + ":" + str(sec) + " s."
                self.labelTiempo.set_text( str(min) + ":" + str(sec) + " s." )
            time.sleep(1)
    
    #Esta función añade una columna a la vista de lista. 
    #En primer lugar, crear el gtk.TreeViewColumn a continuación, 
    #establecer algunas propiedades necesarias
    def AgregarListaAColumna(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.viewData.append_column(column)

# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()
