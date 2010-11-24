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
        signals = { "on_buttonIniciar_clicked" : self.on_buttonIniciar_clicked,
                    "on_about_dialog_clicked" : self.on_about_dialog_clicked,
                    "on_exit_clicked" : gtk.main_quit, # al presionar el boton salir, sale de la aplicacion
                    "gtk_main_quit" : gtk.main_quit }  # 
        
        # Luego se auto-conectan las señales.
        self.widgets.signal_autoconnect(signals)
        # Nota: Otra forma de hacerlo es No crear el diccionario signals y
        # solo usar "self.widgets.signal_autoconnect(self)" -->Ojo con el self
        
        # Ahora obtenemos del archivo glade los widgets que vamos a utilizar        
        self.labelTiempo = self.widgets.get_widget("labelTiempo") #label de tiempo
        self.buttonIniciar = self.widgets.get_widget("buttonIniciar") #boton iniciar
        self.aboutDialog = self.widgets.get_widget("aboutDialog") #dialogo acerca de

        #Definición del widget que manejará la gráfica
        self.figure = Figure(figsize=(6,4), dpi=60)
        self.axis = self.figure.add_subplot(111)

        self.axis.set_xlabel('X')
        self.axis.set_ylabel('Y')
        self.axis.set_title('Graph')
        self.axis.grid(True)
        
        #Agregar la gráfica a la caja vertical
        self.canvas = FigureCanvasGTK(self.figure)
        self.canvas.show()
        self.graphview = self.widgets.get_widget("matplot")
        self.graphview.pack_start(self.canvas, True, True)
 
    # Se definen los métodos, en este caso señales como "destroy" ya fueron
    # definidas en el .glade, así solo se necesita definir "on_button1_clicked"
    def on_about_dialog_clicked(self, widget):
        #self.labelTiempo.set_text("Hola !")
        self.aboutDialog.show()
        
    def on_buttonIniciar_clicked(self, widget):
        self.labelTiempo.set_text("Hola !")    
	
# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()
