#!/usr/bin/env python
#importar setup de distutils
from distutils.core import setup  
#Crear la variable data_files que contiene las rutas de donde se van a colocar los archivos.
data_files = [('share/applications',['pyconfig-accessgnome-ui.desktop']),
    ('share/python-config-accesskey-gnome',['COPYING','configGconf.py','pyconfig-accessgnome.glade','pyconfig-accessgnome-ui.py','README','TODO'])]


#se define el nombre del programa, la versión, una descripción corta, el autor y su correo, 
#el url del proyecto, la licencia, los scripts principales del programa, los archivos de datos adicionales,
#La plataforma soportadas,los módulos que se requieren para el funcionamiento del programa.
#Y el módulo que se desarrollo y necesita el programa principal.


setup(name='ardu-mrua',
      version='0.1',
      description='Allow config keyboard access application with gconf',
      author='Jotam Jr. Trejo', 
      author_email='jotamjr@gmail.com',
      url = 'https://github.com/jotamjr/ardu-mrua',
      license = "GPL v3",
      scripts = ['pyconfig-accessgnome-ui.py', 'configGconf.py'],
      data_files =data_files,
      platforms=['i386'],
      requires = ['gtk','gconf','pygtk','gtk.glade'],
      py_modules = ['configGconf']
      )
