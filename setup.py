#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ardu-mrua',
    version='0.1.dev',
    packages = find_packages(),
    author='Jotam Jr. Trejo', 
    author_email='jotamjr@gmail.com',
    url = 'https://github.com/jotamjr/ardu-mrua',
    license = "GPL v3",
    scripts = ['ardu-mrua.py'],
    install_requires = ['gtk','gconf','pygtk','gtk.glade', 'matplotlib', 'serial'],
)
