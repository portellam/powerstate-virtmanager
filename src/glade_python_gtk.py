#!/usr/bin/env python

#
# Filename:       glade_python_gtk.py
# Version:        1.0.0
# Description:    
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

# TODO: determine if this is still necessary?

class glade_python_gtk(Gtk.Window):
  column_list = [ "Name" "Status" ]

  def __init__(self):
    builder = Gtk.Builder()
    builder.add_from_file(glade_file_name)
    builder.connect_signals(self)

    Domain_List.get_lists()

    self.ListStore1 = builder.get_object('ListStore1')
    self.TreeView1 = builder.get_object('TreeView1')

    for i in range(column_list):
      column = Gtk.TreeViewColumn(column_list[i], Gtk.CellRendererText(), text=i)
      column.set_clickable(True)
      column.set_resizable(True)
      self.TreeView1.append_column(column)

    for domain_and_status in Domain_List.domain_dict:
      self.ListStore1.append(list(domain_and_status))

    window = builder.get_object('ViewPort1')
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()

  def on_window1_destroy(self, object, data=None):
    print ("Quit with exit.")
    Gtk.main_quit()