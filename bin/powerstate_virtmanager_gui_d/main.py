#!/usr/bin/env python

#
# Filename:       main.py
# Version:        1.0.0
# Description:    
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import gi
import glade_python_gtk

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if __name__ == "__main__":
  main = glade_python_gtk()
  Gtk.main()