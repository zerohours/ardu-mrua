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

import numpy

from matplotlib.figure import Figure
from matplotlib.axes import Subplot
from matplotlib.backends.backend_gtk import FigureCanvasGTK
from matplotlib.backends.backend_gtk import NavigationToolbar

from numpy import arange
from numpy import sin
from numpy import pi

import time


#Creamos la clase de la ventana principal del programa
class MainWin:

    def __init__(self):
        # Le decimos a nuestro programa el nombre del archivo glade
        self.widgets = gtk.glade.XML("interface/interface.glade")

        # Creamos un pequeño diccionario que contiene las señales definidas en
        # glade y su respectivo método (o llamada)
        signals = {"on_buttonIniciar_clicked": self.on_buttonIniciar_clicked,
            "on_buttonGraphicVelocidad_clicked": self.graficarVelocidad,
            "on_buttonGraphicAceleracion_clicked": self.graficarAceleracion,
            "on_buttonGraphicTiempo_clicked": self.graficarTiempo,
            "on_about_dialog_clicked": self.on_about_dialog_clicked,
            "on_exit_clicked": gtk.main_quit,
            "gtk_main_quit": gtk.main_quit}

        # Luego se auto-conectan las señales.
        self.widgets.signal_autoconnect(signals)
        # Nota: Otra forma de hacerlo es No crear el diccionario signals y
        # solo usar "self.widgets.signal_autoconnect(self)" -->Ojo con el self

        # Ahora obtenemos del archivo glade los widgets que vamos a utilizar
        #ventana principal
        self.windowMain = self.widgets.get_widget("windowMain")
        #label de tiempo
        self.labelTiempo = self.widgets.get_widget("labelTime")
        #boton iniciar
        self.buttonIniciar = self.widgets.get_widget("buttonIniciar")
        #boton iniciar
        self.buttonVelocidad = self.widgets.get_widget( \
            "buttonGraphicVelocidad")
        #boton iniciar
        self.buttonSalir = self.widgets.get_widget("buttonSalir")
        #dialogo acerca de
        self.aboutDialog = self.widgets.get_widget("aboutDialog")
        #espacio donde ira la grafica
        self.graphview = self.widgets.get_widget("matplot")
        self.viewData = self.widgets.get_widget("viewData")
        #valor del angulo introducido
        self.entryAngulo = self.widgets.get_widget("entryAngulo")
        #valor del angulo introducido
        self.entryDistancia = self.widgets.get_widget("entryDistancia")

        self.lanzamientotext = "Lanzamiento"
        self.tiempotext = "Tiempo"
        self.distanciatext = "Distancia"
        self.velocidadtext = "Velócidad"
        self.aceleraciontext = "Aceleración"
        self.angulotext = "Ángulo"

        #Agrega todas las columnas de la lista a la vista de arbol
        self.AgregarListaAColumna(self.lanzamientotext, 0)
        self.AgregarListaAColumna(self.distanciatext, 1)
        self.AgregarListaAColumna(self.tiempotext, 2)
        self.AgregarListaAColumna(self.velocidadtext, 3)
        self.AgregarListaAColumna(self.aceleraciontext, 4)
        self.AgregarListaAColumna(self.angulotext, 5)

        #Crea la lista de modelo para usar con la vista de arbol
        self.wineList = gtk.ListStore(str, str, str, str, str, str)

        #Agregando el modelo a la vista de arbol
        self.viewData.set_model(self.wineList)

        #Llamamos la grafica inicial
        self.canvas = self.graficaInicial()

        #Mostramos la grafica inicial
        self.graphview.pack_start(self.canvas, True, True)

    # Se definen los métodos, en este caso señales como "destroy" ya fueron
    # definidas en el .glade, así solo se necesita definir "on_button1_clicked"
    def on_about_dialog_clicked(self, widget):
        self.aboutDialog.run()
        self.aboutDialog.hide_on_delete()

    def on_buttonIniciar_clicked(self, widget):
        self.wineList.clear()
        self.wineList.append(["0", "0", "0.000", "0.00", "000", "25"])
        self.wineList.append(["1", "7", "0.216", "32.4", "150", "25"])
        self.wineList.append(["2", "17", "0.354", "48.0", "136", "25"])
        self.wineList.append(["3", "23", "0.440", "52.3", "119", "25"])
        self.wineList.append(["4", "34", "0.470", "72.3", "154", "25"])
        self.wineList.append(["5", "47", "0.615", "76.4", "124", "25"])

        """self.wineList.append(["0",
            "Tiempo",
            self.entryDistancia.get_text(),
            "Velocidad",
            "Aceleracion",
            self.entryAngulo.get_text()])"""

    #Esta función añade una columna a la vista de lista.
    #En primer lugar, crear el gtk.TreeViewColumn a continuación,
    #establecer algunas propiedades necesarias
    def AgregarListaAColumna(self, title, columnId):
        column = gtk.TreeViewColumn(title, \
            gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.viewData.append_column(column)

    def graficaInicial(self):

        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6, 4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('t')
        self.axis.set_ylabel('v')
        self.axis.set_title('Graphic Init')
        self.axis.grid(True)

        #mostramos la funcion usada en la grafica
        self.axis.text(0, -1, r'$sin(2*\pi*t)$', fontsize=18)

        #Creamos un array
        #que va desde 0 hasta 3 en 0.01
        t = arange(0.0, 3.0, 0.01)

        #Graficamos una funcion con seno
        s = sin(2 * pi * t)

        #Agregamos la funcion a la grafica
        self.axis.plot(t, s)

        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)

        #Mostramos la grafica
        self.canvas.show()

        return self.canvas

    def graficarVelocidad(self, widget):

        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6, 4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('Tiempo (s)')
        self.axis.set_ylabel('Velocidad (m/s)')
        self.axis.set_title('Grafico Velocidad vrs. Tiempo')
        self.axis.grid(True)

        #Creamos un array
        #que va desde 0 hasta 3 en 0.01
        t = self.getTiempo()

        #Graficamos una funcion con seno
        v = self.getVelocidad()

        #Agregamos la funcion a la grafica
        self.axis.plot(t, v)

        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)

        #Mostramos la grafica
        self.canvas.show()

        #removemos la grafica actual
        self.removerGrafica()

        #Mostramos la grafica
        self.graphview.pack_start(self.canvas, True, True)

    def graficarAceleracion(self, widget):

        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6, 4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('Tiempo (s)')
        self.axis.set_ylabel('Aceleración (m/s²)')
        self.axis.set_title('Grafico Aceleración vrs. Tiempo')
        self.axis.grid(True)

        #Creamos un array
        #que va desde 0 hasta 3 en 0.01
        t = self.getTiempo()

        #Graficamos una funcion con seno
        a = self.getAceleracion()

        #Agregamos la funcion a la grafica
        self.axis.plot(t, a)

        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)

        #Mostramos la grafica
        self.canvas.show()

        #removemos la grafica actual
        self.removerGrafica()

        #Mostramos la grafica
        self.graphview.pack_start(self.canvas, True, True)

    def graficarTiempo(self, widget):

        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6, 4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('Tiempo (s)')
        self.axis.set_ylabel('Distancia (cm)')
        self.axis.set_title('Grafico Distancia vrs. Tiempo')
        self.axis.grid(True)

        #Creamos un array
        #que va desde 0 hasta 3 en 0.01
        t = self.getTiempo()

        #Graficamos una funcion con seno
        d = self.getDistancia()

        #Agregamos la funcion a la grafica
        self.axis.plot(t, d)

        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)

        #Mostramos la grafica
        self.canvas.show()

        #removemos la grafica actual
        self.removerGrafica()

        #Mostramos la grafica
        self.graphview.pack_start(self.canvas, True, True)

    def removerGrafica(self):
        self.borrar = self.graphview.get_children()
        for x in range(len(self.borrar)):
            self.graphview.remove(self.borrar[x])
            
    def getDistancia(self):
        temp = []
        for row in self.wineList:
            temp.insert(len(temp), row[1])
        return temp

    def getTiempo(self):
        temp = []
        for row in self.wineList:
            temp.insert(len(temp), row[2])
        return temp

    def getVelocidad(self):
        temp = []
        for row in self.wineList:
            temp.insert(len(temp), row[3])
        return temp

    def getAceleracion(self):
        temp = []
        for row in self.wineList:
            temp.insert(len(temp), row[4])
        return temp


# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()
