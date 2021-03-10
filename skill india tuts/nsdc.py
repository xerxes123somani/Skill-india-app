from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty
from nsdcenrollportal import NsdcEnrollPortal
from kivy.lang.builder import Builder
import webbrowser
Builder.load_file("nsdcenrollportal.kv")

class Nsdc(MDScreen):
    scheme_screen_manager=ObjectProperty()
    def Funding(self):
        print("funding pressed")
        webbrowser.open("https://nsdcindia.org/funding")
        #return "Funding_NSDC"
    
    def Find_NSDC_training_center(self):
        print("NSDC training center pressed")
        webbrowser.open("https://nsdcindia.org/find-nsdc-training-centre")
        #return "NSDC_Train"
    
    def Industry_partnership(self):
        print("Industry Partnership pressed")
        webbrowser.open("https://nsdcindia.org/industry-partnership-csr")
        #return "Industry_Partnership_NSDC"
    
    def NSDC_Enroll_Portal(self):
        print("NSDC Enroll pressed")
        return "NSDC_Enroll_Portal"

class Pmkvy(MDScreen):
    scheme_screen_manager=ObjectProperty()
    def visit_pmkvy(self):
        print('Pmkvy visiting')
        webbrowser.open('http://pmkvyofficial.org/')
    
