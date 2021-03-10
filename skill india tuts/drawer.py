from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineListItem
from kivymd.uix.tab import MDTabsBase
import firebase_connect
from signup import Signup
from userprofile import Profile
from schemes import Schemes
from feedback import Feedback
from usersettings import UserSettings
from appliedjobs import AppliedJobs
from jobpost import Jobpost
from userregi import Userregi
Builder.load_file('signup.kv')
Builder.load_file('jobpost.kv')
Builder.load_file('profile.kv')
Builder.load_file('schemes.kv')
Builder.load_file('feedback.kv')
Builder.load_file('usersettings.kv')
Builder.load_file('appliedjobs.kv')
Builder.load_file('userregi.kv')
class Tab(FloatLayout,MDTabsBase):
    pass



class DrawerScreen(MDScreen):
    screen_manager=ObjectProperty()
    screen_list_=[]
    
            
    def account(self,manager):
        manager.current='Signup'
        self.screen_list_.append('Signup')
        print(self.screen_list_)
    def on_back_press(self):
        return self.screen_list.pop()

        

class ContentDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    main_toolbar = ObjectProperty()
    


class DrawerList(ThemableBehavior,MDList):

    def Profile(self):
        print("Profil pressed")
        return "Profile"
        
    def Schemes(self):
        print("Schemes pressed")
        return "Schemes"
    
    def Applied_jobs(self):
        print("Applied_jobs pressed")
        return "AppliedJobs"
    
    def Feedback(self):
        print("Feedback pressed")
        return "Feedback"
    
    def Settings(self):
        print("Settings pressed")
        return "Settings"

        

class Drawer(MDApp):
    
    def build(self):
        return DrawerScreen()
    
    def on_start(self):
        print(self.root.ids)
        for sch in ['Skill India', 'PMKVY','Objective','Courses','Schemes']:
            self.root.ids.Tabs.add_widget(Tab(text=f"{sch}"))
            
    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_image,instance_tab_label):
        print(instance_tabs,instance_tab,instance_tab_image,instance_tab_label)
        if instance_tab_label=='PMKVY':
            PMKVY_decription='The Pradhan Mantri Kaushal Vikas Yojana is deemed as Skill India’s flagship skill development scheme. Its objective is to enable youth to take up training in order to secure a better livelihood. Assessment and training fees under this scheme are covered by the Government and individuals with prior experience can get certified.'
            instance_tab.ids.Tab_image.source='http://pmkvyofficial.org/images/logo.png'
            instance_tab.ids.Tab_description.text=f"{PMKVY_decription}"
            
        if instance_tab_label=='Objective':
            Objective_decription='The main objective of the Skill India programme is to provide adequate training in market-relevant skills to over 40 crore youth by 2022. It also aims to create opportunities for the development of talent within the country and improve the overall scope and space for underdeveloped sectors. It does so with assistance from the National Skill Development Corporation or NSDC.'
            instance_tab.ids.Tab_image.source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThY3xvGDjVGKTbo0EdPfUl8-ahB0WlnY6usg&usqp=CAU'
            instance_tab.ids.Tab_description.text=f"{Objective_decription}"
            
        if instance_tab_label=='Courses':
            Courses_decription='Various courses are broadly divided into 5 main categories for Skill India courses, which include: \n 1. Management and development programmes: Financial statement analysis, modern office practice, marketing for managers, etc. \n 2. Training of trainer: Accreditation program for EM trainers, technology infusion, etc. \n 3. Entrepreneurship development programmes: Women EDP, women empowerment, CRR scheme, etc. \n 4 .Skill development programmes: Dairy based ESDP, carpentry, electroplating, fashion designing, etc. \n 5. Other skills: Promotion of micro-enterprises, cluster development, lending strategies for MSMEs, etc.'
            instance_tab.ids.Tab_image.source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhS2heDnCrlrp4iAHoPJAfPOP9Dekha6ssNA&usqp=CAU'
            instance_tab.ids.Tab_description.text=f"{Courses_decription}"
            
        if instance_tab_label=="Schemes":
            Schemes_description='The schemes for skill development in India are as follows: \n 1. Pradhan Mantri Kaushal Vikas Yojana \n 2. Skills Acquisition and Knowledge Awareness for Livelihood Promotion (SANKALP) \n 3. UDAAN \n4. Standard Training Assessment and Reward Scheme (STAR) \n 5. Polytechnic Schemes \n 6. Vocationalization of Education'
            instance_tab.ids.Tab_image.source='https://www.lakshyaskills.com/wp-content/uploads/2018/08/03e-Skill-India.jpg'
            instance_tab.ids.Tab_description.text=f"{Schemes_description}"
            
    def account(self):
        pass

        

Drawer().run()