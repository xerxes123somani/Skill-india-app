from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
class DrawerScreen(MDScreen):
    def on_start(self):
        icons_item={'Feedback':1,'Scheme':2}

class ContentDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior,MDList):
    def Profile(self):
        print("Profil pressed")
         DrawerScreen().ids.Profile_screen
        
    def Schemes(self):
        print("Schemes pressed")
        
    def Applied_jobs(self):
        print("Schemes pressed")
        
    def Feedback(self):
        print("Schemes pressed")
        
    def Settings(self):
        print("Schemes pressed")

class Drawer(MDApp):
    def build(self):
        return DrawerScreen()
    
Drawer().run()