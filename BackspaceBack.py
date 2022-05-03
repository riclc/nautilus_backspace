#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# by Ricardo Lenz, 2016-jun
# riclc@hotmail.com
#

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

def ok():
    app = Gtk.Application.get_default()
    app.set_accels_for_action( "win.back", ["BackSpace"] )
    #print app.get_actions_for_accel("BackSpace")
    #print app.get_actions_for_accel("<alt>Up")


class BackspaceBack(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass
    
    def get_widget(self, uri, window):
        ok()
        return None

