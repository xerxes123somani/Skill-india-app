
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from nsdc import Nsdc
Builder.load_file("nsdc.kv")

class Schemes(MDScreen):
    scheme_screen_manager=ObjectProperty()
    def NSDC(self):
        print("NSDC pressed")
        return "NSDC"
    
    def PMKY(self):
        print("PMKY pressed")
        return "PMKVY"
    

