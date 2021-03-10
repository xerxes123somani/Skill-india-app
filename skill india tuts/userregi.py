from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from firebase_connect import create_user
class Userregi(MDScreen):
    screen_manager = ObjectProperty()
    main_toolbar = ObjectProperty()
    def Register_user(self,user_name,name,email,password,cnfrm_password):
        if(user_name.text==''):user_name.text="Enter the feild"
        if(name.text==''):name.text="Enter your full name first"
        if(email.text==''):email.text="Enter email"
        if(password.text=="" or cnfrm_password==""):
            password.text="Enter password"
            cnfrm_password.text="Enter password"
        if(password.text!=cnfrm_password):password.text=="password does not match"
        else:
            if(create_user(email.text, password.text)):
                return "Home"
        
