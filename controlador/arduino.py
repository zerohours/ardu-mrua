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

# Creamos la clase de la ventana principal del programa
class MainWin:
    
    def __init__(self):
        # Le decimos a nuestro programa el nombre del archivo glade
        self.widgets = gtk.glade.XML("interface.glade")
        
        # Creamos un pequeño diccionario que contiene las señales definidas en
        # glade y su respectivo método (o llamada)
        signals = { #"on_entry1_activate" : self.on_button1_clicked,
                    #"on_button1_clicked" : self.on_button1_clicked,
                    "create_test" : self.create_lib,
                    "on_exit_clicked" : gtk.main_quit, # al presionar el boton salir, sale de la aplicacion
                    "gtk_main_quit" : gtk.main_quit }  # 
        
        # Luego se auto-conectan las señales.
        self.widgets.signal_autoconnect(signals)
        # Nota: Otra forma de hacerlo es No crear el diccionario signals y
        # solo usar "self.widgets.signal_autoconnect(self)" -->Ojo con el self
        
        # Ahora obtenemos del archivo glade los widgets que vamos a utilizar
        self.label1 = self.widgets.get_widget("label1")

        #Definición del widget que manejará la gráfica
        self.figura = Figure(figsize=(10, 8), dpi=100)
        self.ax = self.figura.add_subplot(111)
        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")
        self.ax.set_title('Grafica')
        self.ax.grid(True)
        self.canvas = FigureCanvasGTK(self.figura)
        self.canvas.show()

        #Agregar la gráfica a la caja vertical
        self.vbox2 = self.widgets.get_object("vbox2")
        self.vbox2.pack_start(self.canvas, True, True)
 
        
    # Se definen los métodos, en este caso señales como "destroy" ya fueron
    # definidas en el .glade, así solo se necesita definir "on_button1_clicked"
    def on_button1_clicked(self, widget):
        texto = self.entry1.get_text()
        self.label1.set_text("Hola %s" % texto)
    def create_lib(self, widget):
        self.label1.set_text("Hola")

# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()
