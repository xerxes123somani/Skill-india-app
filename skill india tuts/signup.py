from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty 
class Signup(MDScreen):    
    screen_manager=ObjectProperty()
    def on_back_press(self,change_screen_to_):
        change_screen_to_.current= "Home"
        
    def user_registerpage(self):
        return "register"
        
    
