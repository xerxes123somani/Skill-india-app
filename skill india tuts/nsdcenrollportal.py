from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty
import webbrowser
class NsdcEnrollPortal(MDScreen):
    def open_portal(self):
       webbrowser.open("https://partnerships.nsdcindia.org/login") 